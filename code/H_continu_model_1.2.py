import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from matplotlib import cm

### INITIALIZE THE BZ -
M_mesh = 500
BZsize=M_mesh ## M x M BZ k-mesh
vec = [0,1]
oneDk=((np.arange(BZsize)/BZsize)-0.5)*2*np.pi#/unitcellsize ## put units of BZ from -pi/L to pi/L
kx, ky = np.meshgrid(oneDk,oneDk) # kx,ky: [#of row :len(oneDk), column: -pi/L to pi/L]
# ex) [[-pi/L,...,pi/L] [-pi/L,...,pi/L] [-pi/L,...,pi/L]...[-pi/L,...,pi/L]] (omit the line changing)
kvecs=np.column_stack((kx.flatten(),ky.flatten())) ## combine kvecs into an array.
# kx.flatten: [-pi/L,...,pi/L, -pi/L,...,pi/L, -pi/L,...,pi/L...-pi/L,...,pi/L] :50 * 50 = 2500
#kvecs =[[-pi/L, -pi/L] ,... ,[pi/L, -pi/L],......,[-pi/L, -pi/L+dk] ,... ,[pi/L, -pi/L+dk],......,] (omit the line changing)
#print('kvecs', kvecs)
N_k = len(kvecs)

TBpara = [-0.238*3.9,0.238,-0.45*0.153,0.03]
delta_d = 0.20 # eV
theta_rad = 2.0*np.arctan2(vec[0],vec[1])
theta_deg = 30*np.pi/180.0

def H_BdG(kvec,vec,Delta_0,theta,TBparameters):
    kx,ky=kvec[:,0],kvec[:,1]
    H=np.zeros((len(kvec),4,4), dtype="complex")    
    a=1.0
    alpha = np.arctan2(ky,kx)
    mu,t,tprime,g_0=TBparameters
    #xi = -mu -2.0*t*(np.cos(kx*a)+np.cos(ky*a))
    xi = -mu -t*(kx**2+ky**2)
    delta_k1 = delta_d*np.cos(2.0*alpha)
    delta_k2 = delta_d*np.cos(2.0*alpha-2.0*theta)

    ## Kinetic E term
    H[:, 0, 0] = 1.0*xi
    H[:, 1, 1] = -1.0*xi
    H[:, 2, 2] = 1.0*xi
    H[:, 3, 3] = -1.0*xi
    
    ## Gap term
    H[:, 0, 1] = delta_k1
    H[:, 1, 0] = np.conjugate(delta_k1)

    H[:,2,3]=delta_k2
    H[:,3,2]=np.conjugate(delta_k2)

    ## Coupling term between two layer
    H[:,0,2] =1.0*g_0
    H[:,1,3] =-1.0*g_0
    H[:,2,0] =1.0*g_0
    H[:,3,1] =-1.0*g_0

    return H

HBdG = H_BdG(kvecs,vec,delta_d,theta_deg,TBpara)

evals=LA.eigvalsh(HBdG,UPLO="U")

E1 = []
E2= []
E3 = []
E4 = []

for eigval in evals:
    energy1 = eigval[0]
    E1.append(energy1)
    energy2 = eigval[1]
    E2.append(energy2)
    energy3 = eigval[2]
    E3.append(energy3)
    energy4 = eigval[3]
    E4.append(energy4)
E1 = np.reshape(E1,(BZsize,BZsize))
E2 = np.reshape(E2,(BZsize,BZsize))
E3 = np.reshape(E3,(BZsize,BZsize))
E4 = np.reshape(E4,(BZsize,BZsize))
print('E1 max: ',E1.max())
print('E1 min: ',E1.min())
print('*'*50)
print('E2 max: ',E2.max())
print('E2 min: ',E2.min())
print('*'*50)
E5 = 0.5*(E1+E2)
print(E5.max())
print(E5.min())
print('*'*50)
'''
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
#bx = fig.add_subplot(212, projection='3d')

ax.plot_surface(kx, ky, E2)
ax.plot_surface(kx, ky, E3)
#bx.plot_surface(kx, ky, E1)
#bx.plot_surface(kx, ky, E4)
plt.show()
'''

'''
norm = cm.colors.Normalize(vmax=abs(E2).max(), vmin=-abs(E2).max())

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)

ims = ax.imshow(E2)
con = ax.contour(kx, ky, E2)
ax.set_xlim(-1.0*np.pi/unitcellsize, np.pi/unitcellsize)
ax.set_ylim(-1.0*np.pi/unitcellsize, np.pi/unitcellsize)
fig.colorbar(con, shrink=0.6, aspect=8)

plt.show()
'''

norm = cm.colors.Normalize(vmax=0, vmin= 0.1*E2.min())
plt.imshow(E2, cmap=cm.gist_heat, norm =norm)

#plt.xlim(-1.0*np.pi/unitcellsize, np.pi/unitcellsize)
#plt.ylim(-1.0*np.pi/unitcellsize, np.pi/unitcellsize)

#plt.xlim(-0.0, unitcellsize)
#plt.ylim(-0.0, unitcellsize)


plt.colorbar()
plt.show()












