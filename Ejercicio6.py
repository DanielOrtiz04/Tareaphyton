frase = input("Por favor, introduce una frase: ")

vocal = input("Ahora, introduce una vocal: ")

# Verificar si la vocal es una letra y es una vocal (a, e, i, o, u) en minúscula
if len(vocal) == 1 and vocal.isalpha() and vocal.lower() in 'aeiou':
    frase_con_vocal_mayuscula = frase.replace(vocal.lower(), vocal.upper())
    
    print("Frase con la vocal en mayúscula:", frase_con_vocal_mayuscula)
else:
    print("La vocal introducida no es válida.")
