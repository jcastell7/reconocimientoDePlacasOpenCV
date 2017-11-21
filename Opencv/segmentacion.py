import numpy as np
import cv2

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
    cv2.imwrite("k/k.bmp",K)
    k=cv2.imread("k/k.bmp")
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
        if p[2]>=0.095*A and p[2]<=0.15*A and p[3]>=0.46*L and p[3]<=0.67*L:
            Box[q]=p
            q=q+1 
    Box=np.array(Box,dtype = np.uint32)
    img=cv2.imread(rutaImagenRecortada)
    
    for i in range(0,6):
        let=img[Box[i*2,1]:Box[i*2,1]+Box[i*2,3],Box[i*2,0]:Box[i*2,0]+Box[i*2,2]]
        cv2.imwrite("letras/"+str(i)+" - letras.jpg",let)
segmentacion("placas procesadas/procesada 3.jpg")