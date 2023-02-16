palabra = "papa"

indice = 0
for letra in palabra:
    print(indice, palabra)
    indice = indice +1
    
print(indice)

for letra in palabra:
    if letra == "a":
        print(letra)