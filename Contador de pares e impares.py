numero = int(input("¿Cuentos numero deseas ingresar?: "))

pares = 0
impares = 0

for _ in range (numero ):
   num = int(input("Ingresa el numero: "))
   if num % 2 == 0:
       pares += 1
   else:
       impares += 1

print(f"ingresaste {pares} numeros pares y {impares} numero impares.")