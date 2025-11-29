import numpy as np
import matplotlib.pyplot as plt
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

import BdG_H
from BdG_H import En, alpha, Ep

deltax = np.pi/50

kx = np.arange(-np.pi,np.pi,deltax) #그리프의 x 범위 지정
ky = np.arange(-np.pi,np.pi,deltax) #그래프의 y 범위 지정
X,Y = meshgrid(kx, ky) # grid of point
Zn = En(X, Y) # evaluation of the function on the grid
Zp = Ep(X, Y)
#A = alpha(X, Y)

#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#ax.plot_surface(X, Y, A, cmap=plt.cm.YlGnBu_r)
#title('$이게뭐지?')
#show()

norm1 = cm.colors.Normalize(vmax=0.1*Zp.max(), vmin= 0.0)
im_p = imshow(Zp,cmap=cm.gist_heat, norm =norm1)

cset_p = contour(Zp,np.arange(-np.pi,np.pi,0.001),linewidths=2)
#clabel(cset_p,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im_p)
title('$Energy_1$')
show()

norm_2 = cm.colors.Normalize(vmax=0.1*Zn.max(), vmin= 0.0)
im_n = imshow(Zn,cmap=cm.gist_heat,norm=norm_2)     # drawing the function   
cset_n = contour(Zn)   # adding the Contour lines with labels
#clabel(cset_n,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im_n)    # adding the colobar on the right
# latex fashion title
title('$Energy_2$')    # latex fashion title
show()