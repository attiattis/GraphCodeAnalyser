import json

from Neo4jConnection import Neo4jConnection
CONFIG_FILE_NAME = "neo4jConfig.json"

# open the file and load the configurations data 
with open(CONFIG_FILE_NAME) as configFile:
    configData = json.load(configFile)

    # connect to the neo4j server
    conn = Neo4jConnection(configData['neo4jURL'], configData['neo4jUserName'], configData['neo4jPassword'])
    print(type(conn))
    query = "MERGE (n:Person{born:1996}) return n"
    result = conn.query(query)
    query = "MATCH (n:Person{born:1996}) return n"
    result = conn.query(query)
    print(result)
    conn.close()


