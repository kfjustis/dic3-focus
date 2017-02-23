import sys, getopt
import quantize
import numpy
import matplotlib.pyplot as plt

from collections import OrderedDict

def main(argv):
  numLevels = ""

  # load file with command line args
  try:
    opts, args = getopt.getopt(argv, "hr:")
  except getopt.GetoptError:
    print("usage: main.py -r <num levels>")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-h": # help
      print("usage: main.py -r <num levels>")
      sys.exit()
    elif opt in ("-r"):
      numLevels = arg
    else:
      printf("usage: main.py -r <num levels>")

  if not opts:
      print("usage: main.py -r <num levels>")
      sys.exit(2)

  # create gaussian distribution
  mu, sigma = 0, 10 # want variance to be 100
  dist = numpy.random.normal(mu, sigma, 1000)
  orig_dist = dist[:] # save copy for later operations
  plt.hist(dist, 100, normed=True, align='mid')

  # sort, then determine data length
  dist.sort()
  length = dist[len(dist)-1] - dist[0]

  # create reconstruction level array
  recon = quantize.init_recon_array_random(length, numLevels)

  if (recon == -1):
    print("Invalid args for reconstruction array\n")
    sys.exit()

  # plot reconstruction lines
  i = 0
  while (i < len(recon)):
    if (recon[i] == 1): # I DO NOT KNOW WHY WE HAVE TO ADD THIS CONSTANT
      plt.axvline(i + int(dist[0]), color='red', label='Reconstruction Level')
      #plt.axvline(i, color='red')
    i += 1

  # create decision level array
  dec = quantize.init_decision_array(orig_dist, recon, dist)

  if (dec == -1):
    print("Invalid args for decision level array\n")
    sys.exit()

  '''
  # plot decision level array
  i = 0 # I DO NOT KNOW WHY WE HAVE TO ADD THIS CONSTANT
  while (i < len(dec)):
    plt.axvline(dec[i], color='green')
    i += 1
  '''

  # Legend, labels, and show graph
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = OrderedDict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys())
  
  plt.xlabel('Values')
  plt.ylabel('Probability')
  plt.title('Quantization of Gaussian Input')
  plt.show()

if __name__ == "__main__":
  main(sys.argv[1:])
