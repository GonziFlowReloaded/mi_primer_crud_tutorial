# mi_primer_crud_tutorial

Este proyecto es un CRUD básico desarrollado con FastAPI y MongoDB. Permite crear, leer, actualizar y eliminar tareas.

## Requisitos previos

- Python 3.9 o superior
- MongoDB en ejecución
- `pip` para instalar dependencias

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/GonziFlowReloaded/mi_primer_crud_tutorial.git
   cd mi_primer_crud_tutorial
   ```

2. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura la conexión a MongoDB en el archivo `core/mongo.py` (si es necesario).

## Ejecución del proyecto

1. Inicia el servidor FastAPI:
   ```bash
   python app.py
   ```

2. Accede a la documentación interactiva de la API en:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints principales

- **POST /tareas/**: Crear una nueva tarea.
- **GET /tareas/{tarea_id}**: Obtener una tarea por su ID.
- **PUT /tareas/{tarea_id}**: Actualizar una tarea existente.
- **DELETE /tareas/{tarea_id}**: Eliminar una tarea por su ID.
- **GET /tareas/**: Listar todas las tareas.

## Estructura del proyecto

```
.
├── api/
│   └── tareas.py          # Endpoints relacionados con tareas
├── core/
│   └── mongo.py           # Configuración de la base de datos MongoDB
├── models/
│   └── models.py          # Modelos de datos para las tareas
├── app.py                 # Punto de entrada de la aplicación
└── README.md              # Documentación del proyecto
```

## Notas

- Asegúrate de que MongoDB esté en ejecución antes de iniciar el servidor.
- Puedes personalizar los modelos y la lógica según tus necesidades.
