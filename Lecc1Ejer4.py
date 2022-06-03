"""
Realize un programa donde se le pida al usuario que ingrese su edad, el programa debe determinar en que rango
de edad se encuentra (20-30 o 30-40)
"""
edad = int(input("Ingrese su edad "))
if edad >=20 and edad < 30:
    print(f"Su edad ({edad}) esta dentro del rango 20-30 años")
elif edad >=30 and edad <40:
    print(f"Su edad ({edad}) esta dentro del rango 30-40 años")
else:
    print(f"Su edad ({edad}) no es aceptada dentro del rango")