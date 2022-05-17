"""
Tienda de libros
Mostrar:
1) Nombre del libro
2) ID del libro
3) Precio del libro
4) Determinar si tiene envio gratis
"""
print("Ingrese los siguentes datos del libro: ")
nombre = input("Ingrese el titulo del libro")
idDelLibro = int (input("Ingrese el ID del libro"))
precio = float (input("Ingrese el precio del libro"))
envio = input("Determine si el envio es gratiuto ('S' o 'N', 's' o 'n', 'Si' o 'No', 'SI' o 'NO')")
print(f"El nombre del libro es: {nombre}")
print(f"El ID del libro es: {idDelLibro}")
print(f"El precio del libro es {precio}")
if envio == "s" or envio == "S" or envio == "si" or envio == "Si" or envio == "SI":
    print("No hay costo de envio")
elif envio == "n" or envio == "N" or envio == "no" or envio == "No" or envio == "NO":
    print("El envio no es gratuito")
else:
    print("Caracter no valido. Determine si el envio es gratiuto ('S' o 'N', 's' o 'n', 'Si' o 'No', 'SI' o 'NO')")

