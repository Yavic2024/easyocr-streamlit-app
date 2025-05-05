import streamlit as st
from PIL import Image
import base64
import os
import easyocr
import numpy as np

# Initialize EasyOCR once (outside function for performance)
reader = easyocr.Reader(['en', 'fr'], gpu=True)

def clean_easyocr_output(results):
    # Sort by top-to-bottom, then left-to-right (based on bounding box coordinates)
    results.sort(key=lambda r: (r[0][0][1], r[0][0][0]))
    lines = [text for (_, text, _) in results]
    return " ".join(lines)  # or use "\n".join(lines) if needed

def query_easyocr(image: Image.Image):
    image_np = np.array(image)
    try:
        results = reader.readtext(image_np)
        if results:
            return clean_easyocr_output(results)
        else:
            return "[No text detected]"
    except Exception as e:
        return f"[ERROR] EasyOCR failed: {str(e)}"


# Page configuration
st.set_page_config(
    page_title="Simple Streamlit EasyOCR App",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and logo
logo_path = os.path.join(os.path.dirname(__file__), "assets", "myOCRicon.png")
st.markdown("""
    # <img src="data:image/png;base64,{}" width="50" style="vertical-align: -12px;"> EasyOCR App (Local Mode)
""".format(base64.b64encode(open(logo_path, "rb").read()).decode()), unsafe_allow_html=True)

# Clear button
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extract printed text from images using EasyOCR — all done locally!</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar upload
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'], help="Upload a PNG, JPG, or JPEG image for OCR.")

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Running EasyOCR..."):
                try:
                    # Resize for performance if needed (optional)
                    image = image.resize((1024, 1024))
                    result = query_easyocr(image)
                    st.session_state['ocr_result'] = result
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")

# Results display
if 'ocr_result' in st.session_state:
    st.markdown("### Herewith the extracted text:")
    st.success(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results here.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using EasyOCR by Victor N. A. Yabili")
