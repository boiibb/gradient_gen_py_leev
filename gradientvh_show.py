#    Python Program : "Gradient function use" by Leevaille Galet.
#    Creation Date 11/01/2022        Location : Nates, France
#    Using Python 3.10 and Atom Text Editor
#    Program Version : 0.1
#    Language : English
#
#    VAR LEXICON
#    ID    TYPE        ROLE            CONSTANT OR NOT
import PIL.Image as ImgP
import numpy as np
from gradientvhf_0_2 import grdpil

width = 12*100
height = 8*100
img = ImgP.new('RGB',(width,height),(0,0,0))
img = grdpil(img,'h',(99,245,255),(0,0,0),height,int(width/2),(0,0))
img = grdpil(img,'h',(0,0,0),(212,171,241),height,int(width/2),(0,int(width/2)))
img.show()
