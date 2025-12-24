# TaskManagerCLI 📋

Una aplicación de **gestor de tareas en línea de comandos** integrada con **Inteligencia Artificial** para descomponer tareas complejas en pasos simples y accionables.

## 📖 Descripción del Proyecto

**TaskManagerCLI** es una herramienta interactiva diseñada para la gestión eficiente de tareas desde la terminal. Combina funcionalidades de un gestor de tareas tradicional con la capacidad de utilizar **IA generativa (Gemini)** para dividir automáticamente tareas complejas en subtareas manejables.

Este proyecto es una **aplicación integradora de conceptos** del _Master de Desarrollo con IA_, demostrando competencias en:

- Desarrollo en Python
- Arquitectura orientada a objetos
- Persistencia de datos (JSON)
- Integración con APIs externas
- Patrones de diseño
- Testing y control de calidad

---

## ✨ Características Principales

### 🎯 Funcionalidades Básicas

- ✅ **Añadir tareas** - Crear nuevas tareas con descripción
- 📝 **Listar tareas** - Ver todas las tareas con estado de completado
- ✓ **Completar tareas** - Marcar tareas como completadas
- 🗑️ **Eliminar tareas** - Remover tareas del gestor
- 💾 **Persistencia** - Las tareas se guardan automáticamente en `tasks.json`

### 🤖 Funcionalidades de IA

- 🧠 **Generación de subtareas** - Usa la API de Gemini para descomponer tareas complejas
- 📊 **Análisis inteligente** - Crea entre 3 y 5 subtareas accionables automáticamente
- 🔄 **Integración fluida** - Las subtareas se añaden directamente al gestor

---

## 🏗️ Arquitectura y Estructura

```bash
TaskManagerCli/
├── main.py                  # Punto de entrada y UI interactiva
├── taskmanager.py          # Lógica principal (TaskManager y Task)
├── ai_service.py           # Integración con API de Gemini
├── tasks.json              # Archivo de persistencia de tareas
├── requirements.txt        # Dependencias del proyecto
├── tests/                  # Suite de tests
│   ├── test_taskmanager.py # Tests unitarios
│   └── __pycache__/
├── .venv/                  # Entorno virtual de Python
├── LICENSE                 # Licencia del proyecto
└── README.md              # Este archivo
```

### 📦 Módulos Principales

#### **main.py** - Interfaz de Usuario

```python
# Menú interactivo con opciones:
# 1. Añadir Tarea
# 2. Añadir Tarea Compleja (con IA)
# 3. Listar Tareas
# 4. Completar Tarea
# 5. Eliminar Tarea
# 6. Salir
```

#### **taskmanager.py** - Lógica de Negocio

- **Clase `Task`**: Representa una tarea individual

  - Propiedades: `id`, `description`, `completed`
  - Método especial `__str__()` para visualización con emoji ✅/✓

- **Clase `TaskManager`**: Gestor completo de tareas
  - `add_task(description)` - Añadir tarea
  - `list_task()` - Listar todas las tareas
  - `complete_task(id)` - Marcar como completada
  - `delete_task(id)` - Eliminar tarea
  - `load_tasks()` - Cargar desde JSON
  - `save_tasks()` - Guardar en JSON

#### **ai_service.py** - Integración con IA

- **Función `create_simple_tasks(description)`**
  - Conecta con la API de Gemini vía OpenAI
  - Desglosa tareas complejas en subtareas
  - Manejo de errores y excepciones
  - Parseo inteligente de respuestas

---

## 🚀 Instalación y Configuración

### Requisitos Previos

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- Conexión a Internet

### Pasos de Instalación

1.**Clonar o descargar el repositorio**

```bash
git clone <url-del-repositorio>
cd TaskManagerCli
```

2.**Crear entorno virtual**

```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows
```

3.**Instalar dependencias**

```bash
pip install -r requirements.txt
```

4.**Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto:

```env
GEMINI_API_KEY=tu_clave_api_de_gemini_aqui
```

> **Nota**: Obtén tu clave de API en [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 💻 Uso

### Ejecutar la Aplicación

```bash
python main.py
```

### Ejemplos de Uso

**Ejemplo 1: Añadir una tarea simple**

```
--- Gestor de Tareas ---
1. Añadir Tarea
2. Añadir Tarea Compleja (con IA)
3. Listar Tareas
4. Completar Tarea
5. Eliminar Tarea
6. Salir

Elige una opción: 1
Descripción de la tarea: Comprar leche
Tarea añadida: Comprar leche
```

**Ejemplo 2: Descomponer tarea compleja con IA**

```
Elige una opción: 2
Descripción de la tarea compleja: Organizar una reunión de equipo
```

_La IA generará automáticamente subtareas como:_

- Definir fecha y hora de la reunión
- Enviar invitaciones a los participantes
- Preparar orden del día
- Reservar sala de conferencias
- Enviar recordatorio el día antes

**Ejemplo 3: Listar y completar tareas**

```bash
Elige una opción: 3
[ ] #1: Comprar leche
[ ] #2: Definir fecha y hora de la reunión
[ ] #3: Enviar invitaciones a los participantes
[✅] #4: Preparar orden del día

Elige una opción: 4
ID de la tarea a completar: 1
Tarea completada: [✅] #1: Comprar leche
```

---

## 📚 Dependencias

El proyecto utiliza las siguientes librerías principales:

| Dependencia     | Versión | Propósito                       |
| --------------- | ------- | ------------------------------- |
| `openai`        | 2.11.0  | Cliente para API de Gemini      |
| `python-dotenv` | 1.2.1   | Gestión de variables de entorno |
| `google-genai`  | 1.56.0  | SDK de Google Generative AI     |
| `pydantic`      | 2.12.5  | Validación de datos             |
| `pytest`        | 9.0.2   | Framework de testing            |
| `requests`      | 2.32.5  | Cliente HTTP                    |

Ver [requirements.txt](requirements.txt) para la lista completa.

---

## 🧪 Testing

### Ejecutar Tests

```bash
pytest tests/
```

### Ejecutar con Verbosidad

```bash
pytest tests/ -v
```

### Cobertura de Tests

```bash
pytest tests/ --cov
```

---

## 📊 Persistencia de Datos

Las tareas se guardan automáticamente en formato **JSON** en el archivo `tasks.json`:

```json
[
  {
    "id": 1,
    "description": "Comprar leche",
    "completed": false
  },
  {
    "id": 2,
    "description": "Preparar presentación",
    "completed": true
  }
]
```

---

## 🔧 Configuración Avanzada

### Personalizar Parámetros de IA

En `ai_service.py`, puedes modificar:

```python
params = {
    "model": "gemini-3-flash-preview",  # Modelo de IA
    "reasoning_effort": "low",            # Esfuerzo de razonamiento
}
```

### Variables de Entorno

Además de `GEMINI_API_KEY`, puedes configurar:

- Ruta del archivo de tareas
- Número de subtareas a generar
- Parámetros de timeout

---

## 📋 Conceptos Aplicados

Este proyecto demuestra competencias en:

### Programación Python

- ✅ Clases y objetos
- ✅ Métodos mágicos (`__str__`, `__init__`)
- ✅ Estructuras de control (match-case)
- ✅ Manejo de excepciones
- ✅ Lectura/escritura de archivos

### Arquitectura

- ✅ Separación de responsabilidades (MVC)
- ✅ Modularización del código
- ✅ Patrón Manager
- ✅ Inyección de dependencias

### API Integration

- ✅ Consumo de APIs REST
- ✅ Autenticación con claves
- ✅ Parseo de respuestas JSON
- ✅ Manejo de errores HTTP

### Persistencia

- ✅ Serialización JSON
- ✅ Carga/guardado automático
- ✅ Gestión de estado

### Testing

- ✅ Pruebas unitarias
- ✅ Fixtures y mocks
- ✅ Assertions

---

## 🐛 Solución de Problemas

### "Error: La API KEY de GEMINI no está configurada"

**Solución**: Asegúrate de que el archivo `.env` existe y contiene `GEMINI_API_KEY`

### "ModuleNotFoundError: No module named 'openai'"

**Solución**: Ejecuta `pip install -r requirements.txt`

### Las tareas no se guardan

**Solución**: Verifica que tienes permisos de escritura en el directorio del proyecto

### Error de conexión con la API

**Solución**: Verifica tu conexión a internet y que la API key es válida

---

## 📝 Licencia

Este proyecto está licenciado bajo los términos de la [LICENSE](LICENSE)

---

## 👤 Autor

Desarrollado como parte del **Master de Desarrollo con IA** de TheBigSchool y por @cybermito.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios significativos, por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit los cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Soporte

Si tienes preguntas o encuentras problemas, por favor abre un issue en el repositorio.

---

**¡Gracias por usar TaskManagerCLI!** 🎉
