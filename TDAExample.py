# Implementacion de TDA
#Esta forma es mas formal, optar por esta
class producto:
    def __init__(self,nombre, precio):   #El primer parametro siempre sera self, Despues vemos que recibe otros dos parametros en este caso.
        self.nombre = nombre
        self.precio = precio


# Otra Implementacion en TDA

class productaso:

    pass  #Marca de posicion, al parecer este metodo evita errores asi como un agente de transito evita accidentes
          #Es como que le dice al programa "que no haga nada" por asi decirlo
    
    def crearProducto (nombre, precio):
        
        p = productaso()  #Esta variable sirve de marcador parecer para crear instancias

        p.nombre = nombre
        p.precio = precio
        return p
        
# crearProducto("aceite",9.5)   Esto es parte de la diapo pero tira error de sintaxis jaja   

