import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ep1-c"]
collection = db["parcial1"]

# Verificar si la colección ya existe
if "parcial1" not in db.list_collection_names():
    # Si no existe, crearla y agregar los documentos
    parcial1.insert_many(data)
    print("La base de datos y la colección han sido creadas exitosamente!")
else:
    print("La colección ya existe en la base de datos.")


