class Documento (object): 

    def __init__(self, id, contenido=None):
        self.id= id
        self.contenido= contenido if contenido is not None else {}

    def obtener_valor (self, clave):
        return self.contenido.get(clave, False)
    
    def modificar_valor (self,clave, valor):
        self.contenido[clave]= valor

    def __str__ (self):
        return f"Documento(id={self.id}, contenido={self.contenido})"
""" 
d= Documento (1, {'nombre': "Macarena"})
if not d.obtener_valor('direccion'):
    d.modificar_valor ('direccion', 'calle falsa 123')
print(d.obtener_valor ('direccion'))
print(d.obtener_valor ('nombre')) """

class Coleccion (object):
    def __init__ (self, nombre):
        self.nombre= nombre
        self.documentos = {} #guarda los documentos que va creando, es un diccionario vacio, accede a cada diccionario por su ID

    def añadir_documento (self,documento):
        self.documentos[documento.id]= documento
    
    def eliminar_documento (self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento] #palabra reservada que elimina una key con su valor 
    
    def buscar_documento (self, id_documento):
        return self.documentos.get(id_documento, None)
    

    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos."

c= Coleccion ('Personas')
p1= Documento(1, {'Nombre': 'Jose' , 'Apellido': 'Perez', 'Edad': 18, 'Email': 'joseperez@gmail.com', 'Telefono': 1568676768}) 
p2= Documento(2, {'Nombre': 'Juana', 'Apellido': 'Perez', 'Edad': 18, 'Email': 'juanaperez@gmail.com', 'Telefono': 1568676769}) 
c.añadir_documento(p1)
c.añadir_documento(p2)
personas= c.buscar_documento(2)
print (personas.obtener_valor('Nombre'), personas.obtener_valor('Email'))
c.eliminar_documento(2)
personas= c.buscar_documento(2)
if personas is not None:
    print (personas.obtener_valor('Nombre'), personas.obtener_valor('Email'))
else:
    print ("la persona no existe mas") 

class BaseDeDatos:
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
    
