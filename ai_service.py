import os
from dotenv import load_dotenv
from openai import OpenAI
#from google import genai

#cargamos las variables de entorno del proyecto
load_dotenv()

#acceso a la api de Gemini a través de OpenAI
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


#Función que desglosa una tarea compleja en varias simples
def create_simple_tasks(description):
    
    if not client.api_key:
        return ["Error: La API KEY de GEMINI no está configurada."]
    
    try:
        prompt = f'''Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
Tarea: {description}

Formato de respuesta:
- Subtarea 1
- Subtarea 2
- subtarea 3
- etc.
        
Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guión.'''

        params = {
            "model":"gemini-3-flash-preview",
            "reasoning_effort": "low",
            "messages" : [
                {"role":"system","content":"Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role":"user","content": prompt}
            ],
            #"max_completion_tokens":300
        }
        
        response = client.chat.completions.create(**params)
        print(response, "\n")
        content = response.choices[0].message.content.strip() #.strip() elimina los espacios en blanco delante y detrás
        print(content)
        subtasks = []
        
        for line in content.split("\n"):
            line = line.strip()

            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se ha podido generar las subtareas."]


    except Exception as e: #Con este formato se pueden ver el tipo de error que da cualquiera de los commandos
        #ejecutados en try
        import traceback
        print(f"ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        return [f"Error: {str(e)}"]