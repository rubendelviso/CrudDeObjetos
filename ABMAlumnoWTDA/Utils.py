
# Desarrollar mediante código de programación la carga de datos de alumnos y que posea la siguiente estructura:

# Codigo_Alumno (numerico autoincremental)
# Apellido y Nombre (string)
# Telefono (string)
# Fecha de nacimiento (tipo Fecha)
# Para ello deberá utilizar un menú con las siguientes opciones:
class Alumno:
    

    def __init__ (self,CodigoAlumno,ApellidoNombre, Telefono, FechaDeNacimiento):
        self.CodigoAlumno = CodigoAlumno
        self.ApellidoNombre=  ApellidoNombre
        self.Telefono = Telefono
        self.FechaDeNacimiento = FechaDeNacimiento

         
    

alumnoRandom  = Alumno(123, "DelViso", 1109, 14.06)

print(alumnoRandom)