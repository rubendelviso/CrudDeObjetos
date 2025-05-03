from Utils import Opcion, GestionDeAlumnos
import time
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
        time.sleep(3)
        Opcionelegida = alumno.ValidarOpcion()
        Opcionelegida = int(Opcionelegida)  #lo casteo pq estoy desempaquetando un string anteriormente
        time.sleep(3)     


         
         

main()