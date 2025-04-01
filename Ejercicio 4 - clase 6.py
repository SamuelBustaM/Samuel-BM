# Hacer un algoritmo que encuentre la suma de los numeros impares comprendidos entre 1 y N
while True:
    n = int(input("Ingrese un numero positivo: "))
    if n>0:
        break
    else:
        print("Debe ser un numero positivo ")

contador=0
i=1
while i<= n:
    contador+=i
    i+=2

print(f"La suma de los numeros impares entre 1 y {n} es: {contador}")