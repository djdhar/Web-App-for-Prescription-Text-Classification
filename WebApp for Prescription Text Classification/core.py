from PIL import Image
import numpy
import cv2
import tkinteropen as classify

def run(link, imageid):
    img = Image.open(link) 
    open_cv_image = cv2.imread(link)
    print(open_cv_image)
    img_gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    outputfilename = "output" + imageid + ".png"
    cv2.imwrite("static/output/" + outputfilename,img_gray)
    return(outputfilename)

def run_(link, imageid):
    img = Image.open(link) 
    open_cv_image = cv2.imread(link)
    print(open_cv_image)
    #img_otp = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    img_otp = classify.Classify(link)
    outputfilename = "output" + imageid + ".png"
    cv2.imwrite("static/output/" + outputfilename,img_otp)
    return(outputfilename)
