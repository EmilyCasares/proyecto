# Generador de historias con IA en Python

Aplicación hecha con **Python + Streamlit** para crear historias en español usando la API de OpenAI.

> Nota: esta app **genera historias**; no es una app de recomendaciones.

## Requisitos

- Python 3.10+
- Clave de API de OpenAI

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración

Variables de entorno:

```bash
export OPENAI_API_KEY="tu_api_key"
# Opcional: cambiar modelo por defecto (gpt-4.1-mini)
export OPENAI_MODEL="gpt-4.1-mini"
```

## Ejecutar

```bash
streamlit run app.py
```

Luego abre la URL local que muestra Streamlit (normalmente `http://localhost:8501`).

## Funciones incluidas

- Parámetros narrativos: protagonista, género, tono, extensión y detalles opcionales.
- Opción para incluir título automáticamente.
- Control de creatividad (temperatura).
- Descarga de la historia generada en `.txt`.
