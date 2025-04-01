
# Realice un algoritmo que permita calcular a partir de un numero de notas, el promedio de una materia, sabiendo que cada materia tiene el mismo porcentaje y estan evaluadas de 0 a 5
n = int(input("ingrese el numero de notas "))
contador=0
i=1
while (i <= n):
    print("Ingrese la nota numero: ",i)
    nota=float(input())
    contador=contador+nota
    i+=1
prom=contador / n 
print ("El promedio de notas es " ,prom)

