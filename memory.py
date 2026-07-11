from langchain_classic.memory import ConversationBufferMemory

# Crear la memoria conversacional
memory = ConversationBufferMemory(
    return_messages=True
)

def guardar_conversacion(usuario, respuesta):
    """
    Guarda el intercambio entre el usuario y SportBot.
    """

    memory.save_context(
        {"input": usuario},
        {"output": respuesta}
    )

def obtener_historial():
    """
    Devuelve todo el historial de la conversación.
    """

    return memory.load_memory_variables({})

def limpiar_memoria():
    """
    Borra toda la conversación.
    """

    memory.clear()
    
