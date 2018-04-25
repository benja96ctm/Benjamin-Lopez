#5.	Permita el ingreso de n números. Al final muestre el promedio de ellos

limite = int(input("ingrese sus notas de alguna asignatura: "))
vueltas = 0
acumulador = 0

while(True):
    numeros = float(input("numeros: "))
    vueltas += 1
    acumulador += numeros / limite

    if(vueltas == limite):
        break

print("el promedio es: ", acumulador)
