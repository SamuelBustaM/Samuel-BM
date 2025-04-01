# Punto 6
while True:
    n=int(input("Ingrese el numero de terminos (n): "))
    a=float(input("Ingrese el valor de a: "))

    if n > 0 and a !=0:
        break
    else:
        print("n debe ser mayor que 0 y a no puede ser 0 ")

c = 0
i=1
while i<=n:
    c += (1 / a)**i
    i +=1
print(f"El resultado de la sumatoria es {c}")