import numpy as np
import matplotlib.pyplot as plt
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

mu = -1 #eV
g = 0.03 #eV
deltad = 0.04 #eV
theta = 9.53

def alpha(kx, ky):
  a = np.arctan2(kx,ky)
  return a

def gap1(kx, ky):
  gp1 = deltad*np.cos(2*alpha(kx, ky))
  return gp1

def gap2(kx, ky):
  gp2 = deltad*np.cos(2*alpha(kx, ky) -2*theta)
  return gp2 

def E1(kx, ky):
  Energy1 = ((gap1(kx, ky))**2 + (gap2(kx, ky))**2)/2  
  return Energy1

def Xi(kx, ky):
  xi = -2*(np.cos(kx)+np.cos(ky))-mu
  return xi  

def Dk(kx, ky):
  D = np.sqrt((((gap1(kx, ky))**2 - (gap2(kx, ky))**2)**2/4)+g**2*((gap1(kx, ky))**2 + (gap2(kx, ky))**2 + 4*(Xi(kx, ky)**2))-2*g**2*(gap1(kx, ky))*(gap2(kx, ky)))
  return D

def Ep(kx, ky):
  PositiveEnergy = np.sqrt(E1(kx, ky)+(Xi(kx, ky)**2)+g**2+Dk(kx, ky))   
  return PositiveEnergy

def En(kx, ky):
  NegativeEnergy = np.sqrt(E1(kx, ky)+(Xi(kx, ky)**2)+g**2-Dk(kx, ky))     
	return NegativeEnergy

deltax = 0.05
 
kx = np.arange(-3.0,3.0,0.1) #그리프의 x 범위 지정
ky = np.arange(-3.0,3.0,0.1) #그래프의 y 범위 지정
X,Y = meshgrid(kx, ky) # grid of point
Zn = En(X, Y) # evaluation of the function on the grid
Zp = Ep(X, Y)

#En 그래프
im_n = imshow(Zn,cmap=cm.RdBu)     # drawing the function   
cset_n = contour(Zn,np.arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)   # adding the Contour lines with labels
clabel(cset_n,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im_n)    # adding the colobar on the right
# latex fashion title
title('$Energy_2$')    # latex fashion title
show()

#Ep그래프
im_p = imshow(Zp,cmap=cm.RdBu)
cset_p = contour(Zp,np.arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset_p,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im_p)
title('$Energy_1$')
show()
