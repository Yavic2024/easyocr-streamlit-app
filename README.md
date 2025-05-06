# EasyOCR Streamlit App

This project leverages **EasyOCR** and **Streamlit** to build an AI-powered Text Extractor app capable of performing optical character recognition (OCR) and extracting structured text from images. Designed for local execution, the application runs significantly faster on GPU-enabled systems, enabling efficient and accurate text extraction directly from image inputs.
---

## Features

- Upload images in **PNG**, **JPG**, or **JPEG** format.
- Extract printed text from images using **EasyOCR**.
- Supports GPU acceleration for faster processing (if available).
- Simple and intuitive user interface.
- Local processing ensures privacy and security.

---

## Installation and Setup

### **1. Prerequisites**

Ensure you have the following installed on your system:
- **Python 3.8 or later**: [Download Python](https://www.python.org/downloads/)
- **pip**: Comes pre-installed with Python. Verify by running:
  ```
  pip --version
 ---
### 2. Navigate to the app directory:
```cd <your destination folder>```

If you downloaded the app as a ZIP file:
1. Extract the ZIP file.
2. Navigate to the extracted folder.

---
### **3. Create a Virtual Environment (Optional but Recommended)**
To avoid dependency conflicts, create a virtual environment: 

```python -m venv venv```
 Activate the virtual environment:
 - **Windows**:
 ```venv\Scripts\activate```
 - **Mac/Linux**:   
 ```source venv/bin/activate```
 ---
### **4. Install Dependencies**
Install the required Python packages using pip. 
If a requirements.txt file is not available, manually install the dependencies:

 ```pip install streamlit easyocr pillow numpy ```:

 ```pip install -r requirements.txt```

 ---
### **5. Add GPU Support (Optional)**
If you want to use GPU acceleration for EasyOCR:
1. Install PyTorch with GPU support. Follow the instructions on the [PyTorch website](https://pytorch.org/get-started/locally/).
2. Verify GPU support: 
```python import torch print(torch.cuda.is_available())```
 ---
 ### **6. Run the App** Start the Streamlit app by running:
 This following command line will open the app in your default web browser. If it doesn't, copy and paste the URL shown in the terminal 
 (e.g., http://localhost:8501) into your browser.
 
 ```streamlit run app.py``` 
 
 ## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.


