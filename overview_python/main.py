import warnings
from elasticsearch import Elasticsearch
warnings.filterwarnings('ignore')

import requests
res = requests.get('http://localhost:9200?pretty')
#print(res.content)

es = Elasticsearch('http://localhost:9200')

#create
#es.indices.create(index="first_index",ignore=400)

#verify
#print(es.indices.exists(index="first_index"))

#delete
#print(es.indices.delete(index="first_index", ignore=[400,404]), "oui")

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Inserting doc1 in id=1
es.index(index="cities", id=1, document=doc1)

#Inserting doc2 in id=2
es.index(index="cities", id=2, document=doc2)

#Inserting doc3 in id=3
es.index(index="cities", id=3, document=doc3)

response = es.index(index="cities", id=1, document=doc1)
#print(response)

#res = es.get(index="cities", id=2)
res = es.search(index="cities", body={"query":{"match_all":{}}})
print(res)

print(es.search(index="cities", body={"query": {"regexp" : { "city" : "l.*n" }}}))