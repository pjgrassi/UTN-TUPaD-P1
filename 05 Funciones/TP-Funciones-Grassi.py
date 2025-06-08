#Definición de Funciones
#1
def imprimir_hola_mundo():
    return print("Hola Mundo")
#2
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")
#3
def informacion_personal(nombre, apellido,edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#4
def calcular_area_circulo(radio):
    return print("El area del circulo es: ",(3.14*(radio**2)))
def calcular_perimetro_circulo(radio):
    return print("El perimetro del circulo es: ",(3.14*(2*radio)))
#5
def segundos_a_horas(segundos):
    return print("Los segundos ingresados corresponden a: ",((segundos/60)/60)," horas")
#6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero,"X",i," = ",(i*numero))
#7
def operaciones_basicas(a, b):
    print(a,"+",b,"=",(a+b))
    print(a,"-",b,"=",(a-b))
    print(a,"x",b,"=",(a*b))
    print(a,":",b,"=",(a/b))
#8
def calcular_imc(peso, altura):
    return print("Tu IMC es: ",(peso/(altura**2)))
#9
def celsius_a_fahrenheit(celsius):
    return print("Los",celsius,"grados Celsius, son: ",((celsius*(9/5))+32),"grados Fahrenheit")
#10
def calcular_promedio(a, b, c):
    return print("El promedio de los valores ingresados es: ",((a+b+c)/3))

#Programa principal
1
imprimir_hola_mundo()
#2
nombre=input("Escribe tu nombre: ")
saludar_usuario(nombre)
#3
nombre=input("Escribe tu nombre: ")
apellido=input("Escribe tu apellido: ")
edad=input("Escribe tu edad: ")
residencia=input("Escribe tu pais de rersidencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#4
radio=float(input("Ingresa el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
#5
segundos=float(input("Ingresa los segundos: "))
segundos_a_horas(segundos)
#6
numero=int(input("Ingresa un numero entero para mostrar su tabla de multiplicación: "))
tabla_multiplicar(numero)
#7
a=int(input("Ingresa el primer numero entero: "))
b=int(input("Ingresa el segundo numero entero: "))
operaciones_basicas(a,b)
#8
altura=float(input("Ingresa tu altura(mts): "))
peso=float(input("Ingresa tu peso(kg): "))
calcular_imc(peso, altura)
#9
celsius=float(input("Ingresa una valor de grados Celsius: "))
celsius_a_fahrenheit(celsius)
#10
a=float(input("Ingresa el primer numero: "))
b=float(input("Ingresa el segundo numero: "))
c=float(input("Ingresa el tercer numero: "))
calcular_promedio(a,b,c)




