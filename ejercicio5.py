#Construya un diagrama de flujo (DF) un pseudocódigo y un desarrollo
# en Python que resuelva un problema que tiene una gasolinera. Los
# dispensadores de esta registran lo que “surten” en galones, pero
# el precio de la gasolina está fijado en litros. El desarrollo debe
# calcular e imprimir lo que hay que cobrarle al cliente.

#Como no nos dan el precio, supongo que son 0.965€ el litro
precio = float(0.965)
galones = float(input("Introduce los galones que ha echado a su depósito: "))
#1 galón son 3.78541 litros
litros = galones*3.78541
precio *=litros
print(precio)