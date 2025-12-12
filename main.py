#Importamos el módulo con la lógica de gestión de tareas
from taskmanager import TaskManager

def print_menu():
    #Menú
        print("\n--- Gestor de Tareas ---")
        print("1. Añadir Tarea")
        print("2. Listar Tareas")
        print("3. Completar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")

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


                case 2: #Listar tareas
                    manager.list_task()

                case 3: #Completar tarea
                    id_a_entero = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id_a_entero)

                case 4: #Eliminar tarea
                    id_a_entero = int(input("ID de la tarea a eliminar: "))
                    manager.delete_task(id_a_entero)

                case 5:
                    print("\nSaliendo...")
                    break

                case _: #Opción por defecto
                    print("\nOpción no válida. Selecciona otra.")

        except ValueError:
            print("Opción incorrecta, seleccione otra.")


#Inicio del programa
if __name__ == "__main__":
    main()

            