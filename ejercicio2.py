#Realiza el psedocódigo y un desarrollo en Python para obtener el promedio simple
# de un estudiante a partir de sus tres notas parciales N1, N2 y N3.
N1 : float
N2 : float
N3 : float
N1 = input("Introduzca la primera nota: ")
N2 = input("Introduzca la segunda nota: ")
N3 = input("Introduzca la tercera nota: ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
promedio : float
promedio= (N1+N2+N3)/3
print(promedio)