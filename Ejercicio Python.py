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

#Ejercicio 1
#Leer 2 números enteros, calcular la suma e informar el resultado.

N1 = int(input("Ingrese un numero"))
N2 = int(input("Ingrese un numero"))
resultado = int(input(N1 + N2))    

if N1 + N2:
     print("el resultado es  "+ resultado)
     
#Ejercicio 2    
#Leer 4 números enteros, calcular la suma e informar el resultado.
n1 = int(input("Ingrese un valor"))
n2 = int(input("Ingrese un valor"))
n3 = int(input("Ingrese un valor"))
n4 = int(input("Ingrese un valor"))
result = int(input(n1 + n2 + n3 + n4))

if n1 + n2 + n3 + n4:
    print("El resultado es   "+ result)
    
#Ejercicio 3
#Dados 2 números enteros, que representan los lados de un rectángulo se pide informar la superficie del mismo.

def multiplicacion ():
    Valor1 = int(input("Ingrese el valor de la superficie"))
    valor2 = int(input("Ingrese el valor de la superficie"))
    Solucion = (Valor1 * valor2)
    
    print("La altura es   ", Solucion)
    
multiplicacion()

#Ejercicio 4
#Dado 1 número con decimales, que representa el lado de un cuadrado se pide informar la superficie del mismo.

def multiplicacion():
    triangulo = float(input("Ingrese un valor decimal"))
    dato = triangulo * 4
    
    print("El area del triangulo es:  ", dato)
    
multiplicacion()

#Ejercicio 5
#Se ingresa 3 números que representan horas, minutos y segundos. Se pide informar el resultado expresado en 
#segundos. Determinar qué tipo de valor es el aconsejable para los datos solicitados

def calcular_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Definir los valores de tiempo
horas = 12
minutos = 55
segundos = 6

# Calcular los segundos totales
segundos_totales = calcular_segundos(horas, minutos, segundos)

# Mostrar el resultado
print("El resultado expresado en segundos es:", segundos_totales)
