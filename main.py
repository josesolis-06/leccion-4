palabra = "Jose"
#print(palabra[0])
#print(palabra[1])
#print(palabra[2])
#print(palabra[3])
#print(palabra[4])
#print(palabra[5])

marcas = ["BMW", "Honda", "Nissan"]
for marca in marcas:
    print(marca)
indice = 0
for marca in marcas:
    print(indice, marca)
    indice = indice +1

for indice, letra in enumerate(palabra):
    print(indice, letra)