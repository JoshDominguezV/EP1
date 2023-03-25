from conection_parameters import collection
import json


def read_products(nombre=None):
    if nombre is not None:
        query = {"name": nombre}
        document = collection.find_one(query)
        print(document)
        if document is not None:
            print(document)
        else:
            print("No se encontró ningún producto con ese nombre.")
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def create_product(json_product):
    result = collection.insert_one(json_product)
    print("Se ha agregado el producto con ID:", result.inserted_id)

def update_product(nombre, json_product_update):
    query = {"name": nombre}
    new_values = {"$set": json_product_update}
    result = collection.update_one(query, new_values)
    if result.modified_count > 0:
        print("Se ha actualizado el producto con nombre:", nombre)
    else:
        print("No se encontró ningún producto con ese nombre.")

def delete_product(nombre):
    query = {"name": nombre}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        print("Se ha eliminado el producto con nombre:", nombre)
    else:
        print("No se encontró ningún producto con ese nombre.")

def filter_products(categoria):
    query = {"category": categoria}
    documents = collection.find(query)
    for document in documents:
        print(document)
