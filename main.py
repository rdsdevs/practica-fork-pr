import json
import os

def cargar_diccionario(archivo='diccionario.json'):
    """Carga los términos desde el archivo JSON."""
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"Error al leer el archivo {archivo}.")
        return []

def mostrar_terminos(diccionario):
    """Muestra los términos cargados en un formato legible."""
    if not diccionario:
        print("El diccionario está vacío.")
        return

    print("\n--- El Diccionario Comunitario de Python ---\n")
    for item in diccionario:
        termino = item.get('termino', 'N/A')
        definicion = item.get('definicion', 'Sin definición')
        autor = item.get('autor', 'Desconocido')
        
        print(f"📖 Término: {termino}")
        print(f"📝 Definición: {definicion}")
        print(f"✍️ Contribuido por: {autor}")
        print("-" * 40)
    print(f"\nTotal de términos: {len(diccionario)}")

def main():
    diccionario = cargar_diccionario()
    mostrar_terminos(diccionario)

if __name__ == "__main__":
    main()
