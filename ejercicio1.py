#Realiza el psedocódigo y un desarrollo en Python para calcular la distancia recorrida (m)
# por un móvil que tiene velocidad constante (m/s) durante un tiempo t (s), considerar que
# es un MRU (Movimiento Rectilíneo Uniforme).
distancia : float
velocidad = float(input("Introduce la velocidad en m/s que lleva: "))
tiempo = float(input("Introduce el tiempo en segundos que ha tardado: "))
#Suponiendo que la distancia inicial recorrida es de 0m, calculamos la distancia
#total recrrida como distancia = velocidad*tiempo
distancia = velocidad*tiempo
print(distancia)