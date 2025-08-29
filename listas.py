

# miLista = ["Erik", "Estudiante", 26, 1.69, "Backend"]
# print(miLista[2])

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))


# numeros.append(num1)
# numeros.append(num2)


# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2


# print("Lista actualizada:", numeros)
# print(f"Suma de {num1} + {num2} = {suma}")
# print(f"Resta de {num1} - {num2} = {resta}")
# print(f"Multiplicación de {num1} * {num2} = {multiplicacion}")

#Diferentes formas de crear listas

lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ["Hola", "Mundo", "Python"]
lista_mixta = [1, "Hola", 3.14, True]

# for i in  range(5):
#     print(i)


frutas = ["manzana", "platano", "guinda"]
#append agrega un elemento al final de la lista
frutas.append("naranja")
print("Despues de append", frutas)

#insert agrega un elemento en la posicion que le indiquemos

frutas.insert(1, "kiwi")
print("Despues de insert", frutas)

#remove elimina un elemento por su valor
frutas.remove("guinda") 
print("Remover guinda", frutas)

numeros = [64, 34, 25, 12, 22, 11, 90]
numeros.sort(reverse=True)
#ordena la lista de menor a mayor
print(numeros)

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
#Como buscar elementos comunes en dos listas
comunes = list(set(lista_a) & set(lista_b))
print(" Los Elementos comunes son:", comunes)

#metodo for para encontrar elementos comunes en dos listas
comunes_for = []
for elemento in lista_a:
    if elemento in lista_b:
        comunes_for.append(elemento)
print("Elementos comunes con for:", comunes_for)

#metodo len para encontrar comunes en dos listas

coincidencias = []
for i in range (len(lista_a)):
    for j in range(len(lista_b)):
        if lista_a[i] == lista_b[j]:
            coincidencias.append(lista_a[i])
print("Elementos comunes con len:", coincidencias)


productos = ["laptop", "mouse", "teclado", "monitor"]
precios = [1200, 250, 80, 30]
existencias = [15, 50, 30, 20]

#listar todos los productos por orden y finalmente
#mostar el total del inventario

productos = ["laptop", "mouse", "teclado", "monitor"]
precios = [1200, 250, 80, 30]
existencias = [15, 50, 30, 20]

total_inventario = 0

print("Inventario de productos:\n")

for i in range(len(productos)):
    producto = productos[i]
    precio = precios[i]
    stock = existencias[i]
    subtotal = precio * stock
    total_inventario += subtotal

    print(f"{producto.capitalize():<10} | Precio: ${precio:<5} | Stock: {stock:<3} | Subtotal: ${subtotal}")

print("\nTotal del inventario:", total_inventario)

# print ("Inventario de productos:")
# print ("-"*40)

# for i in range(len(productos)):
#     valor_total = precios[i] * existencias[i]
#     print(f"Producto {productos[i]}")
#     print(f"Precio: {precios[i]}")
#     print(f"Existencias: {existencias[i]}")
#     print(f"valor total {valor_total}")
#     print("-"*40)


