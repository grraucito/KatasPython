# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
nuevo = input('Ingresa el nombre del planeta (La primer letra debe ser mayuscula):')

# Busca el planeta en la lista
indice = planets.index(nuevo)

# Muestra los planetas más cercanos al sol
print(f'Los planetas mas cercanos a {nuevo}')
print(planets[0:indice])

# Muestra los planetas más lejanos al sol
print(f'Los planetas mas lejanos a {nuevo}')
print(planets[indice+1:])