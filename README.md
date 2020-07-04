# UNIVERSIDAD DE COSTA RICA
## ESCUELA DE INGENIERÍA ELÉCTRICA

## IE0405 - MODELOS PROBABILÍSTICOS DE SEÑALES Y SISTEMAS 

# TAREA 4

## EDGAR MADRIGAL VÍQUEZ
## CARNÉ: B64047
## Profesor: Fabián Abarca


##  PREGUNTA 1
(20 %) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Tenemos una cantidad de 10000 bits para los cuales se realizará el esquema de modulación BPSK, este tipo de modulación tiene como resultado dos posibles fases de salida para la portadora con una sola frecuencia. Una fase de salida representa un 1 lógico y la otra un 0 lógico. Conforme la señal digital de entrada cambia de estado, la fase de la portadora de salida se desplaza entre dos ángulos que están 180° fuera de fase.

Se realizó 50 puntos de muestreo para cada periodo de la señal. En la siguiente figura tenemos la señal portadora de tipo sinusoidal a una frecuencia de 5000 Hz. 

![onda](/onda.png)


En la siguiente figura se tiene la señal modulada con el esquema BPSK para los primeros bits del archivo. Donde como podemos observar se tiene una señal sinusoidal que cambia de fase a medida que la señal digital de entrada cambia de estado.

![bits_modulados](/bits_modulados.png)




##  PREGUNTA 2
(10 %) Calcular la potencia promedio de la señal modulada generada.





##  PREGUNTA 3

Para esta parte se procedió a simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

En la figura siguiente se puede observar la señal ahora con ruido para cada uno de los valores de la relación SNR.
![ruido](/ruido.png)





##  PREGUNTA 4
(10 %) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

Se procedió a graficar la densidad espectral de potencia de la señal con el método de Welch antes del canal ruidoso y se obtuvo la gráfica siguiente.

![antes_ruido](/antes_ruido.png)


Ahora se procedió a calcular nuevamente la densidad espectral de potencia de la señal, pero esta vez luego del canal ruidoso. Se obtuvo la siguiente gráfica.

![despues_ruido](/despues_ruido.png)





##  PREGUNTA 5
(20 %) Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


##  PREGUNTA 6

Ahora se tiene la gráfica de BER vs. SNR. Donde los valores del eje X correspondena a los valores del vector para los diferentes SNR y los valores del eje Y corresponden al vector de BER.

![curva](/curva.png)




