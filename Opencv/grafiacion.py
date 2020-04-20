import matplotlib.pyplot as plt
import segmentacion

BW1,BOX=segmentacion.segmentacion("C:\Users\juan\My Documents\LiClipse Workspace\placas\image\procesado2.jpg")
LETRA1=BW1[BOX[0,1]:BOX[0,1]+BOX[0,3],BOX[0,0]:BOX[0,0]+BOX[0,2]]
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
