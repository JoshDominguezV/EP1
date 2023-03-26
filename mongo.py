import pymongo
import json

# Crear una conexión con el servidor de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear una base de datos llamada "ep1-c"
mydb = client["ep1-c"]

# Crear una colección llamada "parcial1" en la base de datos
parcial1 = mydb["parcial1"]

# Leer los datos del archivo JSON
with open('data.json') as file:
    data = json.load(file)

# Insertar los datos en la colección "parcial1"
parcial1.insert_many(data)

# Imprimir el número de documentos insertados
print(parcial1.count_documents({}))
