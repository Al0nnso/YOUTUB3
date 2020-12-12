import string
import os
from PIL import Image
from PIL import ImageColor
import numpy
import math

#filename="suus.png"
filename=input("file to encode: ")

file = open(filename, "rb")

data=file.read()

#for i in range(5000):
#    print(chr(xux[i]))
#    data+=chr(xux[i])

#print(list(data)[0:100])

def debug(array):
    print("########### first 100 ###########")
    print(array[0:100])
    print("########### last 100 ###########")
    print(array[len(array)-100:len(array)-1])

#debug(list(data))

color2=[]
color_pos=0
#print(len(data)/3)
#print(int(math.sqrt(len(data)/3)))
sqr=int(math.sqrt(len(data)/3))

if(int(sqr)<sqr):
    sqr=int(sqr)+1

for i in range(sqr):
    color_edge=[]
    for j in range(0,sqr):
        if len(data)-3>color_pos:
            #print(color_pos)
            color_edge.append((data[color_pos],data[color_pos+1],data[color_pos+2]))
            #print((data[j],data[j+1],data[j+2]))
            color_pos=color_pos+3
        elif len(data)-2==color_pos:
            color_edge.append((data[color_pos],data[color_pos+1],255))
            #print((data[color_pos],data[color_pos+1],255))
            color_pos=color_pos+2
        elif len(data)-1==color_pos:
            color_edge.append((data[color_pos],256,256))
            #print((data[color_pos],255,255))
            color_pos=color_pos+1
        else:
            color_edge.append((256,256,256))
    #print("#######################################")
    color2.append(color_edge)
#print(color2)

array = numpy.array(color2, dtype=numpy.uint8)

new_image = Image.fromarray(array)
new_image.save(filename+'.png')
os.remove(filename)

print("file encrypted to rgb...")
print("saved as "+filename+'.png')
