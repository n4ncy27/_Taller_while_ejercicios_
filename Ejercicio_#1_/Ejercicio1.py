# Hacer el diagrama de flujo y el programa en Python que lea un numero n entero y positivo de cualquier número de dígitos, que 
# calcule la suma de sus dígitos y la imprima junto con los números leídos.

print("-------------------------------------")
print("--------suma de sus digitos ---------")
print("-------------------------------------")

n = int(input("Digita un número entero y positivo: "))

sum = 0
m = n

while n != 0:
    d = (n // 10)
    r = n - d * 10
    sum = sum + r
    n = d  

print("La suma de los digitos es: ",sum)
print("El número es: ", m)