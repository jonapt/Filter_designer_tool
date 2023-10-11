import numpy as np
import math
#Diseño para filtro pasa bajas segundo orden Sallen Key
def low_pass(c1,c2,a1,b1,fc):
    r1=((a1*c2)-((a1*a1*c2*c2)-(4*b1*c1*c2))**(1/2))/(4*np.pi*fc*c1*c2)
    r2=((a1*c2)+((a1*a1*c2*c2)-(4*b1*c1*c2))**(1/2))/(4*np.pi*fc*c1*c2)
    return [r1,r2]

## Diseño para filtro pasa altas segundo orden Sallen Key
def high_pass(c,a1,b1,fc):
    r1=1/(np.pi*fc*c*a1)
    r2=a1/(4*np.pi*fc*c*b1)
    return [r1,r2]

## Diseño para filtro pasa banda Sallen Key 
def pass_band_just(fm,c,q,ra):
    r=1/(2*np.pi*fm*c)
    g=(3*q-1)/q
    rf=(g-1)*ra
    a=g/(3-g)
    return[r,rf,g,a]

## Diseño para filtro pasa banda angosta MFB (Multi feedback)

def pass_band_mfb(Am,Fm,C,Q):
    R2=Q/(np.pi*Fm*C)
    R1=R2/(-2*Am)
    R3=(-Am*R1)/((2*Q**2)+Am)
    return(R2,R1,R3)