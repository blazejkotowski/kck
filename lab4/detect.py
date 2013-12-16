#!/usr/bin/env python
import numpy as np
import cv2
from colorsys import hsv_to_rgb

if __name__ == "__main__":
  names = ["samolot%02d.jpg" % x for x in range(0,13)]
  for i, name in enumerate(names):
      img = cv2.imread(name)
      temp = cv2.multiply(img, np.array([0.7]))
      temp = cv2.blur(temp, (5,5))
      temp = cv2.Canny(temp,20,120)
      temp = cv2.dilate(temp, np.ones((8,8))*2, iterations=2)

      k, tmp = cv2.findContours(temp,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      for j,kontur in enumerate(k):
          cv2.drawContours(img, [kontur],0,np.array(hsv_to_rgb(1.0/len(k) * j, 1.0, 1.0))*255.0,2)
          moments = cv2.moments(kontur)
          if moments['m00']:
              cv2.circle(img, (int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])), 3, (255, 255, 255), 1)
      cv2.imwrite('samolot%02d-detected.jpg' % i, img)
