import numpy as np
import cv2

def segmentacion2(ruta):
    imagen=cv2.imread(ruta)
    imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgGris,127,255,cv2.THRESH_BINARY)
    S,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    box=[]
    num=len(contours)
    [L,A]=thresh.shape
    for j in range (0,num):
        l=cv2.boundingRect(contours[j])[2]
        a=cv2.boundingRect(contours[j])[3]
        if l>=0.095*A and l<=0.15*A and a>=0.46*L and a<=0.54*L:
            box[j]=cv2.boundingRect(contours[j])
    print box
    for i in range(0,num):
        let=imagen[box[i,1]:box[i,1]+box[i,3],box[i,0]:box[i,0]+box[i,2]]
        cv2.imwrite(str(i)+" - letras.jpg",let)
        
segmentacion2("4 - procesada.jpg")