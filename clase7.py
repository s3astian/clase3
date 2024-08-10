# Loops 
nombres = [ 'maria', 'jose' , 'carlos', 'martina' ]
for espacio in nombres:
    print("hola", espacio)
    
lista_numeros = [1,2,3,4,5]
suma = 0
for suma in lista_numeros:
    suma += suma
    
print(suma)

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
par = 0
inpar = 0

for numero in  lista_numeros :
    if numero % 2 == 0:
        par += numero
    else:
        inpar += numero
    
print(par)
print(inpar)

# for letra in nombres:
#     numero_letra=nombres.index(letra)
    

# for letra in "python":
#     print(letra)

# print(type(nombres))