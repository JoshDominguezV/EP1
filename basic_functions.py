import json
from conection_parameters import collection


def create_product_json():
    print("Ingrese los siguientes datos del producto:")
    name = input("Nombre: ")
    description = input("Descripción: ")
    price = float(input("Precio: "))
    category = input("Categoría: ")
    stock = int(input("Stock: "))
    product = {"name": name, "description": description, "price": price, "category": category, "stock": stock}
    return product


def json_product_update():
    print("Ingrese los datos a modificar del producto")
    name = input("Nombre (dejar en blanco si no desea modificar): ")
    description = input("Descripción (dejar en blanco si no desea modificar): ")
    price = input("Precio (dejar en blanco si no desea modificar): ")
    category = input("Categoría (dejar en blanco si no desea modificar): ")
    stock = input("Stock (dejar en blanco si no desea modificar): ")
    product_update = {}
    if name != "":
        product_update["name"] = name
    if description != "":
        product_update["description"] = description
    if price != "":
        product_update["price"] = float(price)
    if category != "":
        product_update["category"] = category
    if stock != "":
        product_update["stock"] = int(stock)
    return product_update


def get_all_products():
    documents = collection.find()
    products = [doc for doc in documents]
    return products


def get_products_by_category(category):
    query = {"category": category}
    documents = collection.find(query)
    products = [doc for doc in documents]
    return products


def get_product_by_name(name):
    query = {"name": name}
    document = collection.find_one(query)
    return document
