fecha_nacimiento = input("Por favor, introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

partes = fecha_nacimiento.split('/')

if len(partes) == 3:
    dia = partes[0]
    mes = partes[1]
    año = partes[2]

    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")
else:
    print("El formato de la fecha de nacimiento no es válido.")
   
