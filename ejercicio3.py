#Se necesita elaborar un algoritmo (pseudocódigo y desarrollo en Python)
#que solicite el número de respuestas correctas, incorrectas y en blanco,
#correspondientes a un kahoot!, y muestre su puntaje final considerando que
#por cada respuesta correcta tendrá 3 puntos, respuestas incorrectas tendrá -1
#y respuestas en blanco tendrá 0.
correctas = int(input("Introduce el número de respuestas correctas: "))
incorrectas = int(input("Introduce el número de repuestas incorrectas: "))
blanco = int(input("Introduce el número de respuestas en balnco: "))

totalPuntos : int
totalPuntos = correctas*3 + incorrectas*-1 + blanco*0
print(totalPuntos)