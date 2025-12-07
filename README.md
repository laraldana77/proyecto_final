# 🏋️‍♂️ Sistema de Gestión de Gimnasio

Este proyecto es un sistema modular desarrollado en Python para gestionar la información principal de un gimnasio.  
Permite registrar socios, profesores, actividades, inscripciones y pagos, utilizando archivos CSV como base de almacenamiento.

---

## 📌 Características principales

### ✔ Gestión de Socios
- Alta de nuevos socios  
- Búsqueda por nombre o DNI  
- Listado completo  
- Eliminación de datos  

### ✔ Gestión de Profesores
- Registro de instructores  
- Listado general  
- Consulta individual  

### ✔ Gestión de Actividades
- Cargar nuevas actividades  
- Listar actividades disponibles  
- Inscribir socios  
- Vincular actividad + socio en archivo CSV  

### ✔ Gestión de Pagos
- Registrar pagos de socios  
- Listar pagos  
- Consultar estado de deuda  

### ✔ Menú Principal
Un menú central permite navegar a cada módulo de forma ordenada.

---

## 📂 Estructura del proyecto
/proyecto-gym
│── main.py
│── socios.py
│── profesores.py
│── actividades.py
│── pagos.py
│── socios.csv
│── actividades.csv
│── profesores.csv
│── pagos.csv
│── inscripciones.csv
└── README.md

## 🛠 Tecnologías utilizadas

- *Python 3*
- *CSV* para almacenamiento de datos
- Librerías estándar:
  - csv para leer y escribir archivos
  - os para manejo de archivos

## ▶ Cómo ejecutar el sistema

1. Clonar el repositorio:

```bash
git clone https://github.com/laraldana77/tp_integrador

```
2. Ingresa al directorio
   cd proyecto-gym
4. Ejecuta el programa
   python main.py

##👤 Autora

Proyecto desarrollado por Lara Aldana como parte de una práctica de programación en Python
