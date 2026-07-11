import json

from entities import extraer_entidades
from intents import detectar_intent
from memory import guardar_conversacion
from prompts import SYSTEM_PROMPT


# =====================================
# Cargar catálogo
# =====================================

with open("catalogo.json", "r", encoding="utf-8") as archivo:
    catalogo = json.load(archivo)


# =====================================
# Estado de la conversación
# =====================================

estado_cliente = {
    "nombre": None,
    "producto": None,
    "marca": None,
    "talle": None,
    "color": None,
    "presupuesto": None
}


# =====================================
# Buscar productos
# =====================================

def buscar_producto(marca=None, categoria=None):

    resultados = []

    for producto in catalogo["productos"]:

        if marca:
            if producto["marca"].lower() != marca.lower():
                continue

        if categoria:
            if producto["categoria"].lower() != categoria.lower():
                continue

        resultados.append(producto)

    return resultados


# =====================================
# Función principal del chatbot
# =====================================

def responder_usuario(mensaje):

    # Detectar intención
    intent = detectar_intent(mensaje)

    # Detectar entidades
    entidades = extraer_entidades(mensaje)

    # Actualizar memoria del cliente
    for clave in estado_cliente:

        if clave in entidades and entidades[clave] is not None:

        # El nombre solo se guarda una vez
           if clave == "nombre":

            if estado_cliente["nombre"] is None:
                estado_cliente["nombre"] = entidades["nombre"]

        else:

            estado_cliente[clave] = entidades[clave]

    # =====================================
    # SALUDO
    # =====================================

    if intent == "saludo":

        if estado_cliente["nombre"]:

            respuesta = (
                f"¡Hola {estado_cliente['nombre']}! 👋\n\n"
                "Bienvenido a Hernández Sport.\n"
                "¿En qué puedo ayudarte hoy?"
            )

        else:

            respuesta = (
                "¡Hola! 👋\n\n"
                "Bienvenido a Hernández Sport.\n"
                "¿Cómo te llamás?"
            )

    # =====================================
    # PRESENTARSE
    # =====================================

    elif intent == "presentarse":

        if estado_cliente["nombre"]:

            respuesta = (
                f"Mucho gusto, {estado_cliente['nombre']} 😊\n\n"
                "¿Qué producto estás buscando hoy?"
            )

        else:

            respuesta = (
                "Mucho gusto 😊\n\n"
                "¿Qué producto estás buscando?"
            )

    # =====================================
    # BUSCAR PRODUCTO
    # =====================================

    elif intent == "buscar_producto":

        productos = buscar_producto(
            marca=estado_cliente["marca"],
            categoria=estado_cliente["producto"]
        )

        if productos:

            producto = productos[0]

            respuesta = (
                "✅ Encontré este producto:\n\n"
                f"👟 Producto: {producto['nombre']}\n"
                f"🏷 Marca: {producto['marca']}\n"
                f"🎯 Deporte: {producto['deporte']}\n"
                f"🎨 Color: {producto['color']}\n"
                f"💲 Precio: ${producto['precio']}\n"
                f"🎁 Descuento: {producto['descuento']}%\n\n"
                "¿Querés conocer más detalles o ver otras opciones?"
            )

        else:

            respuesta = (
                "No encontré productos con esas características.\n"
                "Probá con otra marca o categoría."
            )

    # =====================================
    # CONSULTAR PRECIO
    # =====================================

    elif intent == "consultar_precio":

        productos = buscar_producto(
            marca=estado_cliente["marca"],
            categoria=estado_cliente["producto"]
        )

        if productos:

            producto = productos[0]

            respuesta = (
                f"💲 El precio de **{producto['nombre']}** "
                f"es de **${producto['precio']}**."
            )

        else:

            respuesta = (
                "Primero decime qué producto estás buscando."
            )

    # =====================================
    # CONSULTAR STOCK
    # =====================================

    elif intent == "consultar_stock":

        productos = buscar_producto(
            marca=estado_cliente["marca"],
            categoria=estado_cliente["producto"]
        )

        if productos:

            producto = productos[0]

            if producto["stock"]:

                respuesta = (
                    f"Sí ✅\n\n"
                    f"Tenemos stock disponible de {producto['nombre']}."
                )

            else:

                respuesta = (
                    "Actualmente ese producto no tiene stock."
                )

        else:

            respuesta = (
                "No pude identificar el producto."
            )

    # =====================================
    # CONSULTAR PROMOCIÓN
    # =====================================

    elif intent == "consultar_promocion":

        productos = buscar_producto(
            marca=estado_cliente["marca"],
            categoria=estado_cliente["producto"]
        )

        if productos:

            producto = productos[0]

            respuesta = (
                f"🎉 Actualmente {producto['nombre']} "
                f"tiene un descuento del {producto['descuento']}%."
            )

        else:

            respuesta = (
                "No encontré promociones para ese producto."
            )

    # =====================================
    # DESPEDIDA
    # =====================================

    elif intent == "despedida":

        if estado_cliente["nombre"]:

            respuesta = (
                f"¡Gracias por visitarnos, {estado_cliente['nombre']}! 😊\n\n"
                "Te esperamos nuevamente en Hernández Sport."
            )

        else:

            respuesta = (
                "¡Muchas gracias por visitar Hernández Sport! 😊"
            )

    # =====================================
    # RESPUESTA POR DEFECTO
    # =====================================

    else:

        respuesta = (
            "No entendí tu consulta.\n\n"
            "Podés preguntarme sobre:\n\n"
            "👟 Zapatillas\n"
            "👕 Remeras\n"
            "🩳 Shorts\n"
            "🧥 Camperas\n"
            "💲 Precios\n"
            "🎁 Promociones\n"
            "📦 Stock"
        )

    # Guardar conversación
    guardar_conversacion(
        mensaje,
        respuesta
    )

    return respuesta
