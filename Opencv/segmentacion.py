import numpy as np
import cv2
import matplotlib.pyplot as plt
import preprocesamiento as pre

def segmentacion(rutaImagenRecortada):
    A=cv2.imread(rutaImagenRecortada)
    [fil,col,cap]=A.shape

    rgB=A[:,:,0]
    rGb=A[:,:,1]
    Rgb=A[:,:,2]

    R=Rgb/255.0
    G=rGb/255.0
    B=rgB/255.0

    K=np.zeros((fil,col))
    for i in range(0,fil):
        for j in range(0,col):
            MAX=max(R[i,j],G[i,j],B[i,j])
            K[i,j]=1-MAX
    cv2.imwrite("k.bmp",K)
    k=cv2.imread("k.bmp")
    BW1=cv2.Laplacian(k,cv2.CV_8UC1)
    Image=BW1[:,:,0]+BW1[:,:,1]+BW1[:,:,2]
    ret,thresh=cv2.threshold(Image,0,255,0)
    S,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt=contours[:]
    num=len(cnt)
    box=np.zeros((num,4))
    for j in range (0,num):
        box[j,:]=cv2.boundingRect(cnt[j])
        
    Box=np.zeros((20,4))
    [L,A]=thresh.shape
    q=0
    print[L,A]
    for j in range(0,num):
        p=box[j,:]
        if p[2]>=90 and p[2]<=130 and p[3]>=220 and p[3]<=240:
            Box[q]=p
            q=q+1
    
    BOX=np.zeros((6,4))
    num=len(Box)
    q=0
    for j in range(0,num):
        if j%2==0 and j<11:
            Box[q]=Box[j]
            q=q+1   
    Box=np.array(Box,dtype = np.uint32)
    img=cv2.imread("3 - procesada.jpg")

    for i in range(0,19):
        let=img[Box[i,1]:Box[i,1]+Box[i,3],Box[i,0]:Box[i,0]+Box[i,2]]
        cv2.imwrite(str(i)+"letras.jpg",let)

"""
    
    LETRA2=BW1[BOX[1,1]:BOX[1,1]+BOX[1,3],BOX[1,0]:BOX[1,0]+BOX[1,2]]
    LETRA3=BW1[BOX[2,1]:BOX[2,1]+BOX[2,3],BOX[2,0]:BOX[2,0]+BOX[2,2]]
    NUM1=BW1[BOX[3,1]:BOX[3,1]+BOX[3,3],BOX[3,0]:BOX[3,0]+BOX[3,2]]
    NUM2=BW1[BOX[4,1]:BOX[4,1]+BOX[4,3],BOX[4,0]:BOX[4,0]+BOX[4,2]]
    NUM3=BW1[BOX[5,1]:BOX[5,1]+BOX[5,3],BOX[5,0]:BOX[5,0]+BOX[5,2]]
    plt.subplot(161),plt.imshow(LETRA1*255)
    plt.subplot(162),plt.imshow(LETRA2*255)
    plt.subplot(163),plt.imshow(LETRA3*255)
    plt.subplot(164),plt.imshow(NUM1*255)
    plt.subplot(165),plt.imshow(NUM2*255)
    plt.subplot(166),plt.imshow(NUM3*255)
    plt.show()
"""
segmentacion("3 - procesada.jpg")