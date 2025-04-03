# Elabore un algoritmo que ecuentre el factorial de un numero entre 0 y 20.
while True:
    n = input("Ingrese un número entre 0 y 20 para calcular su factorial: ")

    if n.isdigit():  
        n = int(n)
        if 0 <= n <= 20:
            factorial = 1
            i = 2  
            
            while i <= n:
                factorial *= i
                i += 1  
            
            print(f"El factorial de {n} es: {factorial}")
        else:
            print("El número debe estar entre 0 y 20.")
    else:
        print("Ingrese un número entero válido.")

    repetir = input("¿Desea calcular otro factorial? (si/no): ").strip().lower()
    if repetir != 'si':
        print("Programa finalizado.")
        break
