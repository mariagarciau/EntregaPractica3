"""
En este desafío, probamos su conocimiento sobre el uso de declaraciones
condicionales if-else para automatizar los procesos de toma de decisiones.
Juguemos un juego para darte una idea de cómo diferentes algoritmos para el mismo
problema pueden tener eficiencias muy diferentes.
Deberás desarrollar un algoritmo que seleccionará aleatoriamente un número entero
entre 1 y 15.
El usuario deberá ser adivinando, deberemos permanecer en la condición hasta
encontrar el número seleccionado.
Además nos deberá dar una pista( si es mayor o menor)  en cada intento.
Ahora desarrolla el código para un número del 1 al 300, sabiendo que no deberías
necesitar más de 9 intentos.
"""
import random
numeroRandom = random.randint(1,15)
numeroIntroducido = int(input("Introduzca un número entre 1 y 15: "))
while numeroIntroducido != numeroRandom:
    if numeroRandom < numeroIntroducido:
        print("El número que debe adivinar es menor")
        numeroIntroducido = int(input("Introduzca un número entre 1 y 15: "))
    elif numeroRandom > numeroIntroducido:
        print("El número que debe adivinar es mayor")
        numeroIntroducido = int(input("Introduzca un número entre 1 y 15: "))
print("Has acertado el número")

numeroRandom2 = random.randint(1,300)
numeroIntroducido2 = int(input("Introduzca un número entre 1 y 300: "))
intentos : int
intentos = 1
while numeroIntroducido2 != numeroRandom2:
    intentos +=1
    if intentos>9:
        break
    elif numeroRandom2 < numeroIntroducido2:
        print("El número que debe adivinar es menor")
        numeroIntroducido2 = int(input("Introduzca un número entre 1 y 300: "))
    elif numeroRandom2 > numeroIntroducido2:
        print("El número que debe adivinar es mayor")
        numeroIntroducido2 = int(input("Introduzca un número entre 1 y 300: "))
if intentos<9:
    print("Has acertado el número")
