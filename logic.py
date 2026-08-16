import json
import os
import comuication
def agregar_trabajo(message):
    try:
        lineas = [l.split(". ", 1)[-1].strip() for l in message.text.strip().split('\n')]    
        if len(lineas) != 5:
               comuication.manejar_resultado(None,message)
               return    
        trabajo = {
                    "cliente": lineas[0],
                    "direccion": lineas[1],
                    "fecha": lineas[2],
                    "contacto": lineas[3],
                    "encargados": [e.strip() for e in lineas[4].split(",")]
                }       
        archivo = "trabajos.json"
        datos = []
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                try:
                    contenido = json.load(f)
                    if isinstance(contenido, list):
                        datos = contenido
                    else:
                        datos = [contenido]
                except json.JSONDecodeError:
                    datos = []
        
        datos.append(trabajo)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        comuication.manejar_resultado(True,message)  
    except Exception as e:
        print(f"Error al escribir: {e}")
        comuication.manejar_resultado(False, message)

def agregar_tarea(message):
    try:
        print("entre x2")
        lineas = [l.split(". ", 1)[-1].strip() for l in message.text.strip().split('\n')]    
        if len(lineas) != 4:
                    comuication.manejar_resultado(None,message)
                    return        
        tarea = {
                    "titulo": lineas[0],
                    "descripcion": lineas[1],
                    "responsable": lineas[2],
                    "estado": lineas[3],
                }       
        archivo = "tareas.json"
        datos = []
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                try:
                    contenido = json.load(f)
                    if isinstance(contenido, list):
                        datos = contenido
                    else:
                        datos = [contenido]
                except json.JSONDecodeError:
                    datos = []
        
        datos.append(tarea)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        comuication.manejar_resultado(True,message)   
    except Exception as e:
        comuication.manejar_resultado(False,message)

def obtener_tareas_por_usuario(user_id):
    with open('tareas.json', 'r', encoding='utf-8') as f:
        tareas = json.load(f)
    with open('usuarios.json', 'r', encoding='utf-8') as f:
        usuarios = json.load(f)
    usuario_info = next((u for u in usuarios if u['telegram_id'] == user_id), None)
    if not usuario_info:
        return None
    tareas_pendientes = [
        t for t in tareas 
        if t['responsable'] == usuario_info['nombre'] and t['estado'] == 'incompleto'
    ]
    
    return tareas_pendientes

def es_usuario_autorizado(user_id):
    try:
        with open('usuarios.json', 'r') as f:
            data = json.load(f)
            return any(u.get("telegram_id") == user_id for u in data)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

