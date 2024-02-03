#   Python Program : "GenerateGradient Vertical or Horizontal function"
#   by Leevaille Galet.
#   Creation Date 05/01/2022        Location : Nantes, France
#   Using Python 3.10 and Atom Text Editor
#   Program Version : 0.2
#   Language : English
#
#   VAR LEXICON
#   ID          TYPE                    ROLE
#
#   grdpil      function                Gen Gradients with pillow
#
#     DETAILS
#       /!\ doesn't support RGBA for the moment + work with Numpy and Pillow
#       grdpil('
#           'pillow image',  gradient 'vertical(v)/horizontal(h)','start clr (RGB array)',
#           'end clr (RGB array)', height, width, start coordinates(X,Y)
#       )
#
#   imgd        Object(Pillow image)    ///
#   vhdata      String                  Says to the function v/h for vertical/horizontal gradient
#   clrs        RGB array               Define the start color
#   clre        RGB array               Define the end color
#   h           int                     Define the Height of the gradient (px)
#   w           int                     Define the width of the gradient (px)
#   coord       XY array                Define the start of the gradient (X,Y)
#       X = Line   Y = colonne
#
#   aray        Image RGB Array         Image Data RGB
#   RAr         Array                   Red Data Array
#   GAr         Array                   Green Data Array
#   BAr         Array                   Blue Data Array
import PIL.Image as ImgP
import numpy as np

def grdpil(imgd, vhdata,clrs,clre,h,w,coord):

    # Transform in array
    aray = np.array(imgd)

    # define color array with linspace
    if (vhdata == 'h'):
        RAr = np.linspace(clrs[0],clre[0],w,dtype='uint8')
        GAr = np.linspace(clrs[1],clre[1],w,dtype='uint8')
        BAr = np.linspace(clrs[2],clre[2],w,dtype='uint8')

        # define the x for the color in the second while
        # like this, value gonna change for each pixel of the line (h)
        line = coord[0]
        while( (line <= (aray.shape[0]-1)) and (line < (coord[0]+h)) ):
            pixel = coord[1]
            x = 0
            while( (pixel <= (aray.shape[1]-1)) and (pixel < (coord[1]+w)) ):
                aray[line][pixel][0] = RAr[x]
                aray[line][pixel][1] = GAr[x]
                aray[line][pixel][2] = BAr[x]
                pixel = pixel+1
                x = x+1
            line = line+1

    if (vhdata == 'v'):
        RAr = np.linspace(clrs[0],clre[0],h,dtype='uint8')
        GAr = np.linspace(clrs[1],clre[1],h,dtype='uint8')
        BAr = np.linspace(clrs[2],clre[2],h,dtype='uint8')

        # define the x for the color in the first while
        # like this, value gonna change for each line (v)
        line = coord[0]
        x = 0
        while( (line <= (aray.shape[0]-1)) and (line < (coord[0]+h)) ):
            pixel = coord[1]
            while( (pixel <= (aray.shape[1]-1)) and (pixel < (coord[1]+w)) ):
                aray[line][pixel][0] = RAr[x]
                aray[line][pixel][1] = GAr[x]
                aray[line][pixel][2] = BAr[x]
                pixel = pixel+1
            line = line+1
            x = x+1

    # define new image, return image
    imgd = ImgP.fromarray(aray)
    return imgd
