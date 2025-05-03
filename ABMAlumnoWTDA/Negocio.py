"PARA RECORDAR"

# self es obligatorio como primer parámetro en los métodos dentro de clases (excepto los métodos @staticmethod).

# Usás self para guardar datos en el objeto y acceder a ellos después.

# Cada objeto que creás tiene su propia copia de esos datos.

# funcion .isnumeric() devuelve un booleano verificando una variable cualesquiera
# es decir si quiero verificar num = 9, num.isnumeric() devolvera True

#Osea la secuencia si quiero guardar un alumno nuevo: Tengo dos clases, una de ellas
#va a tener el constructor para crear el objeto(alumno), la otra (gestor de alumnos)
#donde tengo toda mi logica inicializa una lista en donde guardo a mis alumnos
#y en esa misma clase Creo una funcion que llama a la instancia Alumno para guardar mi objeto
#nuevo osea un alumno nuevo

#El metodo string se utiliza para despues poder invocar los atributos del objeto facilmente. Es decir si quisiera imprimir por pantalla los atributos de un objeto "x"
#lo podria hacer facilmente gracias al metodo __string__

"           Ejemplo de funcion Re"
# import re

# texto = "Hola mundo"
# resultado = re.match(r"Hola", texto)

# if resultado:
#     print("¡Coincidencia encontrada!")
# else:
#     print("No hay coincidencia.")
#si no hay coincidencia con lo que encuentra devuelve None

from Menu import menu
import Utils
import uuid
import re
import datetime 
import time


class Fecha:
    #Tengo que validar que la fecha de nacimiento sea valida
    #Herramientas que puedo usar regex para el formato de la fecha, ademas del formato si la fecha existe o no y Datetime para corroborar si la fecha es hoy
    "Esto significa que La clase espera que le pase el parametro str pero si no va a tomar el valor None por defecto"
    "en el otro scope va a tener sentido"
    def __init__(self,fechaStr: str = None):
        if fechaStr == None:
            hoy= datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year

        
        while True:
            if self.ValidarFecha(fechaStr):
                break
            else:
                fechaStr = (input("Vuelva a ingresar la fecha, la ha ingresado mal recuerde que debe ser con el formato dd/mmm/aaaa: "))


        self.fechaStr = self.FechaFormateada(fechaStr) 

    def FechaFormateada (self,fecha):
        #Lo hice para chequear pero voy a retornar la fecha en el formato normal

        Separacion= fecha.split("/")
        
        
        self.dia = Separacion[0]
        self.mes = Separacion[1]
        self.anio = Separacion[2]                

        return self.dia , self.mes , self.anio
    def ValidarFecha (self, fechastr:int):
        "En la funcion rematch vamos a meter como primer parametro a el patron que vamos a buscar"
        "Y como segundo parametro a en donde vamos a buscar. En el caso que haya coincidencia va a devolver un objeto"
        "Si no hay coincidencia va a devolver None"

        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

        return re.match(patron,fechastr)
    
    def __str__(self):
    
        return f"{self.dia}/{self.mes}/{self.anio}"
    



class Opcion:


    


    def ValidarOpcion (self):


        menuInstancia = menu()
        menuInstancia.mostrarmenu()
        ListadeOpciones = menuInstancia.ObtenerLista() #capturando a la lista del otro script 
        opcion = (input("ingrese por favor un numero"))

        while opcion.isnumeric()!=False or opcion not in range(1,len(ListadeOpciones)):
            if  opcion.isnumeric() == True and\
                  int(opcion) in range(1,len(ListadeOpciones)):
                
                    print("Selecciono Validamente la opcion")
                    return opcion
                    

            else:
                 print("Opcion invalida, Ingrese una con las opciones que ve en pantalla")
                 
                 return self.ValidarOpcion()


class Alumno:
     AcumuladorID = 1
     
     def __init__(self,Codigo,Nombre,Telefono,FechaDeNacimiento): 

        self.Codigo = Alumno.AcumuladorID    #Este acumulador que se inicializa cada vez que llamamos al constructor de la clase
        Alumno.AcumuladorID+=1                      #crea ese ID unico 

        self.Nombre = Nombre 
        self.Telefono = Telefono
        self.FechaDeNacimiento = FechaDeNacimiento

        

     def __str__(self):
         return f"\nAlumno:{self.Codigo}\nNombre: {self.Nombre}\nN°De tel:{self.Telefono}\nFecha De Nacimiento:{self.FechaDeNacimiento}"
        
        
class GestionDeAlumnos:
     
     def __init__(self):
          #self.alumnos = []  #Creo una lista de alumnos que voy a usar para guardar mis alumnos(objetos)
          "Lista hardcodeada, excelente para pruebas"
          self.alumnos = [
                Alumno(1, "Ruben Gómez", "1134567890", "14/04/2003"),
                Alumno(2, "Lucía Pérez", "1145678901", "22/08/2002"),
                Alumno(3, "Martín López", "1156789012", "05/12/2001"),
                Alumno(4, "Carla Ramírez", "1167890123", "30/01/2000"),
                Alumno(5, "Tomás Fernández", "1178901234", "17/06/2004"),
            ]
     
     def __str__(self):
         return self.alumnos    
     def IngresoAlumno(self):
        # Codigo = input("Ingrese el codigo del alumno")
          Nombre = input("Ingrese el nombre del alumno por favor")
          Telefono = input("Ingrese el telefono del alumno por favor")
          FechaDeNacimiento= input("Ingrese la fecha de nacimiento del alumno por favor")

          Telefono = self.Telefonovalido(Telefono)

          FechaStr= Fecha(FechaDeNacimiento)

        #   print(type(FechaStr)) 
          
        #   print(FechaStr)
          
          

          

        #   AlumnoBuscado  = self.filtroCodigo(Codigo)
          
          "Estaba tratando de crear ID's unicos debajo de este scope, cuando es mejor el incremento a causa de crear un alumno nuevo"
        #   if not AlumnoBuscado\
        #     and AlumnoBuscado != None:
        #        print("Ya existe un alumno ingresado con este codigo, por favor vuelva a registrarse con otro codigo")
        #        self.IngresoAlumno()

                #objetivo: Hay que crear una instancia de la clase Alumno para despues poder guardar todos los atributos del nuevo alumno(objeto)
                #dentro de la lista alumnos

          
          AlumnoNuevo = Alumno(len(self.alumnos),Nombre,Telefono,FechaDeNacimiento) #PARA EL ID no me hace falta agregarle el +1, el acumulador esta dentro de la clase alumno ya

          self.alumnos.append(AlumnoNuevo)
     

     def Telefonovalido(self,Telefono):
        #NOTA: La funcion replace como argumento (1ero: [Toma a lo que identificas para reemplazar] , [Toma al dato con el que lo vas a reemplazar])

        if Telefono:
                

             #Aplicar filtro a el telefono : *tratar de juntar todo en una cadena
            Telefono = Telefono.replace(" ","").replace("-","").replace("(","").replace(")","")

             #Aplicar filtro para ver si contiene txt
            while not Telefono.isdigit():
                Telefono = input("el numero que ingreso contiene caracteres no validos por favor ingreselo nuevamente:") 
                
                return self.Telefonovalido(Telefono)
            else: return Telefono
            
     def ModificarAlumno(self):
         print(self.alumnos)
         CodigoAlumno = int(input("ingrese el codigo del alumno que quiere modificar"))

         atrAlumno = self.AlumnoCodigo(CodigoAlumno)
         print(f"Alumno encontrado{atrAlumno}")  
         #Empaqueto a el dato que se quiere modificar y a el alumno
         self.datoModificar(int(input("Ingrese el dato que quiere modificar:\n1_ Nombre \n2_ Telefono\n3_ Fecha de nacimiento")),atrAlumno)
         
     def datoModificar(self,dato:int,alumno):
        #Modificar el dato a str para poder hacer el cambio
        datoModificado = input("ingrese el nuevo dato")
        if dato==1:
            "modificandoNombre"
            
            alumno.Nombre  = datoModificado
            print(f"Dato modificado exitosamente\n{alumno}")     
        elif dato==2:
            "modificandotTel"
            datoModificado = self.Telefonovalido(datoModificado)   #Validando Numero de telefono
            alumno.Telefono  = datoModificado
            
            print(f"Dato modificado exitosamente\n{alumno}")
        elif dato==3:
            "modificandoFechaDeNacimiento"
            datoModificado = Fecha(datoModificado) #Validando Fecha
            print("hasta aca")
            alumno.FechaDeNacimiento = datoModificado
            print(f"Dato modificado exitosamente\n{alumno}")            
     def AlumnoCodigo(self,Codigoo):
         for alumno in self.alumnos:
             if alumno.Codigo == Codigoo:
                 return alumno
             
     def EliminarAlumno(self):
         AlumnoAEliminar= int(input("ingrese el numero del alumno que quiere eliminar")) 
         Eliminar = self.AlumnoCodigo(AlumnoAEliminar)
         print(f"alumno a eliminar{Eliminar}")
         
         self.alumnos.remove(Eliminar)
         print("Cambios efectuados,Mostrados a continuacion")
         self.mostrarAlumnos()

     def mostrarAlumnos(self):
         for i in range(0,len(self.alumnos)):
             print(self.alumnos[i])
          



def main():


    alumno  = Opcion()
    Opcionelegida = float('inf')
    
    gestionarAlumno = GestionDeAlumnos()
    
    while Opcionelegida !=6:  
        if Opcionelegida == 1:
            gestionarAlumno.IngresoAlumno()     
        elif Opcionelegida == 2:
            gestionarAlumno.ModificarAlumno()
        elif Opcionelegida ==3:
            gestionarAlumno.EliminarAlumno()
        elif Opcionelegida==4:
            gestionarAlumno.mostrarAlumnos()
        Opcionelegida = alumno.ValidarOpcion()
        Opcionelegida = int(Opcionelegida)     #lo casteo pq estoy desempaquetando un string anteriormente


         
         

main()