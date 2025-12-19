#Importamos el módulo con la lógica de gestión de tareas
from taskmanager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    #Menú
        print("\n--- Gestor de Tareas ---")
        print("1. Añadir Tarea")
        print("2. Añadir Tarea Compleja (con IA)")
        print("3. Listar Tareas")
        print("4. Completar Tarea")
        print("5. Eliminar Tarea")
        print("6. Salir")

#Función principal, UI
def main():

    #instanciamos el gestor de tareas
    manager = TaskManager()

    while True:
        print_menu()
        
        try:

            choice = int(input("Elige una opción: "))

            #Bloque de selección tipo switch case, en python se llama match case
            match choice:
                case 1: #Añadir tarea
                    # Solicitamos la descripción de la tarea
                    description = input("Descripción de la tarea: ")
                    manager.add_task(description)

                case 2: #Tarea compleja con IA
                    description = input("Descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break


                case 3: #Listar tareas
                    manager.list_task()

                case 4: #Completar tarea
                    id_a_entero = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id_a_entero)

                case 5: #Eliminar tarea
                    id_a_entero = int(input("ID de la tarea a eliminar: "))
                    manager.delete_task(id_a_entero)

                case 6:
                    print("\nSaliendo...")
                    break

                case _: #Opción por defecto
                    print("\nOpción no válida. Selecciona otra.")

        except ValueError:
            print("Opción incorrecta, seleccione otra.")


#Inicio del programa
if __name__ == "__main__":
    main()

            