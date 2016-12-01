from PIL import Image
from PIL import ImageEnhance
import sys

#---------------------------------------------------#
def image_logical_xor(image1, image2):
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_xor(image2.im))
#===================================================#

#---------------------------------------------------#
def image_logical_or(image1, image2):
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_or(image2.im))
#===================================================#

#---------------------------------------------------#
#Superimposes two images on top of each other.
# If you multiply an image with a solid black image,
# the result is black.
# If you multiply with a solid white image, the image is unaffected.
def multiply(image1, image2):
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_multiply(image2.im))
#===================================================#


#---------------------------------------------------#
# the following functions are used to invert and image
# and to specify an alpha level while combining the shares
def invert(image):
    image.load()
    return image._new(image.im.chop_invert())
#===================================================#

#---------------------------------------------------#
# Blend images using a transparency weight(alpha).
def blend(image1, image2, alpha):
    return Image.blend(image1, image2, alpha)
#===================================================#

#---------------------------------------------------#
# takes the shares as input and converts it to a bilevel image.
# Then we create empty image objects to hold the final combined images.
infile1 = Image.open(sys.argv[1])
infile2 = Image.open(sys.argv[2])

infile1 = infile1.convert('1')
infile2 = infile2.convert('1')

outfile1 = Image.new('1', infile1.size)
outfile2 = Image.new('1', infile1.size)
#===================================================#

#---------------------------------------------------#
# takes the maximum value of the pixels at the [x,y] col, row
# and paints the value at the corresponding position in the final image.
for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        outfile1.putpixel((x, y), max(infile1.getpixel((x, y)), infile2.getpixel((x, y))))

outfile1.save('takingMaxValue.png')

#===================================================#
outfile2 = image_logical_xor(infile1,infile2)
outfile2.save('combinedXOR.png')

#===================================================#
outfile2 = invert(outfile2)
outfile2.save('inverted.png')

#===================================================#
outfile2 = multiply(infile1,infile2)
outfile2.save('combinedMultiplied.png')

#===================================================#
outfile2 = blend(infile1,infile2,0.25) #change the alpha value here between 0 - 1.
outfile2.save('blended.png')

#===================================================#
outfile2 = image_logical_or(infile1,infile2)
outfile2.save('combinedLogicalOR.png')

#===================================================#
