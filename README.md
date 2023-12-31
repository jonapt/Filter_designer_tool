# 2nd Order FDT (Filter designer tool)
It is a tool to facilitate the calculations for the design of second order sallen key filters with any desired optimization, either Butterworth, bessel, chebyshev.

Currently only 3 types of filters can be selected:

- Low pass
- High pass
- Band pass

The output folder contains the executable application, and the .py files contain the source code. 

## Diseño para filtro pasa bajas segundo orden Sallen Key
```python
def low_pass(c1,c2,a1,b1,fc):
    r1=((a1*c2)-((a1*a1*c2*c2)-(4*b1*c1*c2))**(1/2))/(4*np.pi*fc*c1*c2)
    r2=((a1*c2)+((a1*a1*c2*c2)-(4*b1*c1*c2))**(1/2))/(4*np.pi*fc*c1*c2)
    return [r1,r2]
```

## Diseño para filtro pasa altas segundo orden Sallen Key
```python
def high_pass(c,a1,b1,fc):
    r1=1/(np.pi*fc*c*a1)
    r2=a1/(4*np.pi*fc*c*b1)
    return [r1,r2]
```

## Diseño para filtro pasa banda Sallen Key 
```python
def pass_band_just(fm,c,q,ra):
    r=1/(2*np.pi*fm*c)
    g=(3*q-1)/q
    rf=(g-1)*ra
    return[r,rf,g]
```

## Diseño para filtro pasa banda angosta MFB (Multi feedback)

```python
def pass_band_mfb(Am,Fm,C,Q):
    R2=Q/(np.pi*Fm*C)
    R1=R2/(-2*Am)
    R3=(-Am*R1)/((2*Q**2)+Am)
    return(R2,R1,R3)
```




