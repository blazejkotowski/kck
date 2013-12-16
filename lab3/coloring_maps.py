#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math as m
import colorsys

def wczytaj():
  lines = []
  with open('big.dem') as f:
    lines = [line.split() for line in f]
  width, height, distance = int(lines[0][0]), int(lines[0][1]), int(lines[0][2])
  data = map(lambda x: map(lambda y: float(y), x), lines[1:])

  maxx = max(map(lambda x: max(x), data))
  minn = min(map(lambda x: min(x), data))

  return width, height, distance, data, maxx, minn

def rysuj(data, width, height, maxi, mini):
  fig, ax = plt.subplots()
  pixels = np.zeros((height, width, 3))
  for i in range(height):
    for j in range(width):
      ti = (i>0 and i - 1 or i + 1)
      tj = (j>0 and j - 1 or j + 1)
      nv = normalizuj(np.array([i, j, data[i][j]]), np.array([i, tj, data[i][tj]]), np.array([ti, j, data[ti][j]]))       
      pixels[i,j] = gradient(data[i][j], maxi, mini, nv, [-15000, 30000, 40000])

  ax.imshow(pixels)
  fig.savefig('mapa.pdf')


def gradient(x, maxi, mini, normalVector, lightVector):
  normalLength = m.sqrt(normalVector[0]**2 + normalVector[1]**2 + normalVector[2]**2)
  lightLength = m.sqrt(lightVector[0]**2 + lightVector[1]**2 + lightVector[2]**2)
  dotProd = np.dot(normalVector, lightVector)
  cosNL = dotProd / (lightLength * normalLength)
  s = 1
  if cosNL >= 0:
    v = np.sin(0.35*cosNL+0.65)
  else:
    v = np.sin(0.5*abs(cosNL) + 0.5)
  if cosNL >=0.6 and cosNL <= 0.75: 
    s = abs(np.cos(cosNL+np.pi + 0.65)) + 0.1
  y = (x-mini)/(maxi-mini)
  return colorsys.hsv_to_rgb((1-y)/2, s,v)

    
def normalizuj(P1, P2, P3):
  return np.cross((P3-P1),(P2-P1))

if __name__ == '__main__':
  width, height, distance, data, maxi, mini = wczytaj()
  rysuj(data, width, height, maxi, mini)

