import gradio as gr
from chatbot import responder_usuario


# ==========================================================
# ESTILOS
# ==========================================================

css = """
.gradio-container{
    background:#111111;
}

footer{
    visibility:hidden;
}

h1{
    color:#22c55e;
    text-align:center;
}

h2{
    color:white;
    text-align:center;
}

.descripcion{
    text-align:center;
    font-size:18px;
    color:#DDDDDD;
}

.ejemplos{
    background:#1b1b1b;
    padding:15px;
    border-radius:10px;
    border:1px solid #22c55e;
    margin-top:10px;
    margin-bottom:15px;
}

button{
    background:#22c55e !important;
    color:white !important;
    font-weight:bold !important;
}

textarea{
    border:2px solid #22c55e !important;
}
"""


# ==========================================================
# CHATBOT
# ==========================================================

def responder(mensaje, historial):
    return responder_usuario(mensaje)


# ==========================================================
# INTERFAZ
# ==========================================================

with gr.Blocks(css=css) as demo:

    with gr.Column():

        # Logo
        gr.Image(
            value="logo.PNG",
            width=220,
            show_label=False,
            container=False
        )

        gr.Markdown("""
# 🏃 SportBot

## Asistente Virtual de Hernández Sport
""")

        gr.Markdown(
            """
<div class="descripcion">

Bienvenido 👋

Soy <b>SportBot</b>, un asistente basado en Inteligencia Artificial
especializado en la venta de ropa y calzado deportivo.

Estoy preparado para ayudarte a encontrar el producto ideal.

</div>
"""
        )

        gr.Markdown(
            """
<div class="ejemplos">

### 💚 Ejemplos de consultas

- 👟 Busco unas zapatillas Nike

- 👕 Necesito una remera Adidas

- 💲 ¿Cuánto cuesta?

- 🎁 ¿Hay promociones?

- 📦 ¿Hay stock?

</div>
"""
        )

        gr.ChatInterface(
            fn=responder,
            chatbot=gr.Chatbot(
                height=430,
                label="Conversación"
            ),
            textbox=gr.Textbox(
                placeholder="Escribí tu consulta aquí...",
                label="Consulta"
            )
        )

        gr.Markdown(
            """
---

<center>

💚 <b>Hernández Sport</b>

SportBot v1.0

Proyecto de Procesamiento del Habla - Inteligencia Artificial Conversacional

</center>
"""
        )

demo.launch()