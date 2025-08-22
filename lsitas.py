

# miLista = ["Erik", "Estudiante", 26, 1.69, "Backend"]
# print(miLista[2])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


numeros.append(num1)
numeros.append(num2)


suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2


print("Lista actualizada:", numeros)
print(f"Suma de {num1} + {num2} = {suma}")
print(f"Resta de {num1} - {num2} = {resta}")
print(f"Multiplicación de {num1} * {num2} = {multiplicacion}")
