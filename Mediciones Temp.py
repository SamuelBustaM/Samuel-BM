Nmed= int(input( "Ingrese el numero de mediciones: "))
prom=0
c=0
while c<Nmed:
    T=float(input("Temp: "))
    if T<15 or T>30 :
        print("ALERTA ")
    prom+=T
    c+=1
promedio=prom/Nmed
print (promedio)