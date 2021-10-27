#Elaborar un algoritmo (pseudocódigo y desarrollo en Python)
#que permita ingresar el número de partidos ganados, perdidos
#y empatados, por ABC club en la liga, se debe de mostrar su
#puntaje total, teniendo en cuenta que por cada partido ganado
#obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.
partidosGanados = int(input("Introduce el número de partidos ganados: "))
partidosEmpatados = int(input("Introduce el número de partidos empatados: "))
partidosPerdidos = int(input("Introduce el número de partidos perdidos: "))

totalPuntos : int
totalPuntos = partidosGanados*3 + partidosEmpatados*1 + partidosPerdidos*0
print(totalPuntos)
