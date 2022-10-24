from PIL import Image
from RAVEN import RAVEN
from MakeShape import HEX, SQUARE

img = Image.new('RGB', (500, 300), 'white')
hex = HEX('test')
hex.makeHex(200,0, None, img, 70)
sq = SQUARE('test')
sq.makeSquare(-200,0, None, img, 70)

rav = RAVEN('test')
rav.randomizeValues()

#print(rav.getScene())
#print(rav.getStructure())
#print(rav.getComponent())
#print(rav.getLayout())
#print(rav.getEntity())