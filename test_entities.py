from entities import extraer_entidades

texto = "Hola, soy Roque y busco unas zapatillas Adidas negras talle 42 para running."

resultado = extraer_entidades(texto)

print("Entidades encontradas:")
print(resultado)
