
#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

w, signal = scipy.io.wavfile.read('err.wav')
signal = [s[0] for s in signal]
spectrum = abs(fft(signal))
spectrum[::10] 

subplot(211)
freqs = linspace(0, w, len(spectrum[::10]))
stem(freqs, spectrum[::10], '-*')
xscale('log')
yscale('log')

show()
