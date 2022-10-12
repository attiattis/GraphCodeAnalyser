# GraphCodeAnalyser
We are trying to create a small code analyser for python using neo4j

## how to start
start a Neo4j container
```
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j
```

edit connection string in `neo4jConfig.json`

run connection test
```
python Neo4jConnectionTest.py
```