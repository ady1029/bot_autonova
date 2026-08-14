import json
import os

def agregar_trabajo(message):
    try:
        lineas = [l.split(". ", 1)[-1].strip() for l in message.text.strip().split('\n')]            
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
                    # AQUÍ ESTÁ EL TRUCO:
                    if isinstance(contenido, list):
                        datos = contenido
                    else:
                        # Si era un diccionario, lo metemos dentro de una lista nueva
                        datos = [contenido]
                except json.JSONDecodeError:
                    datos = []
        
        datos.append(trabajo)
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True    
    except Exception as e:
        print(f"Error al escribir: {e}")
        return False
