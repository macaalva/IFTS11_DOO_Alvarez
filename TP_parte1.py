class Documento: 

    def __init__(self, id, contenido=None):
        self.id= id
        self.contenido= contenido if contenido is not None else {}

    def obtener_valor (self, clave):
        return self.contenido.get(clave, False)
    
    def modificar_valor (self,clave, valor):
        self.contenido[clave]= valor

    def __str__ (self):
        return f"Documento(id={self.id}, contenido={self.contenido})"

d= Documento (1, {'nombre': "Macarena"})
if not d.obtener_valor('direccion'):
    d.modificar_valor ('direccion', 'calle falsa 123')
print(d.obtener_valor ('direccion'))
print(d.obtener_valor ('nombre'))

class Coleccion:
    def __init__ (self, nombre):
        self.nombre= nombre
        self.documentos = {} #guarda los documentos que va creando, es un diccionario vacio, accede a cada diccionario por su ID

    def añadir_documentos (self,documento):
        self.documentos[documento.id]= documento
    
    def eliminar_documento (self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def buscar_documento (self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos."

c= Coleccion ('Libros')
l1= Documento(1, {'Titulo': 'Cien anios de soledad', 'Autor': 'Gabriel Garcia Marquez'})
l2= Documento(2, {'Titulo': 'El Psicoanalista', 'Autor': 'John Katzenbach'})
c.añadir_documentos(l1)
c.añadir_documentos(l2)
libro= c.buscar_documento(1)
print (libro.obtener_valor('Autor'), libro.obtener_valor('Titulo'))

class BaseDeDatosDocumental:
    def __init__ (self):
        self.colecciones= {}

    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion (nombre_coleccion)

    def eliminar_coleccion (self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
        
    def obtener_coleccion (self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__ (self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones."
    
