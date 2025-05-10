#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(1,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num = int(input("Ingrese un número entero: "))
cant_dig = len(str(abs(num)))
print("El número",num,"tiene",cant_dig,"dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
num1=int(input("Ingrese un numero entero: "))
num2=int(input("Ingrese otro numero entero: "))
if num1>num2:
    valor_ini=num2+1
    valor_fin=num1
else:
    valor_ini=num1+1
    valor_fin=num2
suma=0
for num in range(valor_ini,valor_fin):
    suma+=num
print("La suma de los numero comprendidos entre",(valor_ini-1),"y",valor_fin,"excluyendo los mismos es: ",suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
corte=0
suma=0
num=int(input("Ingrese un numero entero (para detener usar 0): "))
while num!=corte:
    suma+=num
    num=int(input("Ingrese un nuevo numero entero (para detener usar 0): "))
print("La suma acumulada de los numero ingresados es:",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
cont=1
num_rand=random.randint(0,9)
num_user=int(input("Adivine el numero entre 0 y 9: "))
while num_user!=num_rand:
    cont+=1
    num_user=int(input("Incorrecto!! elija un nuevo numero: "))
print("Excelente el numero misterioso era el",num_rand,"y necesito de",cont,"intento/s.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range(100,-1,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
suma=0
num_user=int(input("Ingrese un numero entero positivo: "))
if num_user<0:
    num_user=int(input("Ingresó un numero negativo, por favor ingrese un numero positivo: "))
for num in range(0,num_user+1):
    suma+=num
print("La suma de los numero en el rango desde 0 hasta",num_user,"es:",suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont=1
cont_par=0
cont_impar=0
cont_pos=0
cont_neg=0
for cont in range(100):
    print("Ingrese el",(cont+1),"° numero entero: ")
    num=int(input())
    if num%2==0:
        cont_par+=1
    elif num%2!=0:
        cont_impar+=1
    if num>0:
        cont_pos+=1
    elif num<0:
        cont_neg+=1
print("Usted ingreso",cont_par,"numeros pares,",cont_impar,"numeros impares,",cont_pos,"numeros positivos, y",cont_neg,"numeros negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
cont=1
suma=0
for cont in range(100):
    print("Ingrese el",(cont+1),"° numero entero: ")
    num=int(input())
    suma+=num
media=suma/100
print("La media de la suma de los numero ingresados es: ",media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num_inv = 0
num=int(input("Ingrese un numero entero: "))
num_orig=num
while num > 0:
        digito = num % 10
        num_inv = (num_inv * 10) + digito
        num //= 10
print("El numero",num_orig,"invertido es:",num_inv)    




