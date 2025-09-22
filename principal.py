"""
Se trata de incluir las opciones necesarias para los
CRUD de productos y clientes.
"""

import json

from clientes import Clientes
from productos import Productos

try:
    with open("productos.json", "r", encoding="utf-8") as archivo:
        listado = json.load(archivo)
except FileNotFoundError:
    listado = []

mis_productos = Productos(listado)

try:
    with open("clientes.json", "r", encoding="utf-8") as archivo:
        listado_clientes = json.load(archivo)
except FileNotFoundError:
    listado_clientes = []

mis_clientes = Clientes(listado_clientes) 

def gestionar_productos():
    while True:
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Eliminar producto")
        print("4. Modificar producto")
        print("0. Salir\n")
        opcion = input("Digite su opción: ")
        if opcion == "1":
            cod = input("Código: ")
            nom = input("Nombre: ")
            pre = float(input("Precio: "))
            sal = int(input("Saldo: "))
            nuevo_producto = {"codigo": cod,
                              "nombre": nom,
                              "precio": pre,
                              "saldo": sal}
            resultado = mis_productos.agregar(nuevo_producto)
            if resultado == 0:
                print("Producto agregado satisfactoriamente!")
            else:
                print("Código de producto ya existe!")
        elif opcion == "2":
            cod = input("Digite código a buscar: ")
            resultado = mis_productos.buscar(cod)
            if resultado == -1:
                print("Producto no existe!")
            else:
                print(listado[resultado])
        elif opcion == "3":
            cod = input("Digite código a eliminar: ")
            resultado = mis_productos.eliminar(cod)
            if resultado == 0:
                print("Producto eliminado satisfactoriamente!")
            else:
                print("Producto no existe!")
        elif opcion == "4":
            cod = input("Digite código a modificar: ")
            resultado = mis_productos.buscar(cod)
            if resultado == -1:
                print("Producto no existe!")
            else:
                print("Producto encontrado:")
                print(listado[resultado])
                nom = input("Nuevo nombre: ")
                pre = float(input("Nuevo precio: "))
                sal = int(input("Nuevo saldo: "))
                producto_modificado = {"codigo": cod,
                                        "nombre": nom,
                                        "precio": pre,
                                        "saldo": sal}
                mis_productos.modificar(producto_modificado)
        elif opcion == "0":
            break

def gestionar_clientes():
    while True:
        print("1. Agregar cliente")
        print("2. Buscar Cliente")
        print("3. Eliminar Cliente")
        print("4. Modificar Cliente")
        print("0. Salir\n")
        opcion = input("Digite su opción: ")
        if opcion == "1":
            ident = input("Identificación: ")
            nom = input("Nombre: ")
            saldo = float(input("Saldo:"))
            cupo_credito = float(input("Cupo de crédito: "))
            nuevo_cliente = {
                "identificacion": ident,
                "nombre": nom,
                "saldo": saldo,
                "cupo_credito": cupo_credito}
            mis_clientes.agregar(nuevo_cliente)
        elif opcion == "2":
            ident = input("Digite identificación a buscar: ")
            resultado = mis_clientes.buscar(ident)
            if resultado == -1:
                print("Cliente no existe!")
            else:
                print(listado_clientes[resultado])
        elif opcion == "3":
            ident = input("Digite identificación a eliminar: ")
            resultado = mis_clientes.eliminar(ident)
            if resultado == 0:
                print("Cliente eliminado satisfactoriamente!")
            else:
                print("Cliente no existe!")
        elif opcion == "4":
            ident = input("Digite identificación a modificar: ")
            resultado = mis_clientes.buscar(ident)
            if resultado == -1:
                print("Cliente no existe!")
            else:
                print("Cliente encontrado:")
                print(listado_clientes[resultado])
                nom = input("Nuevo nombre: ")
                saldo = float(input("Nuevo saldo: "))
                cupo_credito = float(input("Nuevo cupo de crédito: "))
                cliente_modificado = {
                    "identificacion": ident,
                    "nombre": nom,
                    "saldo": saldo,
                    "cupo_credito": cupo_credito}
                mis_clientes.modificar(ident, cliente_modificado)
        elif opcion == "0":
            break

gestionar_productos()
gestionar_clientes()


with open("productos.json", "w", encoding="utf-8") as archivo:
    json.dump(listado, archivo, indent=4, ensure_ascii=False)

with open("clientes.json", "w", encoding="utf-8") as archivo:
    json.dump(listado_clientes, archivo, indent=4, ensure_ascii=False)
