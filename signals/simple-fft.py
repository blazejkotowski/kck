#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 40           # częstotliwość próbkowania [Hz]
T = 2            # rozważany okres [s]

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

# f = lambda t : sin(5*2*pi*t)    # def. funkcji
# f = lambda t :sin(2*pi*t) + 2*sin(4*pi*t)
f = lambda t : sin(4*2*pi*t) + 0.5*random.random(n)
# f = lambda t : sin(5*2*pi*t)    # 5Hz
# f = lambda t : sin(21*2*pi*t)    # 21Hz
signal = f(t)                 # funkcja spróbkowana

subplot(211)
plot(t, signal, '*')
ylabel("f(t)")
xlabel("t [s]")

signal1 = fft(signal)      
signal1 = abs(signal1)        # moduł 

subplot(212)
freqs = linspace(0, w, n)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal1, '-*')
ylabel("liczba sygnalow")
xlabel("Hz")

show()
