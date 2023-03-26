from crud import *
from basic_functions import *

while True:
    print("Desea crear la base de datos? si la base de datos ya esta creada escoja la opcion 2 ")
    print("1. SI")
    print("2. NO, seguir al menu.")
    print("3. Salir")
    opcion1 = input("Ingrese una opción: ")
    print("\n\n")
    if opcion1 == "1":
        from mongo import *
        from conection_parameters import *
        # Verificar si la colección ya existe
        if "parcial1" not in db.list_collection_names():
            # Si no existe, crearla y agregar los documentos
            parcial1.insert_many(data)
            print("La base de datos y la colección han sido creadas exitosamente! \n")
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
                    print("\n\n")
                elif opcion == "2":
                    category = input("Ingrese la categoría a filtrar: ")
                    filter_products(category)
                    print("\n\n")

                elif opcion == "3":
                    name = input("Ingrese el nombre del producto a buscar: ")
                    read_products(name)
                    print("\n\n")

                elif opcion == "4":
                    product = create_product_json()
                    create_product(product)
                    print("\n\n")

                elif opcion == "5":
                    name = input("Ingrese el nombre del producto a modificar: ")
                    product_update = json_product_update()
                    update_product(name, product_update)
                    print("\n\n")

                elif opcion == "6":
                    name = input("Ingrese el nombre del producto a eliminar: ")
                    delete_product(name)
                    print("\n\n")

                elif opcion == "7":
                    print("Saliendo del sistema...")
                    print("\n\n")
                    break

                else:
                    print("Opción no válida. Intente nuevamente.\n")
        else:
            print("La colección ya existe en la base de datos.\n")
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
                    print("\n\n")
                elif opcion == "2":
                    category = input("Ingrese la categoría a filtrar: ")
                    filter_products(category)
                    print("\n\n")

                elif opcion == "3":
                    name = input("Ingrese el nombre del producto a buscar: ")
                    read_products(name)
                    print("\n\n")

                elif opcion == "4":
                    product = create_product_json()
                    create_product(product)
                    print("\n\n")

                elif opcion == "5":
                    name = input("Ingrese el nombre del producto a modificar: ")
                    product_update = json_product_update()
                    update_product(name, product_update)
                    print("\n\n")

                elif opcion == "6":
                    name = input("Ingrese el nombre del producto a eliminar: ")
                    delete_product(name)
                    print("\n\n")

                elif opcion == "7":
                    print("Saliendo del sistema...")
                    print("\n\n")
                    break

                else:
                    print("Opción no válida. Intente nuevamente.\n")


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
                print("\n\n")
            elif opcion == "2":
                category = input("Ingrese la categoría a filtrar: ")
                filter_products(category)
                print("\n\n")

            elif opcion == "3":
                name = input("Ingrese el nombre del producto a buscar: ")
                read_products(name)
                print("\n\n")

            elif opcion == "4":
                product = create_product_json()
                create_product(product)
                print("\n\n")

            elif opcion == "5":
                name = input("Ingrese el nombre del producto a modificar: ")
                product_update = json_product_update()
                update_product(name, product_update)
                print("\n\n")

            elif opcion == "6":
                name = input("Ingrese el nombre del producto a eliminar: ")
                delete_product(name)
                print("\n\n")

            elif opcion == "7":
                print("Saliendo del sistema...")
                print("\n\n")
                break

            else:
                print("Opción no válida. Intente nuevamente.\n")
    elif opcion1 == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.\n")

