import datetime as dt

# def Telefonovalido():
#         #NOTA: La funcion replace como argumento (1ero: [Toma a lo que identificas para reemplazar] , [Toma al dato con el que lo vas a reemplazar])



#             Telefono = "11)   3231311 asdsad"
#             Telefono2 = 1122313
#             Telefono3 = "213131"

#              #Aplicar filtro a el telefono : *tratar de juntar todo en una cadena
#             Telefono = Telefono.replace(" ","").replace("-","").replace("(","").replace(")","") 
#             ver1 = Telefono.isdigit()
#             # ver2 = Telefono2.isdigit()
#             ver3 = Telefono3.isdigit()
#             print (Telefono)
#             print (ver1)
#             # print (ver2)
#             print (ver3)


# Telefonovalido()





"           Todos los metodos son para la funcion re match:"
# _El acento circunflejo sirve para (^) indicar donde inicia la oracion
# _El signo peso sirve para determinar $ donde termina la oracion
# _Para los corchetes para determinar un rango o elemento al que buscar dentro de ellos []
# _ \d indica un digito  y si lo combino con {6}indica que sea de 6 digitos \D sirve para buscar lo que no sea un entero osea un str
# _Con parentesis recortas lo quq queres buscar y mostrar por pantalla
# _ Si busco una cadena de texto de un tamaño determinado larga \s...s\   los puntos van a indicar cuantos caracteres
# _ ()+ y lo que ponga dentro del texto va a devolver las frases que tengan la cadena de texto que hayas metido dentro del parentesis
fecha  = dt
fechaminima = dt.MINYEAR

print(fechaminima)