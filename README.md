# Elasticsearch

## Nettoyage Docker

sudo docker ps -a

sudo docker stop

sudo docker rm

## Docker multi node architecture

cd multi_node_architecture

sudo docker-compose-up

curl -XPUT 'http://localhost:9200/cities' -H 'Content-Type: application/json' -d '
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}'

curl -XPOST 'http://localhost:9200/cities/_doc' -H 'Content-Type: application/json' -d '
{
  "city": "London",
  "country": "England"
}'

sudo bash insert_data.sh

## Kibana

cd kibana

sudo docker-compose up

curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/json" --data-binary "@movies.json"

url pour la console : http://localhost:5601/app/dev_tools#/console

## Python API Overview

cd overview_python

sudo docker-compose up

Vérifier l'état : curl -X GET "localhost:9200/_cat/indices?v" 

python3 main.py