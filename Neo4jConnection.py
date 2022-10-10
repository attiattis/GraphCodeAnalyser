from neo4j import GraphDatabase
class Neo4jConnection:
    def __init__(self, url, username, password):
        self.__url = url
        self.__username = username
        self.__password = password
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__url, auth=(self.__username, self.__password))
        except Exception as e:
            print("Not able to connect to GraphDatabase", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, parameters=None, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

