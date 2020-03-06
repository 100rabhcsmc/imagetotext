import pytesseract
from PIL import Image

from pytesseract import image_to_string

# pytesseract.pytesseract.tesseract_cmd=r"E:\\python\\textimage\\tesseract\\tesseract.exe"

img=Image.open("E:\\python\\textimage\\einstein.jpg")

text=image_to_string(img)
print(text)
