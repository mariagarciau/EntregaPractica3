"""
Cada cuatro años, se agrega un día adicional al calendario, el 29 de febrero, y el año se
denomina día bisiesto.
Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente
365,25 días en orbitar el sol. Un año bisiesto contiene un día bisiesto.
En el calendario gregoriano, se utilizan tres condiciones para identificar los años
bisiestos:
• El año se puede dividir uniformemente por 4, es un año bisiesto, a menos
que:
    o El año se puede dividir uniformemente por 100, NO es un año
    bisiesto, a menos que:
        ▪ El año también es divisible uniformemente por 400.
        Entonces es un año bisiesto.
Esto significa que, en el calendario gregoriano, los años 2000 y 2400 son años bisiestos,
mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos.
Dado un año, determine si es un año bisiesto. Si es un año bisiesto, devuelva el
booleano True; de lo contrario, vuelva False.
Tenga en cuenta que el código auxiliar proporcionado lee de STDIN y pasa argumentos
a la  fusión is_leap. Solo es necesario completar la función is_leap.
def is_leap(year):
    leap = False
    # Write your logic here
    return leap
year = int(input())
print(is_leap(year))
"""
def is_leap(year):
    leap = False
    if year%4 == 0 or year%400 == 0 and not year%100==0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    return leap
year = int(input())
print(is_leap(year))