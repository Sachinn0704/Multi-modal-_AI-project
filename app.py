from utils.image_module import process_image
from utils.text_module import process_text
from utils.audio_module import extract_text_from_audio




def main():
    print("Select a file (Image, Text, or Audio):")
    file_type = input().lower()
    
    if file_type == 'image':
        print("Enter the path to the image file:")
        image_path = input()
        result = process_image(image_path)
        print("Image result:", result)
    
    elif file_type == 'text':
        print("Enter the path to the text file:")
        text_path = input()
        result = process_text(text_path)
        print("Text result:", result)
    
    elif file_type == 'audio':
        print("Enter the path to the audio file:")
        audio_path = input()
        result = extract_text_from_audio(audio_path)
        print("Audio result:", result)

if __name__ == "__main__":
    main()
