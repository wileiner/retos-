rangoMaximo = int(input("Ingrese el número del rango máximo: "))
divisor = int(input("Ingrese el divisor del rango: "))

# Validación para evitar división por cero
if divisor == 0:
    print("El divisor no puede ser 0.")
else:
    numerosDivisibles = []

    for i in range(1, rangoMaximo + 1):
        if i % divisor == 0:
            numerosDivisibles.append(i)

    print(f"Los números divisibles por {divisor} en el rango de 1 a {rangoMaximo} son:")
    print(", ".join(map(str, numerosDivisibles)))
