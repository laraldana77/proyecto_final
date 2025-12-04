import csv
import os

ARCHIVO_CLIENTES= "datos/clientes.csv"

def menu_clientes():
    """Se define la funcion menu de clientes, la cual continene un bucle while que permite ejecutar el menu repetidamente"""
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def registrar_cliente():
    """Esta funcion registra un nuevo cliente.Escribe el nombre,
      edad y telefono del cliente en un archivo"""
    nombre = input("Nombre del cliente: ").strip()
    edad = input("Edad: ")
    telefono = input("Teléfono: ")

    with open(ARCHIVO_CLIENTES, "a", newline="") as archivo:
        """Esta funcion abre el archivo"""
        writer = csv.writer(archivo)
        writer.writerow([nombre, edad, telefono])
        """Escribe una cadena de texto en el archivo """

    print("Cliente registrado correctamente.")

def listar_clientes():
    """Esta funcion lista todos los clientes registrados"""
    if not os.path.exists(ARCHIVO_CLIENTES):
        """Verifica si el cliente existe"""
        print("No hay clientes cargados.")
        return

    with open(ARCHIVO_CLIENTES, "r") as archivo:
        reader = csv.reader(archivo)
        print("\n--- LISTA DE CLIENTES ---")
        for fila in reader:
            print(f"Nombre: {fila[0]} - Edad: {fila[1]} - Teléfono: {fila[2]}")

def buscar_cliente():
    """ESta funcion busca un cliente por su nombre"""
    nombre = input("Ingrese nombre a buscar: ").lower()

    with open(ARCHIVO_CLIENTES, "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            if nombre in fila[0].lower():
                print(f"Encontrado: {fila}")
                return

    print("Cliente no encontrado.")
