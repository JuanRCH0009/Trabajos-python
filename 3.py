"""
Realize un programa donde se le pida al usuario que ingrese un numero que se encuentre entre 0 y 5,
este debera determinar si el numero se encuentra o no dentro del rango.
"""
num = int(input("Ingrese un numero de rango 0-5"))
if num >= 0 and num<=5:
    print(f"El numero {num} esta dentro del rango")
else:
    print(f"El numero {num} no esta dentro del rango")
