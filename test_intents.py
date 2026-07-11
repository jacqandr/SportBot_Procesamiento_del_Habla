from intents import detectar_intent

mensaje = "Busco unas zapatillas Adidas"

intent = detectar_intent(mensaje)

print(intent)