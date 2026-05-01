# PhotoCampus

Sistema de gestión de servicios fotográficos desarrollado en Python. Permite crear, editar y eliminar servicios fotográficos almacenados en un archivo JSON.
---

## Configuración y uso

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd PhotoCampus
```

### 2. Ejecutar el programa

```bash
python main.py
```

### 3. Opciones del menú

Al ejecutar el programa verás el siguiente menú:

```
1. Crear servicio fotográfico
2. Eliminar servicio fotográfico
3. Actualizar servicio fotográfico
4. Salir
```

**Crear:** Ingresa código, nombre, duración, precio y tipo de evento (Boda / Retrato / Producto).

**Eliminar:** Ingresa el código del servicio que deseas eliminar.

**Actualizar:** Ingresa el código del servicio a modificar y luego los nuevos datos.

**Salir:** Cierra la aplicación.

---

## Estructura del repositorio

```
PhotoCampus/
│
├── main.py                  # Punto de entrada — muestra el menú principal
├── servicioFotografico.py   # Módulo para crear servicios
├── featureeditservices.py   # Módulo para editar/actualizar servicios
├── eliminarServicios.py     # Módulo para eliminar servicios
├── utilidades.py            # Funciones compartidas: validación, lectura y escritura JSON
├── servicios.json           # Base de datos local con los servicios registrados
└── README.md                # Este archivo
```
