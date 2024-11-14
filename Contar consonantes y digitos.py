frase = input("Ingresa una frase: ")

letras = 0
digitos = 0

for i in (frase):
    if i.isalpha ():
        letras += 1

    elif i.isdigit ():
        digitos += 1

print (f"Esta frase tiene {letras} consonantes y {digitos} digitos.")
