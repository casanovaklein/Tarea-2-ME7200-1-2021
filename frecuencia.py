#importar librerias
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft, fftfreq
from numpy import mean, sqrt, square


rod_sin_falla = sio.loadmat('sano-C-1.mat')['Channel_1']
rod_con_falla_pist_ext = sio.loadmat('pista_externa-C-1.mat')['Channel_1']
rod_con_falla_pist_int = sio.loadmat('pista_interna-C-1.mat')['Channel_1']
rod_con_falla_bolas = sio.loadmat('bolas-C-1.mat')['Channel_1']
rod_con_falla_comb = sio.loadmat('combinacion-C-1.mat')['Channel_1']

F_s = 200_000
dt = 1/F_s
N = len(rod_sin_falla)
t = np.linspace(0, dt*(N-1), N)

#calcular parametros 
L=80_000 #largo de los segmentos
l=0 #overlap
Nt=math.floor((N-l)/(L-l)) #total de tramos
nb=8 #numero de bandas

En=np.zeros((Nt,nb))
Eo=np.zeros((Nt,nb))
Ei=np.zeros((Nt,nb))
Eb=np.zeros((Nt,nb))
Ec=np.zeros((Nt,nb))

for i in range(1,Nt+1):
    inicio=(i-1)*L-(i-1)*l+1
    fin=i*L-(i-1)*l

    Fn = fft(rod_sin_falla[inicio:fin,0])[0:int(L/2)]/(L/2)
    Fo = fft(rod_con_falla_pist_ext[inicio:fin,0])[0:int(L/2)]/(L/2)
    Fi = fft(rod_con_falla_pist_int[inicio:fin,0])[0:int(L/2)]/(L/2)
    Fb = fft(rod_con_falla_bolas[inicio:fin,0])[0:int(L/2)]/(L/2)
    Fc = fft(rod_con_falla_comb[inicio:fin,0])[0:int(L/2)]/(L/2)
    frq = fftfreq(L,dt)[0:int(L/2)] 
    
    Lb=int(L/2/nb)
    for k in range(1,nb+1):
        inicio=(Lb//30)*(k-1)+1
        fin=k*(Lb//30)
        En[i-1][k-1]=mean(abs(Fn[inicio:fin]))
        Eo[i-1][k-1]=mean(abs(Fo[inicio:fin]))
        Ei[i-1][k-1]=mean(abs(Fi[inicio:fin]))
        Eb[i-1][k-1]=mean(abs(Fb[inicio:fin]))
        Ec[i-1][k-1]=mean(abs(Fc[inicio:fin]))

f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col',figsize=(9,6))

ax1.plot(En[:,0])
ax1.plot(Eo[:,0])
ax1.plot(Ei[:,0])
ax1.plot(Eb[:,0])
ax1.plot(Ec[:,0])
ax1.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax1.set_title('Banda 1', fontsize=14)

ax2.plot(En[:,1])
ax2.plot(Eo[:,1])
ax2.plot(Ei[:,1])
ax2.plot(Eb[:,1])
ax2.plot(Ec[:,1])
ax2.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax2.set_title('Banda 2', fontsize=14)



ax3.plot(En[:,2])
ax3.plot(Eo[:,2])
ax3.plot(Ei[:,2])
ax3.plot(Eb[:,2])
ax3.plot(Ec[:,2])
ax3.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax3.set_title('Banda 3', fontsize=14)

ax4.plot(En[:,3])
ax4.plot(Eo[:,3])
ax4.plot(Ei[:,3])
ax4.plot(Eb[:,3])
ax4.plot(Ec[:,3])
ax4.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax4.set_title('Banda 4', fontsize=14)


f2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, sharex='col',figsize=(9,6))
ax5.plot(En[:,4])
ax5.plot(Eo[:,4])
ax5.plot(Ei[:,4])
ax5.plot(Eb[:,4])
ax5.plot(Ec[:,4])
ax5.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax5.set_title('Banda 5', fontsize=14)

ax6.plot(En[:,5])
ax6.plot(Eo[:,5])
ax6.plot(Ei[:,5])
ax6.plot(Eb[:,5])
ax6.plot(Ec[:,5])
ax6.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax6.set_title('Banda 6', fontsize=14)

ax7.plot(En[:,6])
ax7.plot(Eo[:,6])
ax7.plot(Ei[:,6])
ax7.plot(Eb[:,6])
ax7.plot(Ec[:,6])
ax7.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax7.set_title('Banda 7', fontsize=14)

ax8.plot(En[:,7])
ax8.plot(Eo[:,7])
ax8.plot(Ei[:,7])
ax8.plot(Eb[:,7])
ax8.plot(Ec[:,7])
ax8.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax8.set_title('Banda 8', fontsize=14)

f1.show()
f2.show()
