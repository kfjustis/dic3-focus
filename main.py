import sys, getopt
import quantize
import numpy
import matplotlib.pyplot as plt

def main(argv):
  inputFile = ""
  outputFile = ""
  numLevels = ""

  # load file with command line args
  try:
    #opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    opts, args = getopt.getopt(argv, "hi:o:r:")
  except getopt.GetoptError:
    print("main.py -i <input file> -o <output file> -r <num levels>")
    sys.exit(2)

  for opt, arg in opts:
    if opt == "-h": # help
      print("main.py -i <input file> -o <output file> -r <num levels>")
      sys.exit()
    elif opt in ("-i"):
      inputFile = arg
    elif opt in ("-o"):
      outputFile = arg
    elif opt in ("-r"):
      numLevels = arg

  
  # load image as array
  imgArray = quantize.load_image_as_array(inputFile)
  print(imgArray)
  print(imgArray.shape)
  print()

  # reshape array from 2D to 1D
  imgArray = imgArray.flatten()

  # determine length (THIS IS THE DENOM FOR PROBABILITY)
  imgLength = len(imgArray)
  print("length: ", imgLength)
  print()
  
  '''
  mu, sigma = 0, 10 # want variance to be 100
  arr = numpy.random.normal(mu, sigma, 1000)
  '''
  
  # determine frequencies
  i = 0
  freqArray = [1] * 256
  while (i < len(imgArray)):
    freqArray[imgArray[i]] += 1
    i += 1

  # determine probabilities
  probArray = [f / imgLength for f in freqArray]
  
  # plot probabilities
  axes = plt.gca()
  axes.set_xlim([0, 255])
  plt.plot(probArray)
  
  # create reconstruction level array
  recon = quantize.init_recon_array_random(256, numLevels)
  if (recon == -1):
    print("Invalid args for reconstruction array\n")
    sys.exit()
  
  # plot reconstruction lines
  i = 0
  while (i < len(recon)):
    if (recon[i] == 1):
      plt.axvline(i, color='red')
    i += 1

  # Labels and show graph
  plt.xlabel('Pixel value')
  plt.ylabel('Probability')
  plt.title('Probability of Pixel Values')
  plt.show()

if __name__ == "__main__":
  main(sys.argv[1:])
