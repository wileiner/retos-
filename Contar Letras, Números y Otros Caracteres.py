fraseDeUsuario = input("ingresa una frase: ")

letras = 0
digitos = 0
otrosCaracteres = 0

for i in fraseDeUsuario:
    if i.isalpha():
        letras += 1

    elif i.isdigit():
        digitos += 1

    else:
        otrosCaracteres += 1

print(f"la frase '{fraseDeUsuario} Tiene:'")
print(f"Letras: {letras}")
print(f"Digitos: {digitos}")
print(f"Otros caracteres: {otrosCaracteres}")