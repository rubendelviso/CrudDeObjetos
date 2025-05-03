# Desarrollar mediante código de programación la carga de datos de alumnos y que posea la siguiente estructura:

# Codigo_Alumno (numerico autoincremental)
# Apellido y Nombre (string)
# Telefono (string)
# Fecha de nacimiento (tipo Fecha)
# Para ello deberá utilizar un menú con las siguientes opciones:


# Crear nuevo alumno
# Modificar alumno
# Eliminar alumno
# Ver alumnos
# Buscar alumno por Codigo de Alumno
# Salir del programa
# Se deja como base la clase Fecha para que puedan reutilizarla, tener en cuenta que para crear
#  una nueva fecha deben pasarle al constructor un formato de fecha válido "dd/mm/AAAA" donde dd representa el día, mm el mes y AAAA el año:

class menu:

    def __init__(self):

    #esta parte solo muestra el menu
    

        self.menuDeOpciones = ["Opciones del menu:","1.Crear nuevo alumno","2.Modificar alumno", "3.Eliminar alumno","4.Ver alumnos","5.Buscar alumno por Codigo de Alumno", "6.Salir del programa"] 
    

    def mostrarmenu(self):
        
        for Eleccion in self.menuDeOpciones:
            print(Eleccion) 
            #time.sleep(1)

    def ObtenerLista (self):

        return self.menuDeOpciones
        #asi capturo a la lista para poder iterarla en el otro script


#menu = Menu()            #Este es el metodo que se usa para invocar al metodo de la clase 
#menu.mostrarmenu()       #Primero creo la instancia despues llamo a la instancia de ese objeto
        

        