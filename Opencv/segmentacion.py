import numpy as np
import cv2

def segmentacion(rutaImagenCortada):
    A=cv2.imread(rutaImagenCortada)
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
    
    BW1=cv2.Laplacian(K,cv2.CV_8UC1)
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
    for j in range(0,num):
        p=box[j,:]
        if p[3]>=0.4*L and p[3]<=0.7*L and p[2]>=0.08*A and p[2]>=0.17*A:
            Box[q]=p
            q=q+1
    BOX=np.zeros((6,4))
    num=len(Box)
    q=0
    for j in range(0,num):
        if j%2==0 and j<11:
            Box[q]=Box[j]
            q=q+1

    return BW1
