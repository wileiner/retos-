import random
numero = random.randint (1,10)

while True:
    usuario = int(input("Ingresa un numero: "))
    if usuario > numero:
        print("El numero es menor")

    elif usuario < numero:
        print("El numero es mayor")

    elif usuario == numero:
        print("Felicidades adivinaste el numero.")
        break
