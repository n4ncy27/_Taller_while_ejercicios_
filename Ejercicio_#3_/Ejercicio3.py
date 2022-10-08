# hacer el diagrama de flujo y el programa en Python, que calcule e imprima a partir del tercero, todos 
# los elementos de la serie de Fibonacci todos los números menores de mil


print("-------------------------------------")
print("------------Serie fibonacci----------")
print("-------------------------------------")

n = 3
a = 0 
b = 1
c = a + b

while c < 1000:
    a = b
    b = c
    c = a + b
    print("El absu",n,"es:",c)
    n = n + 1
