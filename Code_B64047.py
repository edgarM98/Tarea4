# Se importa todas las librerias que se van a necesitar
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import csv
from scipy import signal
from scipy import integrate
'''
'''
# Abrimos el archivo .txt y leemos
prueba = open("bits.txt", "r")
lineas = prueba.read().splitlines()

# Esto es para leer como float cada elemento de la lista.
datos = [linea.split(",") for linea in lineas]
datos = [[float(dato) for dato in linea] for linea in datos]
#print(datos)

# El total de muestras va a ser el número de muestras que tenga el archivo .txt
total = len(datos)
bits = np.array(datos)
#print(bits)
#print("\n")

############  PREGUNTA 1  ##################

# Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

# Número de bits
N = 10000

# Frecuencia de operación
f = 5000 # Hz

# Duración del período de cada símbolo (onda)
T = 1/f # 1 ms

# Número de puntos de muestreo por período
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la forma de onda de la portadora
sinus = np.sin(2*np.pi * f * tp)

# Visualización de la forma de onda sinusoidal de la portadora
plt.plot(tp, sinus)
plt.title("Onda portadora sinusoidal")
plt.xlabel('Tiempo / s')
plt.savefig("onda.png")
plt.show()

# Frecuencia de muestreo
fs = p/T # 

# Creación de la línea temporal para toda la señal 
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada 
senal = np.zeros(t.shape)

# Creación de la señal modulada BPSK
# Vemos que cuando hay un 1 la señal es sen y cuando hay
# un 0 la señal es -sen
for k, b in enumerate(bits):
  senal[k*p:(k+1)*p] = ((2*b) - 1) * sinus


# Visualización de los primeros bits modulados
# Hacemos grafica para los primeros 10 bits
pb = 10  # Cantidad de bits que quiero ver
plt.figure()
plt.plot(senal[0:pb*p])  # p: numero de muestras por periodo
plt.title("Bits modulados")
plt.ylabel('Vector de y')
plt.xlabel('Vector de x')
plt.savefig("bits_modulados.png")
plt.show()



############  PREGUNTA 2  ##################

# Calcular la potencia promedio de la señal modulada generada.

# Potencia instantánea
Pinst = senal**2

# Potencia promedio a partir de la potencia instantánea (W)
Ps = integrate.trapz(Pinst, t) / (N * T)
print("La potencia promedio es de:" ,Ps)
print("\n")


############  PREGUNTA 3  ##################

#  Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB
# AWGN: Aditive white gaussian noise

# Relación señal-a-ruido deseada
SNR = -2

# Potencia del ruido para SNR y potencia de la señal dadas
Pn = Ps / (10**(SNR / 10))

# Desviación estándar del ruido
# Potencia es igual a sigma al cuadrado
sigma = np.sqrt(Pn)

# Crear ruido (Pn = sigma^2)
ruido = np.random.normal(0, sigma, senal.shape)

# Simular "el canal": señal recibida
# Normalmente tiene atenuaciones
Rx = senal + ruido

# Ahora mismo procedimiento pero para otros valores de SNR

SNR2 = -1
Pn2 = Ps / (10**(SNR2 / 10))
sigma2 = np.sqrt(Pn2)
ruido2 = np.random.normal(0, sigma2, senal.shape)
Rx2 = senal + ruido2

SNR3 = 0
Pn3 = Ps / (10**(SNR3 / 10))
sigma3 = np.sqrt(Pn3)
ruido3 = np.random.normal(0, sigma3, senal.shape)
Rx3 = senal + ruido3

SNR4 = 1
Pn4 = Ps / (10**(SNR4 / 10))
sigma4 = np.sqrt(Pn4)
ruido4 = np.random.normal(0, sigma4, senal.shape)
Rx4 = senal + ruido4

SNR5 = 2
Pn5 = Ps / (10**(SNR5 / 10))
sigma5 = np.sqrt(Pn5)
ruido5 = np.random.normal(0, sigma5, senal.shape)
Rx5 = senal + ruido5

SNR6 = 3
Pn6 = Ps / (10**(SNR6 / 10))
sigma6 = np.sqrt(Pn6)
ruido6 = np.random.normal(0, sigma6, senal.shape)
Rx6 = senal + ruido6


# Visualización de los primeros 10 bits recibidos para cada uno
# de los valores del SNR. Graficamos todos en la misma.
pb = 10
plt.figure()
plt.plot(Rx[0:pb*p])
plt.plot(Rx2[0:pb*p])
plt.plot(Rx3[0:pb*p])
plt.plot(Rx4[0:pb*p])
plt.plot(Rx5[0:pb*p])
plt.plot(Rx6[0:pb*p])
plt.title("Ruido para varias relaciones de señal a ruido")
plt.savefig("ruido.png")
plt.show()


############  PREGUNTA 4  ##################

# Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

# Antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.title("Antes del canal ruidoso")
plt.savefig("antes_ruido.png")
plt.show()

# Después del canal ruidoso
fw, PSD = signal.welch(Rx, fs, nperseg=1024)
fw2, PSD2 = signal.welch(Rx2, fs, nperseg=1024)
fw3, PSD3 = signal.welch(Rx3, fs, nperseg=1024)
fw4, PSD4 = signal.welch(Rx4, fs, nperseg=1024)
fw5, PSD5 = signal.welch(Rx5, fs, nperseg=1024)
fw6, PSD6 = signal.welch(Rx6, fs, nperseg=1024)

plt.figure()

plt.semilogy(fw, PSD)
plt.semilogy(fw2, PSD2)
plt.semilogy(fw3, PSD3)
plt.semilogy(fw4, PSD4)
plt.semilogy(fw5, PSD5)
plt.semilogy(fw6, PSD6)

plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.title("Después del canal ruidoso")
plt.savefig("despues_ruido.png")
plt.show()


############  PREGUNTA 5  ##################

# Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

# Pseudo-energía de la onda original (esta es suma, no integral)
# Suma de la pot instantanea al cuadrado
Es = np.sum(sinus**2)

# Inicialización del vector de bits recibidos
bitsRx = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for k, b in enumerate(bits):
  Ep = np.sum(Rx[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx[k] = 1
  else:
    bitsRx[k] = 0

#print(bitsRx)

err = np.sum(np.abs(bits - bitsRx))
# BER: Bit Error Rate (Bits malos entres bits totales)
BER = err/N

print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err, N, BER))

# Mismo procedimiento para todos los demás valores de SNR

#  Para SNR = -1
Es2 = np.sum(sinus**2)
bitsRx2 = np.zeros(bits.shape)
for k, b in enumerate(bits):
  Ep = np.sum(Rx2[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx2[k] = 1
  else:
    bitsRx2[k] = 0
#print(bitsRx)
err2 = np.sum(np.abs(bits - bitsRx2))
BER2 = err2/N
print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err2, N, BER2))

#  Para SNR = 0
Es3 = np.sum(sinus**2)
bitsRx3 = np.zeros(bits.shape)
for k, b in enumerate(bits):
  Ep = np.sum(Rx3[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx3[k] = 1
  else:
    bitsRx3[k] = 0
#print(bitsRx)
err3 = np.sum(np.abs(bits - bitsRx3))
BER3 = err3/N
print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err3, N, BER3))

#  Para SNR = 1
Es4 = np.sum(sinus**2)
bitsRx4 = np.zeros(bits.shape)
for k, b in enumerate(bits):
  Ep = np.sum(Rx4[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx4[k] = 1
  else:
    bitsRx4[k] = 0
#print(bitsRx)
err4 = np.sum(np.abs(bits - bitsRx4))
BER4 = err4/N
print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err4, N, BER4))

#  Para SNR = 2
Es5 = np.sum(sinus**2)
bitsRx5 = np.zeros(bits.shape)
for k, b in enumerate(bits):
  Ep = np.sum(Rx5[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx5[k] = 1
  else:
    bitsRx5[k] = 0
#print(bitsRx)
err5 = np.sum(np.abs(bits - bitsRx5))
BER5 = err5/N
print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err5, N, BER5))

#  Para SNR = 3
Es6 = np.sum(sinus**2)
bitsRx6 = np.zeros(bits.shape)
for k, b in enumerate(bits):
  Ep = np.sum(Rx6[k*p:(k+1)*p] * sinus)
  if Ep > Es/2:
    bitsRx6[k] = 1
  else:
    bitsRx6[k] = 0
#print(bitsRx)
err6 = np.sum(np.abs(bits - bitsRx6))
BER6 = err6/N
print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err6, N, BER6))



############  PREGUNTA 6  ##################

# Graficar BER versus SNR.

# Vector de valores de Bit Error Rate (Bits malos entres bits # totales)

BERf = [BER, BER2, BER3, BER4, BER5, BER6]
# Vector de valores de SNR
SNRf = [-2, -1, 0, 1, 2, 3]

# Grafica de SNR vs. BER
plt.figure()
plt.plot(SNRf, BERf)  # p: numero de muestras por periodo
plt.title("SNR vs BER.")
plt.ylabel('BER')
plt.xlabel('SNR')
plt.savefig("curva.png")
plt.show()