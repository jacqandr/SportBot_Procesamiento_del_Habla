from memory import (
    guardar_conversacion,
    obtener_historial,
    limpiar_memoria
)

# Limpiar la memoria antes de comenzar
limpiar_memoria()

# Simular una conversación
guardar_conversacion(
    "Hola, soy Roque",
    "Hola Roque, ¿en qué puedo ayudarte?"
)

guardar_conversacion(
    "Busco unas zapatillas Adidas",
    "Perfecto. ¿Qué talle necesitás?"
)

# Mostrar el historial
print("=== HISTORIAL ===")
print(obtener_historial())
