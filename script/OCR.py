import cv2 as cv
import numpy
import pytesseract
import sys
from PIL import Image

# Path to tesseract exe file
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function for checking read values
def checkValues(string):
    for i in range(0, len(string)):
        if string[i] == "f" or string[i] == "F":
            string[i] = "7"
        elif string[i] == "l":
            string[i] = "1"
        elif string[i] == "O":
            string[i] = "0"

# List containing filenames passed as arguments
file_list = []

# Loop for adding filenames to list
for item in sys.argv[1:]:
    file_list.append(item)

# Loop for getting numbers from eps files
for item in file_list:
    try:
        # Opening file
        image = Image.open(item)

        # Converting eps file to png format
        image = image.convert("RGBA")

        # Changing file to matrix type
        image = numpy.array(image)

        # Converting file from RGB to Gray
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

        # Image thresholding
        gray = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)[1]

        # Reading text from image with tesseract
        text = pytesseract.image_to_string(gray)

        # Converting string to list
        listedText = list(text)

        checkValues(listedText)

        # Converting list with proper values to string
        text = "".join(listedText)

        # Printing text
        print("------------------------------")
        print(text)
        print("------------------------------")
    
    except FileNotFoundError:
        print(f"File \"{item}\" doesn't exist")