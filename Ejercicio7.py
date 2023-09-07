correo_original = input("Por favor, introduce tu correo electrónico: ")

nombre, dominio = correo_original.split('@')

nuevo_correo = f"{nombre}@ceu.es"

print("Nuevo correo electrónico:", nuevo_correo)
