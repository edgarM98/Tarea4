# UNIVERSIDAD DE COSTA RICA
## ESCUELA DE INGENIERÍA ELÉCTRICA

## IE0405 - MODELOS PROBABILÍSTICOS DE SEÑALES Y SISTEMAS 

# TAREA 4

## EDGAR MADRIGAL VÍQUEZ
## CARNÉ: B64047
## Profesor: Fabián Abarca


##  PREGUNTA 1 
-Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Tenemos una cantidad de 10000 bits para los cuales se realizará el esquema de modulación BPSK, este tipo de modulación tiene como resultado dos posibles fases de salida para la portadora con una sola frecuencia. Una fase de salida representa un 1 lógico y la otra un 0 lógico. Conforme la señal digital de entrada cambia de estado, la fase de la portadora de salida se desplaza entre dos ángulos que están 180° fuera de fase.

Se realizó 50 puntos de muestreo para cada periodo de la señal. En la siguiente figura tenemos la señal portadora de tipo sinusoidal a una frecuencia de 5000 Hz, con un periodo de 0.0002 s. 

![onda](/onda.png)


Luego se procedió a realizar la modulación tipo BPSK con el siguiente código, donde cómo podemos ver la función corresponde a seno si la señal de entrada corresponde a un bit 1 y la función corresponde a -seno si el bit de entrada es 0.

      # Creación de la señal modulada BPSK
      
      for k, b in enumerate(bits):
        senal[k*p:(k+1)*p] = ((2*b) - 1) * sinus
        

En la siguiente figura se tiene ahora la señal modulada con el esquema BPSK para los primeros 10 bits del archivo. Donde como podemos observar se tiene una señal sinusoidal que cambia de fase a medida que la señal digital de entrada cambia de estado. En este caso, se realizó solo para los primeros 10 bits ya que si se hacía para los 10000 entonces no se iba a poder osbervar el cambio de fase.

![bits_modulados](/bits_modulados.png)


##  PREGUNTA 2

-Calcular la potencia promedio de la señal modulada generada.

Primero se calculó la potencia instantánea y después la potencia promedio en base a la potencia instantánea calculada. La potencia promedio obtenida de la señal modulada fue de 0.49 W. Se utilizó el siguiente código.

    # Potencia instantánea
    Pinst = senal**2

    # Potencia promedio a partir de la potencia instantánea (W)
    Ps = integrate.trapz(Pinst, t) / (N * T)
    print("La potencia promedio es de:" ,Ps)


##  PREGUNTA 3

Para esta parte se procedió a simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB. Se utilizó el siguiente código, en el cual se calculó primero la potencia del ruido para el primer valor de SNR que es -1. La raíz cuadrada de este valor de potencia obtenido es igual al valor de la desviación estándar, que se utiliza como parámetro para obtener el ruido por medio de la función de np.random.normal. Finalmente, la señal recibida es la forma de la señal original más el ruido aleatorio creado.

    SNR = -2

    # Potencia del ruido para SNR y potencia de la señal dada
    Pn = Ps / (10**(SNR / 10))

    # Desviación estándar del ruido
    # Potencia es igual a sigma al cuadrado
    sigma = np.sqrt(Pn)

    # Crear ruido (Pn = sigma^2)
    ruido = np.random.normal(0, sigma, senal.shape)

    # Simular "el canal": señal recibida
    # Normalmente tiene atenuaciones
    Rx = senal + ruido

Al graficar este ruido para un valor de SNR = -1, se obtiene lo siguiente:

![ruido_primerSNR](/ruido_primerSNR.png)


Posteriormente, se procedió realizar el mismo procedimiento para todos los valores de SNR solicitados (-1, -2, 0, 1, 2, 3) y se graficó en una misma figura, se obtuvo lo siguiente:

En la figura siguiente se puede observar la señal ahora con ruido para cada uno de los valores de la relación SNR.
![ruido](/ruido.png)



##  PREGUNTA 4
(10 %) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

Primero se graficó la la densidad espectral de potencia de la señal con el método de Welch antes del canal ruidoso para cada uno de los valores de SNR, por medio del siguiente código:

      # Antes del canal ruidoso
      fw, PSD = signal.welch(senal, fs, nperseg=1024)
      plt.figure()
      plt.semilogy(fw, PSD)

Se obtuvo la siguiente gráfica:

![antes_ruido](/antes_ruido.png)

Tiene este comportamiento ya que se realiza antes del ruido, por lo cual no se ve influenciado por la presencia del ruido.

Luego se procedió a calcular nuevamente la densidad espectral de potencia de la señal para cada uno de los valores de SNR, pero esta vez luego del canal ruidoso, por medio del siguiente código:

![despues_ruido](/despues_ruido.png)

       # Después del canal ruidoso
      fw, PSD = signal.welch(Rx, fs, nperseg=1024)
      plt.figure()
      plt.semilogy(fw, PSD)

Como se observa, al incluir el ruido ahora cambia la magnitud en la curva para cada uno de los valores de SNR. La curva en color azul corresponde a la de SNR = -2 y la curva de color azul corresponde a la de color café.


##  PREGUNTA 5
(20 %) Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

Para esta parte, se utilizó las siguientes líneas de código:

      # Pseudo-energía de la onda original, Suma de la pot instantánea al cuadrado
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

Este código permite obtener en el array bits[Rx] un bit 1 si la energía de la señal original es mayor a la mitad de la energía de la señal ruidosa y en caso contrario obtener un bit 0. Como era de esperarse, si imprimimos el array bitsRx, se obtiene los mismos 10000 bits del archivo original. Finalmente, se calculó la tasa de error de los bits obtenidos. Se obtuvo lo siguiente:

-Para un SNR = -2 la tasa de error fue de 0.0004  
-Para un SNR = -1 la tasa de error fue de 0.0002  
-Para un SNR = 0 la tasa de error fue de 0.0003  
-Para un SNR = 1 la tasa de error fue de 0.00  
-Para un SNR = 2 la tasa de error fue de 0.00  
-Para un SNR = 3 la tasa de error fue de 0.00

Se puede observar que la tasa de error disminuye a medida que aumenta la relación de señal a ruido. En base a esto , se tomó la recomendación de hacer la prueba ahora para un intervalo de valores de SNR de -5 a 0; se obtuvo lo siguiente:


-Para un SNR = -2 la tasa de error fue de 0.0123  
-Para un SNR = -1 la tasa de error fue de 0.0058  
-Para un SNR = 0 la tasa de error fue de 0.0027  
-Para un SNR = 1 la tasa de error fue de 0.0015  
-Para un SNR = 2 la tasa de error fue de 0.0003  
-Para un SNR = 3 la tasa de error fue de 0.00


##  PREGUNTA 6

Ahora se tiene la gráfica de BER vs. SNR. Donde los valores del eje X correspondena a los valores del vector para los diferentes SNR (-3, -2, -1, 0, 1, 2, 3) y los valores del eje Y corresponden al vector de BER.

Para una primera simulación se obtuvo:

![curva](/curva.png)

Para esta parte la gráfica en cada ocasión de simulación siempre va a dar diferente ya que está basada en los valores de BER (eje y); además el ruido es generado de forma aleatoria por lo que se va a tener el mismo comportmiento de decreciente, pero algunas variaciones. 

Para una segunda simulación se obtuvo:

![curva2](/curva2.png)

Donde se puede observar el mismo comportamiento en la curva.





