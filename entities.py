import spacy

# Cargar el modelo de español
nlp = spacy.load("es_core_news_md")

# Marcas disponibles
MARCAS = [
    "Nike",
    "Adidas",
    "Puma",
    "New Balance",
    "Under Armour"
]

# Categorías de productos
PRODUCTOS = [
    "zapatillas",
    "remera",
    "short",
    "campera"
]

# Colores
COLORES = {
    "negro": ["negro", "negra", "negros", "negras"],
    "blanco": ["blanco", "blanca", "blancos", "blancas"],
    "azul": ["azul", "azules"],
    "gris": ["gris", "grises"],
    "rojo": ["rojo", "roja", "rojos", "rojas"]
}

# Deportes
DEPORTES = [
    "running",
    "fútbol",
    "gimnasio",
    "tenis"
]


def extraer_entidades(texto):
    """
    Extrae información relevante del mensaje del usuario.
    """

    doc = nlp(texto)

    entidades = {
        "nombre": None,
        "producto": None,
        "marca": None,
        "color": None,
        "talle": None,
        "deporte": None,
        "presupuesto": None
    }

    texto_minuscula = texto.lower()

    # ------------------------
    # Detectar nombre
    # ------------------------

    if "me llamo " in texto_minuscula:
        nombre = texto.split("me llamo", 1)[1].strip()
        entidades["nombre"] = nombre.title()

    elif "mi nombre es " in texto_minuscula:
        nombre = texto.split("mi nombre es", 1)[1].strip()
        entidades["nombre"] = nombre.title()

    elif texto_minuscula.startswith("soy "):
        nombre = texto.split("soy", 1)[1].strip()
        entidades["nombre"] = nombre.title()

    # Respaldo utilizando spaCy
    if entidades["nombre"] is None:
        for entidad in doc.ents:
            if entidad.label_ == "PER":
                entidades["nombre"] = entidad.text
                break

    # ------------------------
    # Detectar marca
    # ------------------------

    for marca in MARCAS:
        if marca.lower() in texto_minuscula:
            entidades["marca"] = marca
            break

    # ------------------------
    # Detectar producto
    # ------------------------

    for producto in PRODUCTOS:
        if producto.lower() in texto_minuscula:
            entidades["producto"] = producto
            break

    # ------------------------
    # Detectar color
    # ------------------------

    for color, variantes in COLORES.items():
        for variante in variantes:
            if variante in texto_minuscula:
                entidades["color"] = color
                break

    # ------------------------
    # Detectar deporte
    # ------------------------

    for deporte in DEPORTES:
        if deporte.lower() in texto_minuscula:
            entidades["deporte"] = deporte
            break

    # ------------------------
    # Detectar talle
    # ------------------------

    for token in doc:

        if token.like_num:

            try:

                numero = int(token.text)

                if 35 <= numero <= 50:
                    entidades["talle"] = numero

            except ValueError:
                pass

    return entidades