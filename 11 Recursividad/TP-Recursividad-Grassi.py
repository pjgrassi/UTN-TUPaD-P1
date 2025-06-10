#Funciones recursivas
#1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

#2
#funcion fibonacci
def fibonacci_rec(pos):
    if pos==0:
        return 0
    elif pos==1:
        return 1
    else:
        return fibonacci_rec(pos-1)+fibonacci_rec(pos-2)
#funcion para mostrar la serie y sus resultados
def mostrar_serie_fibonacci(pos):
    print("Serie de Fibonacci hasta la posición", pos, ":")
    for i in range(pos + 1):
        print(fibonacci_rec(i), end=" ")

#3
def potencia(num1,num2):
    if num2==0:
        return 1
    else:
        return num1*potencia(num1,num2-1)

#3
def decimal_a_bin(num):
    if num==0:
        return 0
    res=num%2 #obtengo el valor del residuo 0 o 1
    cos=num//2 #obtengo el valor entero de la division 
    if cos==0:
        return str(res) #si el cos es 0 retorna el residuo pasado a string
    else:
        return decimal_a_bin(cos)+str(res)


#Programa Principal
#1
num=int(input("Ingrese un numero entero: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}") #recorre los numeros y arroja su factorial

#2
pos=int(input("Escriba un numero entero: "))
print(mostrar_serie_fibonacci(pos))

#3
num1=int(input("Ingrese un numero entero como base: "))
num2=int(input("INgrese un numero entero como exponente: "))
print(potencia(num1,num2))

#4
num=int(input("Ingresa un numero entero positivo para pasar a binario: "))
print(decimal_a_bin(num))