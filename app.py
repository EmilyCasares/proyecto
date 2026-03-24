import os
from typing import Final

import streamlit as st
from openai import OpenAI

DEFAULT_MODEL: Final[str] = "gpt-4.1-mini"
MODEL_ENV_VAR: Final[str] = "OPENAI_MODEL"


st.set_page_config(page_title="Generador de historias con IA", page_icon="📚", layout="centered")
st.title("📚 Generador de historias con IA")
st.caption("Aplicación en Python para crear historias originales en español (no es un recomendador).")


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("No se encontró OPENAI_API_KEY. Configura la variable antes de continuar.")
    return OpenAI(api_key=api_key)


def get_model() -> str:
    return os.getenv(MODEL_ENV_VAR, DEFAULT_MODEL)


def build_prompt(
    protagonista: str,
    genero: str,
    tono: str,
    extension: str,
    detalle: str,
    incluir_titulo: bool,
) -> str:
    titulo_instr = "Incluye un título creativo al inicio." if incluir_titulo else "No uses título."
    return (
        "Eres un escritor creativo experto en narrativa. "
        "Escribe una historia en español con estas características:\n"
        f"- Protagonista: {protagonista}\n"
        f"- Género: {genero}\n"
        f"- Tono: {tono}\n"
        f"- Extensión: {extension}\n"
        f"- Detalles obligatorios: {detalle or 'Ninguno'}\n"
        f"- Formato: {titulo_instr}\n\n"
        "La historia debe tener inicio, conflicto y cierre. "
        "Usa un estilo envolvente y evita listas."
    )


def generate_story(client: OpenAI, model: str, prompt: str, temperature: float) -> str:
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=temperature,
    )
    return response.output_text.strip()


if "last_story" not in st.session_state:
    st.session_state.last_story = ""

with st.form("story_form"):
    protagonista = st.text_input("Protagonista", "Luna, una exploradora espacial")
    genero = st.selectbox("Género", ["Fantasía", "Ciencia ficción", "Misterio", "Aventura", "Terror"])
    tono = st.selectbox("Tono", ["Inspirador", "Oscuro", "Divertido", "Épico", "Melancólico"])
    extension = st.selectbox("Extensión", ["Corta (150-250 palabras)", "Media (300-500 palabras)", "Larga (600-900 palabras)"])
    detalle = st.text_area("Detalles opcionales", placeholder="Ejemplo: incluye un dragón azul y una ciudad flotante")
    incluir_titulo = st.checkbox("Incluir título", value=True)
    creativity = st.slider("Creatividad", min_value=0.2, max_value=1.2, value=0.9, step=0.1)
    submitted = st.form_submit_button("Generar historia")

if submitted:
    try:
        client = get_client()
        model = get_model()
        prompt = build_prompt(
            protagonista=protagonista,
            genero=genero,
            tono=tono,
            extension=extension,
            detalle=detalle,
            incluir_titulo=incluir_titulo,
        )

        with st.spinner("Creando historia..."):
            story = generate_story(client=client, model=model, prompt=prompt, temperature=creativity)

        if not story:
            st.warning("No se pudo generar una historia en este intento. Intenta de nuevo.")
        else:
            st.session_state.last_story = story
            st.success(f"Historia generada con el modelo: {model}")
    except Exception as exc:
        st.error(f"Ocurrió un error al generar la historia: {exc}")

if st.session_state.last_story:
    st.subheader("Tu historia")
    st.write(st.session_state.last_story)
    st.download_button(
        label="Descargar historia (.txt)",
        data=st.session_state.last_story,
        file_name="historia_ia.txt",
        mime="text/plain",
    )
