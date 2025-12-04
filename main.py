from modulos.clientes import menu_clientes
from modulos.rutinas import menu_rutinas
from modulos.pagos import menu_pagos

def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE GIMNASIO ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de Rutinas")
        print("3. Gestión de Pagos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_rutinas()
        elif opcion == "3":
            menu_pagos()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "_main_":
    menu_principal()
    