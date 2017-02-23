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
        # stores the reconstruction points
        recon = [0] * int(length)

        # error check params
        if (len(recon) == 0 or length < 0):
                print("length was <= 0")
                return -1

        if (int(numLevels) <= 0):
                print("numlevels <= 0")
                return -1

        # loop through array and place recon points
        i = 0
        while (i < len(recon)):
                shouldPlace = numpy.random.randint(0, length)
                #shouldPlace = numpy.random.randint(start, end)
                
                # make sure we place all recon points
                if (int(shouldPlace) <= int(numLevels)):
                        if ((int(numLevels) - 1) >= 0 and recon[i] != 1):
                                numLevels = int(numLevels) - 1
                                recon[i] = 1
                                
                # keep looping if we still have points to place
                if (int(numLevels) > 0 and i == (len(recon) - 1)):
                        i = 0

                i += 1

        return recon

def init_decision_array(dist, recon, dist_sorted): # PASS THIS FOR OFFSET
        if (sum(dist) == 0 or sum(recon) == 0 or sum(dist_sorted) == 0):
                return -1
        if (not recon):
                return -1
        
        numRecons = sum(recon)
        numDecisions = sum(recon) + 1

        if (numDecisions <= 0):
                return -1

        # stores the position of each decision level
        decs = [0] * numDecisions

        # for each interval, determine the midpoint and store value
        i = 0
        avg = 0

        ind1 = next((ind for ind, val in enumerate(recon)
                     if val != 0), None)
 
        #decs[0] = (dist[0] + dist[ind1]''' + dist_sorted[0]''') / 2
        decs[0] = (dist[0] + dist[ind1] - dist_sorted[0]) / 2

        i = ind1 + 1
        found = 1
        newInd = None
        while (found < sum(recon) - 1):
                if (recon[i] is not 0):
                        newInd = i
                        avg = ((dist[ind1] + dist[newInd] - dist_sorted[0]) / 2)
                        decs[found] = avg
                        found += 1
                        ind1 = newInd
                

                i += 1

        avg = ((dist[newInd] + dist[len(dist)-1] - dist_sorted[0]) / 2)
        decs[len(decs)-1] = avg

        return decs
