from PIL import Image
from RAVEN import RAVEN
from MakeShape import HEX, SQUARE
import numpy as np
import os

print(f"Folder Name (with \): ")
folder = input()


print(f"Save Name: ")
SaveName = input()

path = os.getcwd()
RavPath = path + '\RAVEN-10000' + folder
SavePath = path + '\Images' + folder
CheckImPath = path + '\Images'

TrainNum = 0
ValNum = 0
TestNum = 0

print(f"Rav: {RavPath}")
print(f"Save: {SavePath}")

for dirName in os.scandir(RavPath):
    
    if dirName.is_dir() or dirName.is_file():
        
        print(f"{dirName.name}")
        # check if the image ends with npz
        # images.endswith(".npz")
        if (dirName.name.endswith(".npz")):
            name = dirName.name
            
            b = np.load(f"{RavPath}\{name}")
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

            # converting back to PIL Image and saving it to the correct folder in 'Images' directory
            PIL_image = Image.fromarray(np.uint8(npImage)).convert('RGB')
            saveName = SavePath + '.jpg'
            

            # checking to see if there is an 'Images' directory and creating one if not
            if os.path.isdir(CheckImPath) == False:
                os.mkdir(CheckImPath)
                
            # checking to see if there is an directory where the images will be saved and creating one if not
            if os.path.isdir(SavePath) == False:
                os.mkdir(SavePath)
            
            # saving image with correct name based on if train, validation, or test
            if name.endswith("_train.npz"):
                PIL_image.save(f"{SavePath}\{SaveName}_train_{TrainNum}.jpg")
                TrainNum += 1
            if name.endswith("_val.npz"):
                PIL_image.save(f"{SavePath}\{SaveName}_val_{ValNum}.jpg")
                ValNum += 1
            if name.endswith("_test.npz"):
                PIL_image.save(f"{SavePath}\{SaveName}_test_{TestNum}.jpg")
                TestNum += 1
        

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
