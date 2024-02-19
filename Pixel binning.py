import cv2
import time

fp="../../Downloads/Bits_Clock_tower.png"
image=cv2.imread(fp)
new=image.copy()
h,w,n=new.shape
new2=cv2.resize(image,(600,600))
cv2.imshow('Before',new2)
    
for x in range(0,h-1,2):
    for y in range(0,w-1,2):
        p1=new[x,y]
        p2=new[x+1,y]
        p3=new[x,y+1]
        p4=new[x+1,y+1]
        r=int(p1[0])+int(p2[0])+int(p3[0])+int(p4[0])
        g=int(p1[1])+int(p2[1])+int(p3[1])+int(p4[1])
        b=int(p1[2])+int(p2[2])+int(p3[2])+int(p4[2])
        p=[r,g,b]
        p[0]=p[0]//4
        p[1]=p[1]//4
        p[2]=p[2]//4

        new[x,y]=p.copy()
        new[x+1,y]=p.copy()
        new[x,y+1]=p.copy()
        new[x+1,y+1]=p.copy()

new=cv2.resize(new,(600,600))
cv2.imshow('After',new)
cv2.moveWindow('After',650,0)

'''time.sleep(10)
cv2.destroyAllWindows()'''
