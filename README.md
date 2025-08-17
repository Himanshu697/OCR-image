# OCR with Keyword Search (Hindi + English)

This project extracts text from images containing **Hindi and English** using EasyOCR.  
It also allows you to **search keywords** inside the extracted text, highlight them, and view results in **JSON format**.  
The app runs on a simple **Gradio web interface**.

---

## 📦 Installation

Make sure you have **Python 3.8+** installed. Then install dependencies:

```bash
pip install -r requirements.txt
If requirements.txt is not available, install manually:
pip install easyocr tensorflow numpy pandas opencv-python matplotlib gradio
