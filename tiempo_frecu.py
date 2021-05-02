#importar librerías
import scipy.io as sio
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import math
from scipy.fftpack import fft, fftfreq

# Datos
rod_sin_falla = sio.loadmat('sano-C-1.mat')['Channel_1']
rod_con_falla_pist_ext = sio.loadmat('pista_externa-C-1.mat')['Channel_1']
rod_con_falla_pist_int = sio.loadmat('pista_interna-C-1.mat')['Channel_1']
rod_con_falla_bolas = sio.loadmat('bolas-C-1.mat')['Channel_1']
rod_con_falla_comb = sio.loadmat('combinacion-C-1.mat')['Channel_1']


Fs=200_000 #sampling rate
Nd=2_000_000

x1=rod_sin_falla[1:Nd,0]
f, t, S1 = signal.spectrogram(x1,Fs,window='boxcar',nperseg=20000,noverlap=2500)

x2=rod_con_falla_pist_ext[1:Nd,0]
f, t, S2 = signal.spectrogram(x2,Fs,window='boxcar',nperseg=20000,noverlap=2500)

x3=rod_con_falla_pist_int[1:Nd,0]
f, t, S3 = signal.spectrogram(x3,Fs,window='boxcar',nperseg=20000,noverlap=2500)

x4=rod_con_falla_bolas[1:Nd,0]
f, t, S4 = signal.spectrogram(x4,Fs,window='boxcar',nperseg=20000,noverlap=2500)

x5=rod_con_falla_comb[1:Nd,0]
f, t, S5 = signal.spectrogram(x5,Fs,window='boxcar',nperseg=20000,noverlap=2500)

fr_inicial=600
fr_final =1200
plt.figure(1)
plt.pcolormesh(t, f[fr_inicial:fr_final], S1[fr_inicial:fr_final] ,cmap='binary')
plt.ylabel('Frecuencia[Hz]', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Normal', fontsize=14)
plt.show()

plt.figure(2)

plt.pcolormesh(t, f[fr_inicial:fr_final], S2[fr_inicial:fr_final],cmap='binary')
plt.ylabel('Frecuencia[Hz]', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Pista Externa', fontsize=14)
plt.show()


plt.figure(3)

plt.pcolormesh(t, f[fr_inicial:fr_final], S3[fr_inicial:fr_final],cmap='binary')
plt.ylabel('Frecuencia[Hz]', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Pista Interna', fontsize=14)
plt.show()


plt.figure(4)

plt.pcolormesh(t, f[fr_inicial:fr_final], S4[fr_inicial:fr_final],cmap='binary')
plt.ylabel('Frecuencia[Hz]', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('falla en bolas', fontsize=14)
plt.show()


plt.figure(5)

plt.pcolormesh(t, f[fr_inicial:fr_final], S5[fr_inicial:fr_final],cmap='binary')
plt.ylabel('Frecuencia[Hz]', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('falla combinada', fontsize=14)
plt.show()