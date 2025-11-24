class Usuario:
    def __init__ (self,nombre,clave):
        self.nombre = nombre
        self.__clave = clave


    def muestra_datos(self):
            print(self.nombre)
            print(self.__clave)
usuario1 = Usuario("admin","root1234")
#usuario1.muestra_datos()
#print(usuario1.__clave)  

