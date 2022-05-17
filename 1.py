"""
Realice un programa donde se le pida al usuario que ingrese un numero y compruebe si es par
o impar, ademas mostrar el resto de la division
"""
a = int(input("Ingrese un numero"))
if a % 2==0:
    print("Es un numero par")
else:
    print("Es un numero impar")
print(f"El resto de la division es {a%2}")

