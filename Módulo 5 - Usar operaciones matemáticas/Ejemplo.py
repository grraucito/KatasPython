# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")
primero = input('Distancia del 1er planeta:')
segundo = input('Distancia del 2do planeta:')

# Convierte las cadenas de ambos planetas a números enteros
distancia1 = int(primero)
distancia2 = int(segundo)

# Realizar el cálculo y determinar el valor absoluto
distance = distancia1 - distancia2
print(abs(distance))

# Convertir de KM a Millas
print(abs(distance * 0.621))