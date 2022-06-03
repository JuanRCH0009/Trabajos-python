#manejo de canenas
"""
miGrupoFavorito = "Iron Maiden"
caracteristicas = "The best heavy metal band"
print("mi grupo favorito es" ,miGrupoFavorito, caracteristicas)
numero1 = "7"
numero2 = "8"
print(int (numero1)+ int (numero2))
#Tipos booleanos (boole)
miBooleano = 3 > 2
print(miBooleano)
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
#Procesar entarda del usuario
#Funcion Input
Resultado=input("Digite un número: ") #Regresa un dato tipo "string"
print(Resultado)
#Conversion de la entrada de datos
numero1 = int (input("Escribe el primer numero: "))
numero2 = int (input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
#Realizar un programa que calcule el area y el perimtro de un rectangulo
ladoA = int (input("Ingrese el valor del lado A "))
ladoB = int (input("Ingrese el valor del lado B "))
perimero = (ladoA*2)+(ladoB*2)
area = ladoA * ladoB
print(f"El perimetro del rectangulo es: {perimero}")
print(f"El area del rectangulo es: {area}")

#Operadores de reasignacion
miVariable3 = 10
print(miVariable3)
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3+= 1
print(miVariable3)
miVariable3-=1
print(miVariable3)
miVariable3*=2
print(miVariable3)
miVariable3//=2
print(miVariable3)

#Operadores de comparacion
#Operadores iguales
d = 4
b = 4
resultado = d==b #Comprueba si son iguales
print(resultado)
#Operadores diferentes
resultado = b != d
print(resultado)
#Operador mayor que
resultado = d>b
print(resultado)
#Operador menor que
resultado = d<b
print(resultado)
#Operador menor o igual
resultado = d<=b
print(resultado)
#Operador mayor o igual
resultado = d>=b
print(resultado)
"""

#Operadores logicos

#Operador "and"
a = True
b = True
resultado = a and b
print(resultado)

#Operador "or"
resultado = a or b
print(resultado)

#operador "not"
resultado = not a
print(resultado)
