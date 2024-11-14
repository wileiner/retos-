FraseDeUsuario = (input("Ingresa una Frase: "))

vocales = 0
consonantes = 0

for letra in FraseDeUsuario:
    if letra.lower() in  "aeiou" :
        vocales += 1
    elif letra.isalpha():
        consonantes += 1

print(f"La frase '{FraseDeUsuario}' tinene {vocales} vocales y {consonantes} Consonantes.")