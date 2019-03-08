import numpy as np
import cv2
import random
import glob



def main():
    iters = input('Transformations per image: ')
    iters = int(iters)
    i = 1
    while int(i) <= int(iters):
        for filename in glob.glob('*.jpg'):
            print("Editting: " , filename)
            #reading the image
            img = cv2.imread(filename,1)
            
            
            rows,cols,ch = img.shape
            x = 1
            isset = 0
            #Scaling the image
            if random.sample(set([0, 1]), 1) == [0]:
            	newImg = cv2.resize(img, (0,0), fx=2, fy=2)
            #Rotate Image
            if random.sample(set([0, 1]), 1) == [0]:
                rotateChoice = [0,90,180,270]
                rotateDecide = (random.choice(rotateChoice))
                rotate = cv2.getRotationMatrix2D((cols/2,rows/2),rotateDecide,1)
                if isset == 1:
                    newImg = cv2.warpAffine(newImg,rotate,(cols,rows))
                else:
                    isset = 1
                    newImg = cv2.warpAffine(img,rotate,(cols,rows))
            #Translation
            if random.sample(set([0, 1]), 1) == [0]:
                #Horizontal
                horizontalChoice = [-15,-5,0,5,15]
                horizontal = (random.choice(horizontalChoice))
                #Vertical
                verticalChoice = [-15,-5,0,5,15]
                vertical = (random.choice(verticalChoice))
                tran = np.float32([[1,0,horizontal],[0,1,vertical]])
                if isset == 1:
                    newImg = cv2.warpAffine(newImg,tran,(cols,rows))
                else:
                    isset = 1
                    newImg = cv2.warpAffine(img,tran,(cols,rows))
		
	    

            #Reflection
            if random.sample(set([0, 1]), 1) == [0]:
                flipChoice = ["hor","ver","both"]
                x = (random.choice(flipChoice))
                #Horizontal
                if x=="hor":
                    if isset == 1:
                        newImg = cv2.flip( newImg, 0 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, 0 )
                #Vertical
                if x=="ver":
                    if isset == 1:
                        newImg = cv2.flip( newImg, 1 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, 1 )
                #Both
                if x=="both":
                    if isset == 1:
                        newImg = cv2.flip( newImg, -1 )
                    else:
                        isset = 1
                        newImg = cv2.flip( img, -1 )
            
            


            x = filename.split(".")
            if "_NEW" not in x[0]:
                newFile = x[0] + "_NEW-" + str(i) + ".JPG"
            else:
                y = filename.split("-")
                newFile = y[0] + "-" + str(i) + ".JPG"
            print("Saving new image: ", newFile)
            cv2.imwrite(newFile,newImg)
        i = int(i) + 1
main()
