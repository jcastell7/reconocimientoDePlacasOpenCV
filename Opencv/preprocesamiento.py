import numpy as np
import cv2

def preprocesamiento(ruta):
    imagen=cv2.imread(ruta)
    rgB=np.matrix(imagen[:,:,0])
    rGb=np.matrix(imagen[:,:,1])
    Rgb=np.matrix(imagen[:,:,2])
    img=cv2.absdiff(rGb,rgB)
    [fil,col]=img.shape
    for i in range(0,fil):
        for j in range(0,col):
            if img[i,j]<80:
                img[i,j]=0
    for i in range(0,fil):
        for j in range(0,col):
            if img[i,j]>0:
                img[i,j]=1
    se=np.ones((50,50), np.uint8)
    se2=np.ones((10,10),np.uint8)
    closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,se)
    dilation=cv2.dilate(closing, se2,1)
    S,contours,hierarchy=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt=contours[:]
    num=len(cnt)
    box=np.zeros((num,4))
    for i in range(0,num):
        box[i,:]=cv2.boundingRect(cnt[i])
        L=np.zeros((num,4))
        Max=[0,0]
        for i in range (0,num):
            L[i,:]=box[i]
            if L[i,2]>Max[1]:
                Max=[i,L[i,2]]
    BOX=box[Max[0],:]
    BOX=np.array(BOX,dtype = np.uint32)
    b=imagen[BOX[1]:BOX[1]+BOX[3],BOX[0]:BOX[0]+BOX[2],:]
    cv2.imwrite("placas procesadas/procesada "+ruta,b)
preprocesamiento("5.jpg")