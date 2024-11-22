# main.py
from clases.db import BaseDeDatos


def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    db = BaseDeDatos("MiBaseDeDatos")

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.crear_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada.")
        
        elif opcion == "2":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            collection = db.obtener_coleccion(nombre_coleccion)
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            collection.import_csv(nombre_coleccion, ruta_csv)
        
        elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = input("Ingrese el ID del documento: ") #### aclarar que se un int sino no arroja resultados
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                documento = coleccion.buscar_documento(doc_id)
                if documento:
                    print("Documento encontrado:")
                    print(documento)
                else:
                    print("Documento no encontrado.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = input("Ingrese el ID del documento a eliminar: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                coleccion.eliminar_documento(doc_id)
        
        elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                documentos = coleccion.list_documents()
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-----------")
                else:
                    print("No hay documentos en la colección.")
        
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()