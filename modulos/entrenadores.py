import csv
import os

ARCHIVO_ENTRENADORES= "datos/entrenadores.csv"
def menu_entrenadores():
    """Se define la función menu de entrenadores, la cual contiene un bucle while
      que permite ejecutar el menú continuamente hasta que el usuario decida salir."""
    while True:
        print("\n--- Gestión de Entrenadores ---")
        print("1. Registrar entrenador")
        print("2. Listar entrenadores")
        print("3. Buscar entrenador")
        print("4. Volver")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            registrar_entrenador()
        elif opcion == "2":
            listar_entrenadores()
        elif opcion == "3":
            buscar_entrenador()
        elif opcion =="4":
            break
        else:
            print("Opcion invalida")

def registrar_entrenador():
    nombre=input("Nombre del entrenador: ").strip()
    especialidad=input("Especialidad: ").strip()
    telefono=input("Telefono: ").splip()

    entrenador=[nombre, especialidad, telefono]

    if not os.path.isfile(ARCHIVO_ENTRENADORES):
        with open(ARCHIVO_ENTRENADORES, mode='w', newline='') as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(entrenador)

        print("Entrenador registrado exitosamente")

def listar_entrenadores():
    if not os.path.isfile(ARCHIVO_ENTRENADORES):
        print("No hay entreandores registrados aún.")
        return
    
    with open(ARCHIVO_ENTRENADORES, "r") as archivo:
        lector = csv.reader(archivo)
        print("\n--- LISTA DE ENTRENADORES ---")
        for fila in lector:
            print(f"Nombre: {fila[0]} - Especialidad: {fila[1]} - Teléfono: {fila[2]}")


def buscar_entrenador():
 nombre = input("Ingrese nombre a buscar: ").lower()

 with open(ARCHIVO_ENTRENADORES, "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if nombre in fila[0].lower():
                print(f"Encontrado: {fila}")
                return

print("Entrenador no encontrado.")
