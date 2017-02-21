from PIL import Image
import numpy

'''
Loads an image from given file path
and stores it as an array. Used for
grayscale only -- other images untested

// param:  imgFile - the file path for a given
//         image to be loaded
// return: an array of numbers between 0-255
//         representing the given image file
'''
def load_image_as_array(imgFile):
	img = Image.open(imgFile)
	imgArray = numpy.asarray(img)

	return imgArray

'''
Generates an array of randomly distributed
reconstruction levels

// param:  length - the length of the array
// param:  numLevels - the number of requested levels
// return: an array of values representing randomly placed
           reconstruction levels where a 1 represents a valid
           placement and 0 represents an empty slot -- returns
           -1 on error
'''
def init_recon_array_random(length, numLevels):
        recon = [0] * length

        # error check params
        if (len(recon) == 0 or length < 0):
                return -1

        if (int(numLevels) <= 0):
                return -1

        # loop through array and place recon points
        i = 0
        while (i < len(recon)):
                shouldPlace = numpy.random.randint(0, length)
                if (int(shouldPlace) <= int(numLevels)):
                        if ((int(numLevels) - 1) >= 0 and recon[i] != 1):
                                numLevels = int(numLevels) - 1
                                recon[i] = 1
                                
                # keep looping if we still have points to place
                if (int(numLevels) > 0 and i == (len(recon) - 1)):
                        i = 0

                i += 1

        return recon
