fraseDeUsuario = input("Ingresa una frase: ")

# Verificamos que el usuario haya ingresado una frase
if not fraseDeUsuario:
    print("No ingresaste ninguna frase.")
else:
    palabras = fraseDeUsuario.split()

    numeroDePalabras = len(palabras)

print(numeroDePalabras)