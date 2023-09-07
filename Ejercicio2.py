nombre_completo = input("Por favor, introduce tu nombre completo: ")

print("Nombre completo en minúsculas:", nombre_completo.lower())

print("Nombre completo en mayúsculas:", nombre_completo.upper())

nombres_apellidos = nombre_completo.split()

nombre_formateado = " ".join([nombre.capitalize() for nombre in nombres_apellidos])
print("Nombre completo formateado:", nombre_formateado)
