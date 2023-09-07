cesta_compra = input("Por favor, introduce los productos de la cesta de compra separados por comas: ")

productos = cesta_compra.split(',')

print("Productos en la cesta de compra:")
for producto in productos:
    print(producto.strip())  
