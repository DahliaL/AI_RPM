from PIL import Image
from RAVEN import RAVEN
from MakeShape import HEX, SQUARE
import numpy as np

b = np.load('RAVEN_1_train.npz')
images = b['image'] # image: a (16, 160, 160) array where all 16 figures in each problem are stacked
                    # on the first dimension.
                    # Note that first 8 figures compose the problem matrix and the last 8 figures are choices.
target = b['target']# target: the index of the correct answer in the answer set. Note that it starts from 0
                    # and you should offset it by 8 if you want to retrieve it from the image array.

#for num in range(160):
    #for num2 in range(160):
        #if images[1][num][num2] != 255:
            #print(images[1][num][num2], num, num2)


PILimage = Image.new('RGB', (850, 1010), 'white') #960 but 40 added for buffer in between
testimg = Image.new('RGB', (160, 160), 'white')

# Use numpy to convert the PIL image into a numpy array
npImage = np.array(PILimage)
npTest = np.array(testimg)

# problem image generation
for i in range(8):
    offsetx = (i%3*160)
    if i in range(0, 2):
        offsety = 0
    if i in range(3, 5):
        offsety = 160
    if i in range(6, 8):
        offsety = 320
    for num in range(160):
        for num2 in range(160):
            if images[i][num][num2] != 255:
                npImage[num+offsety][num2+offsetx] = images[i][num][num2]

# answer choice
for i in range(9, 16):
    offsetx = (i%2*160)+530
    if i in range(9, 11):
        offsety = 0
    if i in range(11, 13):
        offsety = 160
    if i in range(13, 15):
        offsety = 320
    if i in range(15, 17):
        offsety = 480
    for num in range(160):
        for num2 in range(160):
            if images[i][num][num2] != 255:
                npImage[num+offsetx][num2+offsety] = images[i][num][num2]

# converting back to PIL Image and saving it
PIL_image = Image.fromarray(np.uint8(npImage)).convert('RGB')
PIL_image.show()


# this is for testing each figure when needed
#for num in range(160):
 #   for num2 in range(160):
  #      if images[1][num][num2] != 255:
   #         npTest[num][num2] = 0

#test_img = Image.fromarray(np.uint8(npTest)).convert('RGB')
#test_img.show()


# old stuff
#hex = HEX('test')
#hex.makeHex(200,0, None, img, 50)
#sq = SQUARE('test')
#sq.makeSquare(-200,0, None, img, 70)
#img.show()
