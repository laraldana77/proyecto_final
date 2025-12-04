import csv
import os

ARCHIVO_RUTINAS = "datos/rutinas.csv"

def menu_rutinas():
    """Muestra un menu de opciones para gestionar rutinas """

    while True:
        print("\n--- Gestión de Rutinas ---")
        print("1. Crear rutina")
        print("2. Listar rutinas")
        print("3. Buscar rutina por cliente")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_rutina()
        elif opcion == "2":
            listar_rutinas()
        elif opcion == "3":
            buscar_rutina()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def crear_rutina():
    """Recopila la informacion necesaria del usuario para crear una rutina"""

    cliente = input("Nombre del cliente: ").strip()
    objetivo = input("Objetivo (Ej: Bajar de peso, Ganar músculo): ").strip()
    dias = input("Días por semana: ").strip()
    ejercicios = input("Ejercicios (separados por comas): ").strip()

    """Se utiliza strip en las entradas para eliminar los espacios en blanco """

    with open(ARCHIVO_RUTINAS, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([cliente, objetivo, dias, ejercicios])

    print("✔ Rutina registrada correctamente.")


def listar_rutinas():
    """Muestra en pantalla todas las rutinas registradas"""

    if not os.path.exists(ARCHIVO_RUTINAS):
        print("No hay rutinas registradas.")
        return
    
    with open(ARCHIVO_RUTINAS, "r") as archivo:
        reader = csv.reader(archivo)
        """Si existen rutinas registradas, abre el archivo en modo lectura, lee las filas del archivo csv y luego imprime"""

        print("\n--- LISTA DE RUTINAS ---")
        for fila in reader:
            cliente, objetivo, dias, ejercicios = fila
            print(f"\nCliente: {cliente}")
            print(f"Objetivo: {objetivo}")
            print(f"Días/semana: {dias}")
            print(f"Ejercicios: {ejercicios}")


def buscar_rutina():
    """Busca una rutina especifica por el nombre del cliente"""
    nombre = input("Nombre del cliente a buscar: ").lower()

    if not os.path.exists(ARCHIVO_RUTINAS):
        print("No hay rutinas registradas.")
        return

    with open(ARCHIVO_RUTINAS, "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if nombre in fila[0].lower():
                print("\n--- RUTINA ENCONTRADA ---")
                print(f"Cliente: {fila[0]}")
                print(f"Objetivo: {fila[1]}")
                print(f"Días/semana: {fila[2]}")
                print(f"Ejercicios: {fila[3]}")
                return

    print("No se encontró la rutina de ese cliente.")