#importar librerías
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import kurtosis, skew
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

# Ploteando los 5 graficos
"""
fig_1, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5, ncols=1, sharex=True, sharey=True)

ax1.plot(t, rod_sin_falla)
ax1.set_title('rodamiento sin falla')
ax1.legend()

ax2.plot(t, rod_con_falla_pist_ext)
ax2.set_title('rodamiento con falla pista externa')
ax2.legend()

ax3.plot(t, rod_con_falla_pist_int)
ax3.set_title('rodamiento con falla pista interna')
ax3.set_ylabel('Aceleración ' "$(m/s^2)$", fontsize=14)
ax3.legend()

ax4.plot(t, rod_con_falla_bolas)
ax4.set_title('rodamiento con falla en las bolas')
ax4.legend()

ax5.plot(t, rod_con_falla_comb)
ax5.set_title('rodamiento con fallas combinadas')
ax5.legend()
ax5.set_xlabel('TiemP_falla_ext (s)', fontsize=14)

fig_1.show()

"""


#calcular parametros P_falla_extr tramos
L=50_000 #largo de los segmentos
l=0 #overlap
Nt=math.floor((N-l)/(L-l)) #total de tramos


#inicializar matrices con parametros
P_normal=np.zeros((Nt,8))
P_falla_ext=np.zeros((Nt,8))
P_falla_int=np.zeros((Nt,8))
P_falla_bolas=np.zeros((Nt,8))
P_falla_comb=np.zeros((Nt,8))

for i in range(1,Nt+1):
    inicio=(i-1)*L-(i-1)*l+1
    fin=i*L-(i-1)*l

    P_normal[i-1,0]=sqrt(mean(square(rod_sin_falla[inicio:fin]))) #RMS
    P_normal[i-1,1]=np.amax(rod_sin_falla[inicio:fin]) #Peak
    P_normal[i-1,2]=np.amax(rod_sin_falla[inicio:fin])-np.amin(rod_sin_falla[inicio:fin]) #peak-peak
    P_normal[i-1,3]=P_normal[i-1,1]/P_normal[i-1,0] #crest
    P_normal[i-1,4]=np.mean(rod_sin_falla[inicio:fin]) #Media
    P_normal[i-1,5]=np.var(rod_sin_falla[inicio:fin]) #var
    P_normal[i-1,6]=skew(rod_sin_falla[inicio:fin])[0] #asimetria
    P_normal[i-1,7]=kurtosis(rod_sin_falla[inicio:fin])[0] #curtosis
    
    P_falla_ext[i-1,0]=sqrt(mean(square(rod_con_falla_pist_ext[inicio:fin]))) #RMS
    P_falla_ext[i-1,1]=np.amax(rod_con_falla_pist_ext[inicio:fin]) #Peak
    P_falla_ext[i-1,2]=np.amax(rod_con_falla_pist_ext[inicio:fin])-np.amin(rod_con_falla_pist_ext[inicio:fin]) #peak-peak
    P_falla_ext[i-1,3]=P_falla_ext[i-1,1]/P_falla_ext[i-1,0] #crest
    P_falla_ext[i-1,4]=np.mean(rod_con_falla_pist_ext[inicio:fin]) #Media
    P_falla_ext[i-1,5]=np.var(rod_con_falla_pist_ext[inicio:fin]) #var
    P_falla_ext[i-1,6]=skew(rod_con_falla_pist_ext[inicio:fin])[0] #asimetria
    P_falla_ext[i-1,7]=kurtosis(rod_con_falla_pist_ext[inicio:fin])[0] #curtosis
    
    P_falla_int[i-1,0]=sqrt(mean(square(rod_con_falla_pist_int[inicio:fin]))) #RMS
    P_falla_int[i-1,1]=np.amax(rod_con_falla_pist_int[inicio:fin]) #Peak
    P_falla_int[i-1,2]=np.amax(rod_con_falla_pist_int[inicio:fin])-np.amin(rod_con_falla_pist_int[inicio:fin]) #peak-peak
    P_falla_int[i-1,3]=P_falla_int[i-1,1]/P_falla_int[i-1,0] #crest
    P_falla_int[i-1,4]=np.mean(rod_con_falla_pist_int[inicio:fin]) #Media
    P_falla_int[i-1,5]=np.var(rod_con_falla_pist_int[inicio:fin]) #var
    P_falla_int[i-1,6]=skew(rod_con_falla_pist_int[inicio:fin])[0] #asimetria
    P_falla_int[i-1,7]=kurtosis(rod_con_falla_pist_int[inicio:fin])[0] #curtosis

    P_falla_bolas[i-1,0]=sqrt(mean(square(rod_con_falla_bolas[inicio:fin]))) #RMS
    P_falla_bolas[i-1,1]=np.amax(rod_con_falla_bolas[inicio:fin]) #Peak
    P_falla_bolas[i-1,2]=np.amax(rod_con_falla_bolas[inicio:fin])-np.amin(rod_con_falla_bolas[inicio:fin]) #peak-peak
    P_falla_bolas[i-1,3]=P_falla_bolas[i-1,1]/P_falla_bolas[i-1,0] #crest
    P_falla_bolas[i-1,4]=np.mean(rod_con_falla_bolas[inicio:fin]) #Media
    P_falla_bolas[i-1,5]=np.var(rod_con_falla_bolas[inicio:fin]) #var
    P_falla_bolas[i-1,6]=skew(rod_con_falla_bolas[inicio:fin])[0] #asimetria
    P_falla_bolas[i-1,7]=kurtosis(rod_con_falla_bolas[inicio:fin])[0] #curtosis
    
    P_falla_comb[i-1,0]=sqrt(mean(square(rod_con_falla_comb[inicio:fin]))) #RMS
    P_falla_comb[i-1,1]=np.amax(rod_con_falla_comb[inicio:fin]) #Peak
    P_falla_comb[i-1,2]=np.amax(rod_con_falla_comb[inicio:fin])-np.amin(rod_con_falla_comb[inicio:fin]) #peak-peak
    P_falla_comb[i-1,3]=P_falla_comb[i-1,1]/P_falla_comb[i-1,0] #crest
    P_falla_comb[i-1,4]=np.mean(rod_con_falla_comb[inicio:fin]) #Media
    P_falla_comb[i-1,5]=np.var(rod_con_falla_comb[inicio:fin]) #var
    P_falla_comb[i-1,6]=skew(rod_con_falla_comb[inicio:fin])[0] #asimetria
    P_falla_comb[i-1,7]=kurtosis(rod_con_falla_comb[inicio:fin])[0] #curtosis


#graficar datos
f1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col',figsize=(9,6))
ax1.plot(P_normal[:,0])
ax1.plot(P_falla_ext[:,0])
ax1.plot(P_falla_int[:,0])
ax1.plot(P_falla_bolas[:,0])
ax1.plot(P_falla_comb[:,0])
ax1.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax1.set_title('RMS', fontsize=14)

ax2.plot(P_normal[:,1])
ax2.plot(P_falla_ext[:,1])
ax2.plot(P_falla_int[:,1])
ax2.plot(P_falla_bolas[:,1])
ax2.plot(P_falla_comb[:,1])
ax2.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax2.set_title('Valor peak', fontsize=14)

ax3.plot(P_normal[:,2])
ax3.plot(P_falla_ext[:,2])
ax3.plot(P_falla_int[:,2])
ax3.plot(P_falla_bolas[:,2])
ax3.plot(P_falla_comb[:,2])
ax3.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax3.set_title('Valor peak-peak', fontsize=14)

ax4.plot(P_normal[:,3])
ax4.plot(P_falla_ext[:,3])
ax4.plot(P_falla_int[:,3])
ax4.plot(P_falla_bolas[:,3])
ax4.plot(P_falla_comb[:,3])
ax4.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax4.set_title('Factor de cresta', fontsize=14)

f1.show()

f2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, sharex='col',figsize=(9,6))

ax5.plot(P_normal[:,4])
ax5.plot(P_falla_ext[:,4])
ax5.plot(P_falla_int[:,4])
ax5.plot(P_falla_bolas[:,4])
ax5.plot(P_falla_comb[:,4])
ax5.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax5.set_title('Media Aritmética', fontsize=14)

ax6.plot(P_normal[:,5])
ax6.plot(P_falla_ext[:,5])
ax6.plot(P_falla_int[:,5])
ax6.plot(P_falla_bolas[:,5])
ax6.plot(P_falla_comb[:,5])
ax6.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax6.set_title('Varianza', fontsize=14)

ax7.plot(P_normal[:,6])
ax7.plot(P_falla_ext[:,6])
ax7.plot(P_falla_int[:,6])
ax7.plot(P_falla_bolas[:,6])
ax7.plot(P_falla_comb[:,6])
ax7.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax7.set(xlabel='Segmento')
ax7.set_title('Asimetría', fontsize=14)

ax8.plot(P_normal[:,7])
ax8.plot(P_falla_ext[:,7])
ax8.plot(P_falla_int[:,7])
ax8.plot(P_falla_bolas[:,7])
ax8.plot(P_falla_comb[:,7])
ax8.legend(['Normal','Pista externa','Pista interna','bolas','combinacion de fallas'])
ax8.set(xlabel='Segmento')
ax8.set_title('Curtosis', fontsize=14)

f2.show()

