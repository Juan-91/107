import pymongo
import certifi
con_str="mongodb+srv://Test_1:test1@cluster0.uzbis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=pymongo.MongoClient(con_str, tlsCAfile=certifi.where())
db=client.get_database("organika")