import streamlit as st
from gradio_client import Client

st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

st.title("🎨 AI Image Generator")
st.write("Enter a prompt to generate an image.")

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                client = Client("black-forest-labs/FLUX.1-schnell")

                result = client.predict(
                    prompt=prompt,
                    api_name="/infer"
                )

                image_path = result[0]

                st.image(image_path, caption="Generated Image", use_container_width=True)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")