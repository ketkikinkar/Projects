n = []
import cv2
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread('14.jpg')
original = img
#original = cv2.cvtColor(original,cv2.COLOR_BGR2RGB)
cv2.imshow('original',original)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)

print(boxes)

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        len(b)

        if len(b) == 12:
             m = b[11:12]
             m = ' '.join(m)
             translator = Translator()
             l = translator.translate(m, src='en', dest='de')
             m = l.text
             b.insert(11,m)
             print(b)
             '''mytext = b
             n.append(m)
             k = len(n)'''
             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
             cv2.rectangle(img, (x, y), (w + x, h + y), (255, 0, 0), 1)
             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

cv2.imshow('Result', img)
cv2.waitKey(0)