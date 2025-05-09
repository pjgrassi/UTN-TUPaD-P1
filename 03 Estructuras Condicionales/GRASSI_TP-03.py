#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad=int(input("Ingrese su edad: "))
if edad>=18:
    print("Usted es mayor de edad.")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”
nota=int(input("Ingrese su nota: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". 
numero=int(input("Ingrese un numero par: "))
if numero%2==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad=int(input("Ingrese su edad: "))
if edad<12:
    print("Eres Niño/a")
elif edad>=12 and edad<18:
    print("Eres Adolecente")
elif edad>=18 and edad<30:
    print("Eres Adulto/a joven")
else:
    print("Eres Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
password=input("Ingrese una contraseña de entre 8 a 14 caracteres: ")
if len(password)>=8 and len(password)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado 
# por pantalla.
import random
from statistics import mode, median, mean
numero_aleatorios=[random.randint(1,100) for i in range(50)]
media=mean(numero_aleatorios)
moda=mode(numero_aleatorios)
mediana=median(numero_aleatorios)
if media>mediana and mediana>moda:
    print("La lista de numeros aleatorios tiene sesgo positivo")
elif media<mediana and mediana<moda:
    print("La lista de numeros aleatorios tiene sesgo negativo")
else: 
    print("La lista de numeros aleatorios no tiene sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
palabra=input("Ingrese una palabra: ")
if palabra[-1]=="a" or palabra[-1]=="e" or palabra[-1]=="i" or palabra[-1]=="o" or palabra[-1]=="u":
    print(f"{palabra}!")
else:
    print(f"{palabra}")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre=input("Ingrese su nombre: ")
opcion=int(input("Elija una de las siguientes opciones: \n 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.: "))
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
else:
    print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud=int(input("Escriba la magnitud del terremoto: "))
if magnitud<3:
    print("Muy leve (imperceptible)")
elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible)")
elif magnitud>=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud>=6 and magnitud<7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
from datetime import date
hemisferio=str(input("Ingrese en que hemisferio se encuentra N o S: "))
mes=int(input("Ingrese el numero del mes actual: "))
dia=int(input("Ingrese el numero de dia actual: "))
fecha=date(2025,mes,dia)
if fecha>=date(2024,12,21) and fecha<=date(2025,3,20) and (hemisferio=="N" or hemisferio=="n"):
    print("Estas en Verano")
elif fecha>=date(2024,12,21) and fecha<=date(2025,3,20) and (hemisferio=="S" or hemisferio=="s"):
    print("Estas en Invierno")
elif fecha>=date(2024,3,21) and fecha<=date(2025,6,20) and (hemisferio=="N" or hemisferio=="n"):
    print("Estas en Primavera")
elif fecha>=date(2024,3,21) and fecha<=date(2025,6,20) and (hemisferio=="S" or hemisferio=="s"):
    print("Estas en Otoño")
elif fecha>=date(2024,6,21) and fecha<=date(2025,9,20) and (hemisferio=="N" or hemisferio=="n"):
    print("Estas en Verano")
elif fecha>=date(2024,6,21) and fecha<=date(2025,9,20) and (hemisferio=="S" or hemisferio=="s"):
    print("Estas en Invierno")
elif fecha>=date(2024,9,21) and fecha<=date(2025,12,20) and (hemisferio=="N" or hemisferio=="n"):
    print("Estas en Otoño")
elif fecha>=date(2024,9,21) and fecha<=date(2025,12,20) and (hemisferio=="S" or hemisferio=="s"):
    print("Estas en Primavera")
else:
    print("Ha introducido algun dato no valido.")










