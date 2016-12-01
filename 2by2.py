from PIL import Image
from PIL import ImageEnhance
import random
import sys

# input a jpeg or png as a argv
image = Image.open(sys.argv[1])

# convert the given image to bilevel
image = image.convert('1')

# we make two files to hold the resultant shares.
share1 = Image.new("1", [dimension * 2 for dimension in image.size])
share2 = Image.new("1", [dimension * 2 for dimension in image.size])


for x in range(0, image.size[0], 2):
    for y in range(0, image.size[1], 2):
        sourcepixel = image.getpixel((x, y))
        print sourcepixel
        assert sourcepixel in (0, 255)
        chance = random.random()
        if sourcepixel == 0: #if it's black
            if chance < .5:
                print "black pixel with less than 0.5"
                share1.putpixel((x * 2, y * 2), 255)         #  1  white
                share1.putpixel((x * 2 + 1, y * 2), 0)       #  0  black
                share1.putpixel((x * 2, y * 2 + 1), 0)       #  0  black
                share1.putpixel((x * 2 + 1, y * 2 + 1), 255) #  1  white

                share2.putpixel((x * 2, y * 2), 0)           #  0
                share2.putpixel((x * 2 + 1, y * 2), 255)     #  1
                share2.putpixel((x * 2, y * 2 + 1), 255)     #  1
                share2.putpixel((x * 2 + 1, y * 2 + 1), 0)   #  0
            else:
                print "black pixel with greater than 0.5"
                share1.putpixel((x * 2, y * 2), 0)           #  0
                share1.putpixel((x * 2 + 1, y * 2), 255)     #  1
                share1.putpixel((x * 2, y * 2 + 1), 255)     #  1
                share1.putpixel((x * 2 + 1, y * 2 + 1), 0)   #  0

                share2.putpixel((x * 2, y * 2), 255)         #  1
                share2.putpixel((x * 2 + 1, y * 2), 0)       #  0
                share2.putpixel((x * 2, y * 2 + 1), 0)       #  0
                share2.putpixel((x * 2 + 1, y * 2 + 1), 255) #  1


        elif sourcepixel == 255: # if it's white
            if chance < .5:
                print "white pixel with less than 0.5"
                share1.putpixel((x * 2, y * 2), 255)
                share1.putpixel((x * 2 + 1, y * 2), 0)
                share1.putpixel((x * 2, y * 2 + 1), 0)
                share1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                share2.putpixel((x * 2, y * 2), 255)
                share2.putpixel((x * 2 + 1, y * 2), 0)
                share2.putpixel((x * 2, y * 2 + 1), 0)
                share2.putpixel((x * 2 + 1, y * 2 + 1), 255)
            else:
                print "white pixel with greater than 0.5"
                share1.putpixel((x * 2, y * 2), 0)
                share1.putpixel((x * 2 + 1, y * 2), 255)
                share1.putpixel((x * 2, y * 2 + 1), 255)
                share1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                share2.putpixel((x * 2, y * 2), 0)
                share2.putpixel((x * 2 + 1, y * 2), 255)
                share2.putpixel((x * 2, y * 2 + 1), 255)
                share2.putpixel((x * 2 + 1, y * 2 + 1), 0)

share1.save('result1.png')
share2.save('result2.png')
