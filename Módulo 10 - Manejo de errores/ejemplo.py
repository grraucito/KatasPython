# Declara dos variables
new_planet = ''
planets = []

# Escribe el ciclo while solicitado
while new_planet != 'done':
    new_planet = input('Nuevo Planeta:')
    if new_planet != 'done':
        planets.append(new_planet)

# Escribe tu ciclo for para iterar en una lista de planetas
print('---------------------------------------------------')
print('La lista de planetas es :')
for planet in planets:
    print(f'El planeta es:{planet}')