# utils/image_module.py
import easyocr
from PIL import Image

# Initialize easyocr reader (default is English)
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """Extract text from the given image file using easyocr."""
    try:
        # Use easyocr to extract text from the image
        result = reader.readtext(image_path)
        
        # Combine all text results into a single string
        text = ' '.join([text[1] for text in result])
        
        return text
    
    except Exception as e:
        return str(e)
