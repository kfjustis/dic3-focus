import sys, getopt
import quantize
import numpy
import matplotlib.pyplot as plt

def main(argv):
  numLevels = ""

  # load file with command line args
  try:
    opts, args = getopt.getopt(argv, "hr:")
  except getopt.GetoptError:
    print("main.py -r <num levels>")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-h": # help
      print("main.py -r <num levels>")
      sys.exit()
    elif opt in ("-r"):
      numLevels = arg

  # create gaussian distribution
  mu, sigma = 0, 10 # want variance to be 100
  dist = numpy.random.normal(mu, sigma, 1000)
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
    if (recon[i] == 1):
      plt.axvline(i + int(dist[0]), color='red')
    i += 1

  # Labels and show graph
  plt.xlabel('Values')
  plt.ylabel('Probability')
  plt.title('Quantization of Gaussian Input')
  plt.show()

if __name__ == "__main__":
  main(sys.argv[1:])
