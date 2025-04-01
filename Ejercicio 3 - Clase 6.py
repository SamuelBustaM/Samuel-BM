# Desarrolle un algoritmo que escriba en pantalla, uno despues del otro, los resultados de la funcion n^x desde 0 hasta n, con n entero positivo maximo 9 y x positivo maximo de 9.
n= int(input("Ingrese un numero entero positivo (maximo 9): "))
while True:
    if  1<= n <=9:
        break
else:
    print ("Escriba un numero valido entre 1 y 9")

x=int(input("Ingrese el exponente entero positivo (maximo 9): "))
while True:
    if 1<= x <=9:
        break
    else:
        print ("Escriba un numero valido entre 1 y 9")
i=0
while (i <=x): 
    resultado = n**i
    print(f"{n}**i = {resultado}")
    i+=1