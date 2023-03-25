from crud import *
from basic_functions import *

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
