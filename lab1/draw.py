#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
from collections import OrderedDict
from itertools import cycle
from numpy import mean

algorithms = ['2cel-rs', '2cel', 'cel-rs', 'cel', 'rsel']
# data[alg_name][generation] = average result
# last_dataset[alg_name] = last data line
data = dict()
last_dataset = dict()

if __name__ == "__main__":
  # Data handling
  for alg, fn in zip(algorithms, map(lambda x: x+'.csv', algorithms)):
    data[alg] = OrderedDict()
    with open(fn, 'rb') as fd:
      reader = csv.reader(fd, delimiter=',')
      next(reader)
      for number,row in enumerate(reader):
        suma = sum(map(lambda x: float(x), row[2:]))
        dlugosc = len(row[2:])
        data[alg][int(row[1])/1000] = float(suma)/float(dlugosc)*100
        last_dataset[alg] = map(lambda x: float(x)*100, row[2:])
  

  # Plots
  plt.figure(1)
  plt.subplot(121)
  plt.xlabel("Rozegranych gier (x1000)")
  plt.ylabel("Odsetek wygranych [%]")
  plt.tick_params(labeltop="on")
  plt.grid()

  plots_legends = []
  markers = cycle(['D','s','^','v','o'])
  for name, values in data.items():
    p, = plt.plot(values.keys(), values.values(), markers.next()+'-', label=name, markersize=8, markevery=30)
    plots_legends += [[p, name]]

  plt.legend(*map(lambda x: list(x), zip(*plots_legends)), loc=4)
  plt.xlim([0, 500])
  plt.twiny()
  plt.xticks(range(0,201,40))
  plt.xlim([0, 200])
  plt.xlabel("Pokolenie")


  # Boxplot
  plt.subplot(122)
  plt.grid()
  plt.tick_params(labelleft="off", labelright="on")
  plt.boxplot(map(lambda (x,y): y, last_dataset.items()), notch=True)
  plt.scatter(range(len(last_dataset)+1)[1:], map(lambda x: mean(x), last_dataset.values()))
  plt.xticks(range(len(last_dataset)+1)[1:], last_dataset.keys())
  plt.ylim([60,100])

  # plt.savefig('lab1.pdf')
  plt.show()
  plt.close()
