"""
El código proporcionado lee dos números enteros.
    #Python 2
    a  =  int ( raw_input ())
    b  =  int ( raw_input ())
    #Python 3
    # a  =  int ( input ())
    # b  =  int ( input ())
En las declaraciones anteriores, raw_input()y input()están los métodos de Python 2 y
Python 3 para leer líneas. Los métodos devuelven una cadena de forma
predeterminada. Dado que este problema utiliza datos numéricos, el valor de entrada
debe convertirse a un número entero.
Ahora, un poco sobre los operadores aritméticos.
Los tres operadores aritméticos básicos son los siguientes:
    • Suma (+)
    • Resta (-)
    • Multiplicación (*)
De los tres operadores que se muestran, la multiplicación tiene prioridad sobre la
suma y la resta. La suma y la resta tienen igual precedencia.
Agregue código para imprimir tres líneas donde:
    1. La primera línea contiene la suma de los dos números.
    2. La segunda línea contiene la diferencia de los dos números (primero -
    segundo).
    3. La tercera línea contiene el producto de los dos números.
Ahora queremos que trabajéis la división, debéis añadir
La cuarta línea debe contener el resultado de la división de enteros, // .
La quinta línea debe contener el resultado de la división flotante, / .
"""
#Python 3
a  =  int ( input ())
b  =  int ( input ())
suma = a+b
resta = a-b
multiplicacion = a*b
divisionEnteros = a//b
divisionFloat = a/b
print(suma)
print(resta)
print(multiplicacion)
print(divisionEnteros)
print(divisionFloat)
