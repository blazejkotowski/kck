#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

signal = genfromtxt("spots.txt")
t = linspace(0, len(signal), len(signal), endpoint=False) # punkty na osi OX [s]

subplot(211)
plot(t, signal, '*')
ylabel("f(t)")
xlabel("t [s]")

signal1 = fft(signal)      
signal1 = abs(signal1)        # moduł 
print max(signal1[1:]), argmax(signal1[1:])

subplot(212)
freqs = linspace(0, len(signal), len(signal))
stem(freqs[1:], signal1[1:], '-*')
ylabel("liczba sygnalow")
xlabel("Hz")

show()
