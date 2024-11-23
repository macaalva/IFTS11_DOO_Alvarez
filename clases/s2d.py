#Esquema nombre	apellido edad mail


class str2Doc(object):
    def __init__(self, keyStr, separator=","):
        self.separator= separator
        self.keys= keyStr.split(separator)
    def convert (self, line):
        values= line.split(self.separator)
        if len(values) == len(self.keys):
            d= {}
            i=0 
            while i < len(values):
                key= self.keys[i]
                val= values[i]
                d[key]= val
                i= i+1
            return d 

s2d= str2Doc("nombre,email,telefono,edad")
print (s2d.keys)
d= s2d.convert("macarena,maca@gmail.com,13456789,29")
print (d)




"""es el corazon de todo, en que parte se implementa?? en la parte dos del main hay que implementar el csv
para eso tenemos que leer el archivo linea a linea, la primera linea es la mas importante porque me dice como se llaman los datos de la primera columna. transforma el listado del csv en diccionarios.
hace la definicion del esquema del diccionario (objeto mapa de keys values). dentro de la clase documento cuando creamos un documento pasamos id y contenido (el contenido es el diccionario) almacena con el id el diccionario, 
que va a ser su contenido. diccionario, que es? d= {} (inicializado en 0) se completa asi d["nombre"]= "Macarena" o creando e inicializando d={"nombre": "macarena, "edad": 29} 
"""
"""que tiene que suceder con string to doc??
linea0=  "nombre, apellido, edad, mail" #creo una clase, cuando la inicializo le digo como se va a llamar las keys"
print (linea.split(","))"""

