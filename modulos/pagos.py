import csv
import os

ARCHIVO_PAGOS = "datos/pagos.csv"

def menu_pagos():
    """Funcion principal que muestra un menu de pagos"""
    while True:
        print("\n--- Gestión de Pagos ---")
        print("1. Registrar pago")
        print("2. Listar pagos")
        print("3. Buscar pagos por cliente")
        print("4. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_pago()
        elif opcion == "2":
            listar_pagos()
        elif opcion == "3":
            buscar_pagos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def registrar_pago():
    """Esta funcion solicita al usuario el nombre del clientes,
      el mes abonado y el monto correspondiente. 
      Luego registra esta informacion en un archivo csv"""
    
    cliente = input("Nombre del cliente: ").strip()
    mes = input("Mes abonado (Ej: Enero, Febrero): ").strip()
    monto = input("Monto: ").strip()

    with open(ARCHIVO_PAGOS, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([cliente, mes, monto])

    print("✔ Pago registrado correctamente.")


def listar_pagos():
    if not os.path.exists(ARCHIVO_PAGOS):
        print("No hay pagos registrados.")
        return

    with open(ARCHIVO_PAGOS, "r") as archivo:
        reader = csv.reader(archivo)

        print("\n--- LISTA DE PAGOS ---")
        for fila in reader:
            print(f"Cliente: {fila[0]} - Mes: {fila[1]} - Monto: ${fila[2]}")


def buscar_pagos():
    """Permite buscar pagos especificos utilizando el nombre del cliente"""
    nombre = input("Nombre del cliente: ").lower()

    if not os.path.exists(ARCHIVO_PAGOS):
        print("No hay pagos registrados.")
        return

    encontrado = False

    with open(ARCHIVO_PAGOS, "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if nombre in fila[0].lower():
                if not encontrado:
                    print("\n--- PAGOS ENCONTRADOS ---")
                print(f"Cliente: {fila[0]} - Mes: {fila[1]} - Monto: ${fila[2]}")
                encontrado = True

    if not encontrado:
        print("No hay pagos registrados para ese cliente.")