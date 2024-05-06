#Crear una lista llamada meses y que alamacena el nombre de los doce meses del año.
#Mostrar por pantalla los doce nombres utilizando la función print().


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


for mes in meses:
    print(mes)
    
    
#A partir del siguiente array que se proporciona: var valores = [true, 5, false, "hola", "adios",2];
#Determinar cual de los dos elementos de texto es mayor
#Utilizando exclusivamente los dos valores booleanos del array, determinar los operadores
#necesarios para obtener un resultado true y otro resultado false
#Determinar el resultado de las cinco operaciones matemáticas realizadas con los dos
#elementos numéricos

valor = [True, 5, False, "hola", "adios", 2]

if len(valor[3]) < len(valor[4]):
    print("adios es mas grande que hola")
    print(valor[0])
    
else:
    print("hola es más chico que adios")
    print(valor[2])
 
print(valor[1]+valor[5])
print(valor[1]-valor[5])
print(valor[1]*valor[5])
print(valor[1]/valor[5])
    