import json

#Creamos la clase constructora de tareas
class Task:
    #Constructor
    def __init__(self, id, description, completed=False):
        
        self.id = id
        self.description = description
        self.completed = completed

    #Sobreescribimos la función string que tienen todas las funciones. La modificación
    #es para mostrar un texto con nuestro formato.
    def __str__(self):
        status = "✅" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
#Clase gestión de tareas: Definimos toda la lógica principal de la aplicación
class TaskManager:

    FILENAME = "tasks.json"
    #Definimos el constructor
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    #Definimos cada funcionalidad de la clase TaskManager
    #Añadir tarea
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description} ")
        self.save_tasks()
    
    #Listar tareas
    def list_task(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)
    
    #Completar tarea
    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return 
        print(f"Tarea no encontrada: #{id}")

    #Borrar tarea
    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
        print("Tarea no encontrada: #{id}")

    #Cargar archivo Json
    def load_tasks(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], 
                                    item["description"], 
                                    item["completed"]) 
                                    for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
        except FileNotFoundError:
            self._tasks = []

    #Guardar archivo Json
    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([{"id": task.id, 
                        "description": task.description, 
                        "completed": task.completed}
                        for task in self._tasks], file, indent=4)