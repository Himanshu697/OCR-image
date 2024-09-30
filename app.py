# Import the Library
import easyocr
import gradio as gr
import re
import numpy as np
import json

# Function to extract text from image using EasyOCR
def extract_text_easyocr(image):
    try:
        # Initialize the EasyOCR reader with Hindi and English language support
        reader = easyocr.Reader(['en', 'hi'])

        # Convert the PIL image to a NumPy array
        image_np = np.array(image)

        # Perform OCR on the uploaded image
        result = reader.readtext(image_np, detail=0)  # detail=0 returns only the text

        # Join the results in a single string
        extracted_text = ' '.join(result)
        return extracted_text
    except Exception as e:
        return f"Error in text extraction: {str(e)}"

# Function to handle keyword searching and highlighting
def highlight_keywords(text, keyword):
    try:
        if keyword:
            # Use regular expressions to find and highlight keyword matches (case-insensitive)
            highlighted_text = re.sub(f'({keyword})', r'<mark style="background-color: yellow;">\1</mark>', text, flags=re.IGNORECASE)
            if highlighted_text == text:
                return "No keyword match"  # Return specific message if no matches found
            return highlighted_text
        return text
    except Exception as e:
        return f"Error in keyword highlighting: {str(e)}"

# Process image to extract text, highlight keywords, and prepare JSON output
def process_image(image, keyword):
    try:
        # Step 1: Extract text from the image using EasyOCR
        extracted_text = extract_text_easyocr(image)

        # Step 2: Highlight the keyword in the extracted text (if no errors)
        if not extracted_text.startswith("Error"):
            highlighted_text = highlight_keywords(extracted_text, keyword)
        else:
            highlighted_text = "Error in highlighting"  # Generic error message if extraction fails

        # Create output dictionary for JSON
        output = {
            "extracted_text": extracted_text,
        }

        # Return plain text, JSON output, and highlighted text
        return extracted_text, json.dumps(output, ensure_ascii=False), highlighted_text  # ensure_ascii=False for Hindi characters
    except Exception as e:
        # Return plain text error, empty JSON output, and empty highlighted text
        return f"Error in processing: {str(e)}", json.dumps({"error": f"Error in processing: {str(e)}"}, ensure_ascii=False), ""

# Gradio Interface
interface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),  # Image input for OCR
        gr.Textbox(label="Enter Keyword to Search")  # Textbox input for keyword
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),  # Display the extracted text
        gr.Textbox(label="Json"),  # Show output in JSON format
        gr.HTML(label="Highlighted Text")  # Display the highlighted text
    ],
    title="Hindi and English OCR with Keyword Search",
    description="Upload an image to extract text in Hindi and English and search for specific keywords."
)

# Launch the Gradio interface
interface.launch(share=True)
