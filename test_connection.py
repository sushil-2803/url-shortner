from itertools import count
from pymongo import MongoClient

clinet =MongoClient()

client = MongoClient('mongodb://localhost:27017/')

mydatabase = client['url_shortner']

mycollection=mydatabase['urls']

# rec={
#     'url':'https://google.com',
#     'code':'mymy'
# }
# record=mydatabase['urls'].insert_one(rec)

# cursor=mydatabase['urls'].find({"code":'mymy123'})
# for x in cursor:
#     print(x)
# print(len(cursor))