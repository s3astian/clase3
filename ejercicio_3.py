## creacion de programa de analisis de texto
texto = input ("hola bienvenido al sistema de inteligencia menos inteligente de analisis de texto  por fabor ingresa tu texto :")
textol1 = texto.split()
letr1 = input ("se requiere que ingreses 3 letras a tu eleccion para comenzar la magia...   ingresa letra 1 : ")
letr2 = input (" ingresa letra 2 : ")
letr3 = input (" ingresa letra 3 : ")

l1 = textol1.count(letr1)
l2 = textol1.count(letr2)
l3 = textol1.count(letr3)

print ("sabes cuantas letras de las que elejiste estan en tu texto? aqui te muestro : " )
print ( " para la letra :" , letr1 , "en total hay ", l1)
print ( " para la letra :" , letr2 , "en total hay ", l2)
print ( " para la letra :" , letr3 , "en total hay ", l3)

print ("los caracteres de todo tu texto son", len(textol1))
fragmento =  textol1 [0]
fragmento2 = textol1 [-1]
print ("El primer caracter de tu texto es : " , fragmento ,"..y el ultimo es :" , fragmento2 )
print ("tu texto invertido se veria de la siguiente manera: ", (texto)[::-1])
print ("la palabra python se encuentra en la posicion : " , texto.find("python"))
