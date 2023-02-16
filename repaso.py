print("jose" + "1997" + "solis")


edad = 25


if edad > 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

lista_del_mago = "patas de araña", "lengua de rana", "ojo de buey"
print(lista_del_mago[1][3])

for elemento in lista_del_mago:
    print(elemento)

palabra = "oso"

acumulador = 0

for letra in palabra:
    if letra == "o":
        acumulador = acumulador + 1
print(acumulador)