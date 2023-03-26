from crud import *
from basic_functions import *
while True:
    print("Desea crear la base de datos? si la base de datos ya esta creada escoja la opcion 2 ")
    print("1. SI")
    print("2. NO, seguir al menu.")
    print("3. Salir")
    opcion1 = input("Ingrese una opción: ")
    if opcion1 == "1":
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
    elif opcion1 == "2":
        while True:
            print("Menu de opciones")
            print("1. Ver todos los productos")
            print("2. Filtrar productos por categoría")
            print("3. Buscar un producto por nombre")
            print("4. Agregar un producto")
            print("5. Modificar un producto")
            print("6. Eliminar un producto")
            print("7. Salir del sistema")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                read_products()

            elif opcion == "2":
                category = input("Ingrese la categoría a filtrar: ")
                filter_products(category)

            elif opcion == "3":
                name = input("Ingrese el nombre del producto a buscar: ")
                read_products(name)

            elif opcion == "4":
                product = create_product_json()
                create_product(product)

            elif opcion == "5":
                name = input("Ingrese el nombre del producto a modificar: ")
                product_update = json_product_update()
                update_product(name, product_update)

            elif opcion == "6":
                name = input("Ingrese el nombre del producto a eliminar: ")
                delete_product(name)

            elif opcion == "7":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.\n")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.\n")

