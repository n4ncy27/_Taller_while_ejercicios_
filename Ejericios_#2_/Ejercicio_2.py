# Hacer el diagrama de flujo y el programa en Python que lea un numero entero y positivo de cualquier número 
# de dígitos, que le calcule su numero inverso y lo imprima junto con el numero leído.

print("-------------------------------------")
print("------------numero inverso-----------")
print("-------------------------------------")

n = int(input("Digita un número entero y positivo: "))
m = n
ni = 0

while n != 0:
    d = (n // 10)
    r = n - d * 10
    ni = ni *10 + r
    n = d  

print("El número es: ", m)
print("La suma de los digitos es: ",ni)