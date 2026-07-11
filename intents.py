"""
Detección de intenciones para SportBot
"""

INTENTS = {

    "saludo": [
        "hola",
        "buenas",
        "buen día",
        "buenas tardes",
        "buenas noches"
    ],

    "presentarse": [
        "me llamo",
        "soy",
        "mi nombre es"
    ],

    "buscar_producto": [
        "busco",
        "quiero",
        "necesito",
        "estoy buscando"
    ],

    "consultar_precio": [
        "precio",
        "cuánto cuesta",
        "cuanto cuesta",
        "valor"
    ],

    "consultar_stock": [
        "hay",
        "disponible",
        "stock",
        "tienen"
    ],

    "consultar_promocion": [
        "promoción",
        "promocion",
        "descuento",
        "oferta"
    ],

    "recomendar_producto": [
        "recomendás",
        "recomiendas",
        "qué me recomendás",
        "que me recomendas"
    ],

    "confirmar_compra": [
        "lo compro",
        "lo quiero",
        "me lo llevo",
        "comprar"
    ],

    "despedida": [
        "gracias",
        "hasta luego",
        "nos vemos",
        "adiós",
        "adios"
    ]
}


def detectar_intent(texto):

    texto = texto.lower()

    for intent, palabras in INTENTS.items():

        for palabra in palabras:

            if palabra in texto:

                return intent

    return "desconocido"
