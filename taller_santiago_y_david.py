# -*- coding: utf-8 -*-
"""taller-santiago-y-david.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/storres195/7d2a009f8a45405e3af8fb306d8c2596/taller-santiago-y-david.ipynb

Profe este trabajo lo realice con mi compañero David Dominguez, ya que como te comentaba en clase él no tiene pc y aqui en la Biblioteca de la U ya tenian todos prestados
"""

base = int(input("Ingrese el tamaño de la altura: "))
altura = int(input("ingrese el tamaño de la base:"))

resultado = (base*altura)/2

print("El resultado es: ")
print(resultado)

print("Programa para convertir entre grados Celsius y Fahrenheit")

cel = int(input("Ingrese grados Celsius:"))

F = (cel*9/5)+32

print("Los grados Fahrenheit son: ")
print(F)

print("Promedio de 3 numeros")

num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))
num3 = int(input("Numero 3:"))

promedio = (num1+num2+num3)/3

print("El promedio es: ")
print(promedio)

print("Area de un circulo dado su radio")

radio = int(input("Ingrese el radio:"))

area = 3.1416*(radio**2)
perimetro = 2*3.1416*radio

print("El area es: ")
print(area)
print("El perimetro es: ")
print(perimetro)

import math

print("Resolver ecuación cuadrática")

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

res = b**2 - 4*a*c

if res >= 0:
    x1 = (-b + math.sqrt(res)) / (2*a)
    x2 = (-b - math.sqrt(res)) / (2*a)
    print("Las soluciones son: ", "x1 =", x1, "y", "x2 = ", x2)
else:
    print("No hay soluciones reales.")

print("programa par o impar ")

numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

print("Programa año bisiesto")
Año = int(input("Ingrese el año: "))

if Año % 4 == 0:
    if Año % 100 == 0:
        if Año % 400 == 0:
            print("El año", Año, "es un año bisiesto.")
        else:
            print("El año", Año, "no es un año bisiesto.")
    else:
        print("El año", Año, "es un año bisiesto.")
else:
    print("El año", Año, "no es un año bisiesto.")

print("Persona de la tercera edad")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 70:
    print("Señor@:",nombre,"Tiene Prioridad en la Fila")
else:
  print("Señor@:",nombre,"No tiene Prioridad en la Fila")

print("Comparación de numeros")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("El mayor número es:", numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("El mayor número es:", numero2)
else:
    print("El mayor número es:", numero3)

print("Programa Triangulo")
LadoA = int(input("Ingrese el tamaño del lado A: "))
LadoB = int(input("Ingrese el tamaño del lado B: "))
LadoC = int(input("Ingrese el tamaño del lado C: "))

if LadoA == LadoB == LadoC:
    print("El triángulo es equilátero.")
    if LadoA == LadoB or LadoA == LadoC or LadoB == LadoC:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

print("Programa Masa Corporal")
nombre = input("Introduce tu nombre: ")
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

IMC = peso / (altura ** 2)
if IMC < 18.5:
    categoria = "Bajo peso"
    descripcion = "Debes considerar aumentar tu ingesta calórica y realizar actividad física para ganar masa muscular."
elif 18.5 <= IMC < 24.9:
    categoria = "Normal"
    descripcion = "Tu peso es saludable. Mantén una dieta equilibrada y realiza ejercicio regularmente."
elif 25 <= IMC < 29.9:
    categoria = "Sobrepeso"
    descripcion = "Es recomendable que consideres hacer ajustes en tu dieta y realizar más ejercicio para evitar problemas de salud."
else:
    categoria = "Obesidad"
    descripcion = "Es importante que consultes a un médico para recibir orientación sobre una dieta adecuada y ejercicio físico."

print(nombre, "tu IMC es:", IMC)
print("Categoría:", categoria)
print(descripcion)

print("Calculadora")
num1 = float(input("Ingrese el número A: "))
num2 = float(input("Ingrese el número B:"))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: No se puede dividir entre cero.")
        resultado = None
else:
    print(resultado)
    print("Operador no válido.")

if resultado is not None:
    print("El resultado es:", resultado)

print("Calificación en letras según letra numérica")

calificacion = int(input("Ingrese la calificación numérica: "))

if calificacion == 100:
  print("Tiene una A")
elif calificacion >= 90:
  print("Tiene una B")
elif calificacion >= 80:
  print("Tiene una C")
elif calificacion >= 70:
  print("Tiene una D")
elif calificacion  >= 60:
  print("Tiene una F")

print("Día semana")

dia = int(input("Ingrese la calificación numérica: "))

if dia == 1:
  print("Lunes")
elif dia == 2:
  print("Martes")
elif dia == 3:
  print("Miércoles")
elif dia == 4:
  print("Jueves")
elif dia  == 5:
  print("Viernes")
elif dia == 6:
  print("Sábado")
elif dia  == 7:
  print("Domingo")

# Solicitar al usuario que ingrese los tres números
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Validar si pueden formar un triángulo
if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo.")

    # Determinar el tipo de triángulo
    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("No pueden formar un triángulo.")

import random

num = random.randint(1, 10)

for i in range(0, 11):
    res = num * i
    print(res)

import random

print("Suma números naturales")

num = random.randint(1,10)

for i in range(0, num):
  res = num+i
  print(res)

print("Cálculo número factorial")

num = int(input("Ingresa un número entero positivo: "))

if num < 0:
    print("El número debe ser positivo.")
else:
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print("El factorial de ", num, " es: ", fact)

print("Programa serie fibonacci")

n = int(input("Ingresa cuántos números de la serie Fibonacci quieres ver: "))

a, b = 0, 1

print("Los primeros", n, "números de la serie Fibonacci son:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

import random

print("Adivinanza colores")

colores = []

for i in range(10):
    color = input(f"Ingresa el color {i + 1}: ").strip().lower()
    colores.append(color)

color_secreto = random.choice(colores)

intentos = 0
max_intentos = 10

print("¡El programa intentará adivinar el color secreto!")

while intentos < max_intentos:
    intentos += 1
    print(f"\nIntento {intentos}:")

    intento = random.choice(colores)
    print(f"El programa piensa que el color secreto es: {intento}")

    if intento == color_secreto:
        print(f"¡El programa adivinó el color secreto '{color_secreto}' en {intentos} intentos!")
        break
    else:
        print("Incorrecto. Intentando de nuevo...")
a
if intentos == max_intentos:
    print(f"\nEl programa no pudo adivinar el color secreto '{color_secreto}' en {max_intentos} intentos.")

print("Números pares del 1 al 100")

for i in range(1, 101):  # range(1, 101) para incluir del 1 al 100
    if i % 2 == 0:  # Verificar si el número es par
        print("El número", i, "es par")
    else:
        print("El número", i, "es impar")

print("Programa que calcule la suma de los dígitos de un número.")

numero = input("Ingresa un número: ")
suma = 0

for digito in numero:
  suma += int(digito)
  print(f"La suma de los dígitos de {numero} es: {suma}")

print("Programa número primo")

numero = int(input("Ingresa un número: "))

if numero <= 1:
    print(numero, " no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

print("el patrón de un triángulo con asteriscos")
def triangulo_con_while(n):
    i = 1
    while i <= n:  # Ciclo para las filas
        j = 1
        while j <= i:  # Ciclo para imprimir los asteriscos en cada fila
            print("*", end="")
            j += 1
        print()  # Salto de línea después de cada fila
        i += 1

n = int(input("Ingrese el número de filas para el triángulo: "))
triangulo_con_while(n)

print("la potencia de un número sin usar el operador")
def potencia_con_while(base, exponente):
    resultado = 1
    contador = 0
    while contador < exponente:  # Multiplicar la base "exponente" veces
        resultado *= base
        contador += 1
    return resultado

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es: {potencia_con_while(base, exponente)}")

print("Tablas de multiplicar 1 al 10")
def mostrar_tablas_multiplicar():
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Salto de línea entre tablas

mostrar_tablas_multiplicar()

print("números perfectos hasta n")
def es_numero_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores == num

def encontrar_numeros_perfectos(n):
    numeros_perfectos = []
    for i in range(1, n + 1):
        if es_numero_perfecto(i):
            numeros_perfectos.append(i)
    return numeros_perfectos

n = int(input("Ingrese un número n: "))
print(f"Números perfectos hasta {n}: {encontrar_numeros_perfectos(n)}")

print("diamante con asteriscos")
def generar_diamante(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = int(input("Ingrese el tamaño del diamante: "))
generar_diamante(n)

print("números Armstrong hasta n")
def es_numero_armstrong(num):
    digitos = [int(d) for d in str(num)]
    longitud = len(digitos)
    suma = sum([d ** longitud for d in digitos])
    return suma == num

def encontrar_numeros_armstrong(n):
    numeros_armstrong = []
    for i in range(1, n + 1):
        if es_numero_armstrong(i):
            numeros_armstrong.append(i)
    return numeros_armstrong

n = int(input("Ingrese un número n: "))
print(f"Números Armstrong hasta {n}: {encontrar_numeros_armstrong(n)}")

print("reloj digital mostrando horas, minutos y segundos durante un período específico")
!pip install pytz
import datetime
import pytz
import time

def reloj_digital_colombia(duracion):
    zona_horaria_colombia = pytz.timezone('America/Bogota')

    for _ in range(duracion):
        ahora = datetime.datetime.now(zona_horaria_colombia)
        print(ahora.strftime("%H:%M:%S"))
        time.sleep(1)

duracion = int(input("Ingrese la duración en segundos: "))
reloj_digital_colombia(duracion)

"""Con Operador Terniario ejercicios del 6 al 10"""

# Solicitar número al usuario
numero = int(input("Ingrese un número: "))

# Operador ternario para determinar si es par o impar
resultado = "Par" if numero % 2 == 0 else "Impar"
print(f"El número {numero} es {resultado}")

# Solicitar año al usuario
año = int(input("Ingrese un año: "))

# Operador ternario para determinar si es bisiesto
es_bisiesto = "Bisiesto" if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) else "No bisiesto"
print(f"El año {año} es {es_bisiesto}")

# Solicitar nombre y edad al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Operador ternario para determinar prioridad en la fila
prioridad = "Se le da prioridad en la fila" if edad >= 70 else "No tiene prioridad en la fila"
print(f"{nombre}, {prioridad}")

# Solicitar tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Operador ternario para encontrar el mayor
mayor = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
print(f"El número mayor es: {mayor}")

triangulo = lambda a, b, c: print(f"{a}, {b}, {c} " + ("no forman triángulo" if not (a+b>c and a+c>b and b+c>a) else f"forman un triángulo {['Equilátero', 'Isósceles', 'Escaleno'][len(set([a,b,c]))-1]}"))(3, 3, 3)

tabla = lambda n: print('\n'.join([f"{n} x {i} = {n*i}" for i in range(1,11)]))(5)

suma_n = lambda n: print(sum(range(n+1)))(10)

from functools import reduce; factorial = lambda n: print(reduce(lambda x,y: x*y, range(1,n+1),1) if n>=0 else None)(5)

fib = lambda n: print(reduce(lambda x,_: x + [x[-1]+x[-2]], range(n-2), [0,1]) if n>2 else [0]*(n>0) + [1]*(n>1))(10)

adivina_color = lambda: [print(f"¿Es {c}?") or input("¿Acerté? (s/n): ")=='s' and exit() for c in [input(f"Color {i+1}: ") for i in range(10)]]()

pares = lambda: print([i for i in range(2,101,2)])()

suma_digitos = lambda n: print(sum(map(int, str(n))))(123)

primo = lambda n: print(n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)))(17)

triangulo_asteriscos = lambda n: print('\n'.join('*'*i for i in range(1,n+1)))(5)

potencia = lambda b, e: print(reduce(lambda x,_: x*b, range(e),1))(2,3)

tablas = lambda: print('\n\n'.join(['\n'.join(f"{i} x {j} = {i*j}" for j in range(1,11)) for i in range(1,11)]))()

perfectos = lambda n: print([x for x in range(1,n+1) if sum([i for i in range(1,x) if x%i==0]) == x])(10000)

diamante = lambda k: print('\n'.join([' '*(k-i-1)+'*'*(2*i+1) for i in range(k)] + [' '*(k-i-1)+'*'*(2*i+1) for i in range(k-2,-1,-1)]))(5)

armstrong = lambda n: print([x for x in range(1,n+1) if sum(int(d)**len(str(x)) for d in str(x)) == x])(1000)

reloj = lambda: [print(f"{h:02}:{m:02}:{s:02}") for h in range(24) for m in range(60) for s in range(60)]()

