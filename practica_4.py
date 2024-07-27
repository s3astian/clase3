text = "hoy esta soleado"
variable= text.upper()
print (variable)

palabra1 = "aprender mucho"
palabra2 = " es bueno"
palabra3 = "desarrollas conocimientos"
palabra4 = " fortaleces la mente"
palabra5 = "creas conocimiento"
palabra6 = " es bueno para la salud"

resultado = " ".join([palabra1 , palabra2 , palabra3 , palabra4, palabra5 , palabra6])
print (resultado)

text2 = "si la implementacion es dificil de explicar, puede que sea una mala idea."
resultado = text2.replace("dificil" , "FACIL")
resultado2 = resultado.replace("mala" , "BUENA")

print (resultado2)