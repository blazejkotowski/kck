#!/usr/bin/python2.7

from matplotlib import pyplot as plt
from skimage import data, io

if __name__ == "__main__":
  image = data.imread("samolot01.jpg")
  io.imshow(image)
  plt.show()
  
