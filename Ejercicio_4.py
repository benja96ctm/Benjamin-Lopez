#4.	Permita el ingreso de n números. Al final muestre la suma de ellos

limite = int(input("ingrese la cantidad de numeros que quiera: "))
vueltas = 0
acumulador = 0

while(True):
    numeros = int(input("numeros: "))
    vueltas += 1
    acumulador += numeros

    if(vueltas == limite):
        break

print("la suma es: ", acumulador)



