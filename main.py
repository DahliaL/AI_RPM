from PIL import Image
from RAVEN import RAVEN
from MakeShape import HEX, SQUARE

import numpy as np
b = np.load('RAVEN_9792_train.npz')
images = b['image']

for num in range(160):
    for num2 in range(160):
        if images[1][num][num2] != 255:
            print(images[1][num][num2], num, num2)

                       
#print(images[4][140][50])


img = Image.new('RGB', (500, 300), 'white')
hex = HEX('test')
hex.makeHex(200,0, None, img, 50)
sq = SQUARE('test')
sq.makeSquare(-200,0, None, img, 70)
#img.show()

rav = RAVEN('test')
rav.randomizeValues()

#print(rav.getScene())
#print(rav.getStructure())
#print(rav.getComponent())
#print(rav.getLayout())
#print(rav.getEntity())
