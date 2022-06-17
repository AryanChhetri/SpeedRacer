import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aryan\anaconda3\Library\bin\tesseract.exe'

def readscreenshot():
    img=cv2.imread('1.png')
    a=(pytesseract.image_to_string(img))
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    a=a[1:]
    a=a[:-1]
    b=""
    for i in a:
        if i=='{' or i=='|':
            b+='I'
        else:
            b+=i
    return b