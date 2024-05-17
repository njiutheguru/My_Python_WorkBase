#from PIL import Image
#import pytesseract

def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    image_path = "sample.png"  # Replace with the path to your image file

    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("No text found.")