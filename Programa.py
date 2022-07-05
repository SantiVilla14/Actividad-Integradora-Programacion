numeros=[]
cantidad = 5
print()
print("Bienvenido Usuario!!")
print()
print("Escriba 5 numeros enteros")

for i in range(cantidad):
    numero=(input("ingresa un numero: "))
    numero = int(numero)
    numeros.append(numero)

print()
print("Que quieres hacer con estos numeros: ", numeros)
print()
print("[1 - Función Suma] [2 - Función Promedio] [3 - Función Máximo] [4 - Función Mínimo] [Cualquier otro - Salir]")
i=int(input())

if i==1:
    def sumar(numeros):
        suma=0
        for elemento in numeros:
            suma += elemento
        return suma

    print("La suma de tus numeros es:")
    print(sumar(numeros))

elif i==2:
    suma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
    promedio = float(suma // 5)
    print("El promedio de tus numeros es:")
    print(promedio)

elif i==3:
    print("El maximo de tus numeros es: ")
    print(max(numeros))

elif i==4:
        print("El minimo de tus numeros es: ")
        print(min(numeros))
else:
    print()
    print("Saliendo...")
print()
print("Gracias por usar este programa")