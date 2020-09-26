import math

#name = input("Nombre: ")
#print("Bienvenido, {}!".format(name))

num = int(input("Numero: "))
print("{}! = {}".format(num,math.factorial(num)))

if(num % 2 == 0):
    print(num,"es par")
else:
    print(num,"es impar")