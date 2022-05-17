#Realize un programa donde se le pida al usuario que ingrese dos numeros y determinar cual es el mayor

num1 = int (input("Ingrese un numero"))
num2 = int (input("Ingrese otro numero"))
if num1 > num2:
    print(f"El numero ({num1}) es el mayor" )
elif num1 == num2:
    print("Los numeros son iguales")
else:
    print(f"El numero ({num2}) es el mayor")