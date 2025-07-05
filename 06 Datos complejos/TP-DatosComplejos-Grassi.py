#Creacion de diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Se añaden frutas nuevas con sus precios
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
#Imprimir diccionario con nuevos keys y valores
print(precios_frutas)
#Modificar valores de keys
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
#Imprimir para ver modificaciones
print(precios_frutas)
#Crear lista utilizando solo las keys
lista_frutas=list(precios_frutas)
#Imprimir lista
print(lista_frutas)
print(type(lista_frutas))
#Programa para agendar nombre y numero telefonico
print("Creación de agenda telefonica")
dicc_tel={}
for i in range(1,6):
    nombre=input("Ingrese un nombre: ")
    tel=input("Ingrese el telefono: ")
    dicc_tel[nombre]=tel
#print(dicc_tel)
buscar=input("Que telefono quiere encontrar?: ")
print(f"El telefono de {buscar} es: {dicc_tel[buscar]}")
#Programa que solicita frase a usuario
frase = input("Escribe una frase: ")
#Separa las palabras
palabras = frase.split()
#Obtiene las palabras únicas
palabras_unicas = set(palabras)
#Contar palabras
cont_palabras = {}
for palabra in palabras:
    if palabra in cont_palabras:
        cont_palabras[palabra] += 1
    else:
        cont_palabras[palabra] = 1
#Imprime resultado
print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", cont_palabras)
#Diccionario para almacenar los datos
alumnos = {}
#Permite 3 alumnos 3 notas cada uno
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    notas = tuple(int(input(f"Ingresá la nota {j + 1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas
# Muestra el promedio de cada alumno
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
#Sets de numeros que representan estudiantes que aprobaron uno y otro parcial
parcial1 = {10001, 10002, 10003, 10004}
parcial2 = {10003, 10004, 10005, 10006}
#Aprobaron ambos parciales
ambos = parcial1 & parcial2
#Aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2
#Aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2
#Muestra resultados
print("Aprobó ambos parciales:", ambos)
print("Aprobó solo uno de los dos:", solo_uno)
print("Aprobó al menos un parcial:", al_menos_uno)
#Diccionario inicial de productos y su stock
stock_productos = {"manzanas": 6,"bananas": 4,"naranjas": 2}
while True:
    print("\n--- Menú ---")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Elegí una opción (1-4): ")
    if opcion == "1":
        producto = input("Ingresá el nombre del producto: ").lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades.")
        else:
            print(f"{producto} no está en el inventario.")
    elif opcion == "2":
        producto = input("Ingresá el nombre del producto: ").lower()
        if producto in stock_productos:
            try:
                cantidad = int(input(f"Ingresá cuántas unidades agregar a {producto}: "))
                stock_productos[producto] += cantidad
                print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
            except ValueError:
                print("Ingresá un número válido.")
        else:
            print(f"{producto} no existe. Usá la opción 3 para agregarlo.")
    elif opcion == "3":
        producto = input("Ingresá el nombre del nuevo producto: ").lower()
        if producto in stock_productos:
            print(f"{producto} ya existe en el inventario.")
        else:
            try:
                cantidad = int(input(f"Ingresá la cantidad inicial de {producto}: "))
                stock_productos[producto] = cantidad
                print(f"{producto} agregado con {cantidad} unidades.")
            except ValueError:
                print("Ingresá un número válido.")
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intentá de nuevo.")
#Agenda (dia, hora, evento)
agenda = {("lunes", "09:00"): "Reunión de equipo",("martes", "14:00"): "Clase de inglés",("viernes", "18:30"): "Gimnasio"}
while True:
    print("\n--- Agenda ---")
    print("1. Consultar evento")
    print("2. Agregar/modificar evento")
    print("3. Mostrar agenda completa")
    print("4. Salir")
    opcion = input("Elegí una opción (1-4): ")
    if opcion == "1":
        dia = input("Ingresá el día: ").lower()
        hora = input("Ingresá la hora (ej: 14:00): ")
        clave = (dia, hora)
        if clave in agenda:
            print(f"Evento agendado: {agenda[clave]}")
        else:
            print("No hay ningún evento agendado en ese horario.")
    elif opcion == "2":
        dia = input("Ingresá el día: ").lower()
        hora = input("Ingresá la hora (ej: 14:00): ")
        evento = input("Ingresá el evento: ")
        agenda[(dia, hora)] = evento
        print(f"Evento guardado: {evento} en {dia} a las {hora}.")
    elif opcion == "3":
        print("\nAgenda completa:")
        if not agenda:
            print("La agenda está vacía.")
        else:
            for clave in sorted(agenda):
                dia, hora = clave
                print(f"{dia.capitalize()} {hora} → {agenda[clave]}")
    elif opcion == "4":
        print("Saliendo de la agenda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
#Diccionario paises capitales
paises_a_capitales = {"Argentina": "Buenos Aires","Brasil": "Brasilia","Chile": "Santiago","Uruguay": "Montevideo"}
#Invierte el diccionario
capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}
# Muestra el nuevo diccionario
print("Diccionario invertido (capital/país):")
print(capitales_a_paises)