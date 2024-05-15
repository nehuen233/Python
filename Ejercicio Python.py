#Crear una lista llamada meses y que alamacena el nombre de los doce meses del año.
#Mostrar por pantalla los doce nombres utilizando la función print().

def ejercicio():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


    for mes in meses:
        print(mes)
    
    
#A partir del siguiente array que se proporciona: var valores = [true, 5, false, "hola", "adios",2];
#Determinar cual de los dos elementos de texto es mayor
#Utilizando exclusivamente los dos valores booleanos del array, determinar los operadores
#necesarios para obtener un resultado true y otro resultado false
#Determinar el resultado de las cinco operaciones matemáticas realizadas con los dos
#elementos numéricos
def ejercicio2():
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
def ejercicio1p():
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
    

#Ejercicio 4
#Dado 1 número con decimales, que representa el lado de un cuadrado se pide informar la superficie del mismo.

def multiplicacion():
    Cuadrado = float(input("Ingrese un valor decimal"))
    dato = Cuadrado * 4
    
    print("El area del triangulo es:  ", dato)


#Ejercicio 5
#Se ingresa 3 números que representan horas, minutos y segundos. Se pide informar el resultado expresado en 
#segundos. Determinar qué tipo de valor es el aconsejable para los datos solicitados

def calcular_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Definir los valores de tiempo
def ejercicio5():
    horas = int(input("Ingrese un valor"))
    minutos = int(input("Ingrese un valor"))
    segundos = int(input("Ingrese un valor"))

# Calcular los segundos totales
    segundos_totales = calcular_segundos(horas, minutos, segundos)

# Mostrar el resultado
    print("El resultado expresado en segundos es:", segundos_totales)

#Ejercicio 6
#Se necesita calcular la superficie de un triángulo, y se dispone solamente de los valores de su base y altura.
#Definir también que tipo de valor es aconsejable para las variables con la información que se tiene.
#**No se podrá usar valores fijos en las fórmulas del algoritmo. Solo variables y/o constantes.**

def ejercicio6():
    base = int(input("Ingrese el valor de la base")) 
    altura = int(input("Ingrese el valor de la altura"))
    superficie = (base * altura)

    print("La superficie es:  ", superficie)



#Ejercicio7
#Dados 6 números reales, informar el promedio de los mismos.

def ejercicio7():
   N1 = float(input("el valor es: "))
   N2 = float(input("el valor es: "))
   N3 = float(input("el valor es: "))
   N4 = float(input("el valor es: ")) 
   N5 = float(input("el valor es: "))
   N6 = float(input("el valor es: "))

   resultado = (N1 + N2 + N3 + N4 + N5 + N6)/6
   print("el promedio es:  ", resultado)

#Ejercicio8
#Dados 2 números enteros, que representan una cantidad parcial y total se pide: Calcular e informar 
#el porcentaje que representa la primera de la segunda. ¿Qué tipo de datos son los recomendados para este algoritmo?

def ejercicio8():
    n1 = int(input("Ingrese un valor numerico"))
    n2 = int(input("Ingrese un valor numerico"))
    resultado = (n1 * n2)/100

    print("El promedio es:  ", resultado)

#Ejercicio9
#Dada una fecha que se lee en formato numérico DDMMAAAA (dos números para el día, dos para el mes, cuatropara el año),
#se solicita obtener el día el mes y año por separado en tres variables. (usar descomposición matemática)

def ejercicio9():
    # Leemos la fecha en formato numérico DDMMAAAA
    fecha_numerica = int(input("Ingrese la fecha en formato numérico DDMMAAAA: "))

    # Descomponemos la fecha en día, mes y año
    anio = fecha_numerica % 10000  # Obtenemos los últimos cuatro dígitos para el año
    mes_dia = fecha_numerica // 10000  # Obtenemos los primeros seis dígitos para el mes y día
    mes = mes_dia // 100  # Obtenemos los dos primeros dígitos para el mes
    dia = mes_dia % 100  # Obtenemos los dos últimos dígitos para el día

    # Mostramos los resultados
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)

#ejercicio10
#En un curso de ciencias de la computación la calificación final del estudiante se determina a partir del
#rendimiento en tres aspectos del trabajo. A) Existe una calificación por los exámenes parciales que representa el
#30% del valor total de la nota final. B) la calificación por los trabajos prácticos corresponde al 20% del valor de la
#nota final. C) el examen integrador que corresponde al 50% restante. (los valores de las notas pueden ir de 0 a 10)

def ejercicio10()
    
