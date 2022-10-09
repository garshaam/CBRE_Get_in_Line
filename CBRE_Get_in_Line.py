#import file system and path functionality
import os
#import the ability to read a file as an image (necessary for pytesseract)
from PIL import Image
#import the ability to convert an image into text (reads text from the image)
import pytesseract

#cmdLocation is where the pytesseract command runs from.
def ReadImages(cmdLocation, imagePath):
    '''This function scans all images in imagePath for text using the pytesseract module and prints each message out.'''
    pytesseract.pytesseract.tesseract_cmd = cmdLocation

    #Loops through each file in the imagePath directory
    for i in range(len(os.listdir(imagePath))):
        #file is the combined filepath of the imagePath and file name (plus extension)
        file = os.path.join(imagePath, os.listdir(imagePath)[i])
        fileConvertedToImage = Image.open(file)
        #imageTesseracted is a string with all the image text
        imageTesseracted = pytesseract.image_to_string(fileConvertedToImage)
        print('File: ' + os.listdir(imagePath)[i])
        #Each message/block of text seems to be separated by two line breaks so we can split the list that way.
        tesseractedIntoList = imageTesseracted.split('\n\n')
        for e in range(len(tesseractedIntoList)):
            #If the string is empty, then it will return False as a boolean
            #This means that only non-empty strings will print
            if(tesseractedIntoList[e]):
                print(f'Message {e + 1}: ' + tesseractedIntoList[e])
        print("")

#currentPath is the current working directory. This makes it possible to call this program from outside.
currentPath = os.getcwd()
imageDirectory = ''
#The user inputs a value for the 
#If the current path is longer than 20 characters...
if (len(currentPath) > 40):
    imageDirectory = input(f"Which directory within {currentPath[0:20]}...{currentPath[-20:]} would you like to read from?")
else:
    imageDirectory = input(f"Which directory within ${currentPath} would you like to read from?")

#If the user leaves directory blank
if (not imageDirectory):
    imagePath = currentPath
    cmdLocation = input('Specify tesseract_cmd location. Leave blank for default (C:\\Program Files\\Tesseract-OCR\\tesseract.exe)')
    if (not cmdLocation):
        cmdLocation = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ReadImages(cmdLocation, imagePath)
#If the user enters a directory that does work 
elif (os.path.exists(os.path.join(currentPath, imageDirectory))):
    imagePath = os.path.join(currentPath, imageDirectory)
    cmdLocation = input('Specify tesseract_cmd location. Leave blank for default (C:\\Program Files\\Tesseract-OCR\\tesseract.exe)')
    if (not cmdLocation):
        cmdLocation = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ReadImages(cmdLocation, imagePath)
#if the user enters a directory that doesn't work
else:
    print("Directory invalid")