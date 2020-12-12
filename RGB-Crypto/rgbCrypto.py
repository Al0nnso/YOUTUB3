import sys
import string
import os
from PIL import Image
from PIL import ImageColor
import numpy
import math

def debug(array):
	print("########### first 100 ###########")
	print(array[0:100])
	print("########### last 100 ###########")
	print(array[len(array)-100:len(array)-1])

def encode(filename,delete):
	print("encoding... "+filename)
	file = open(filename, "rb")
	data=file.read()

	color2=[]
	color_pos=0
	sqr=int(math.sqrt(len(data)/3))

	if(int(sqr)<sqr):
	    sqr=int(sqr)+1

	for i in range(sqr):
	    color_edge=[]
	    for j in range(0,sqr):
	        if len(data)-3>color_pos:
	            color_edge.append((data[color_pos],data[color_pos+1],data[color_pos+2]))
	            color_pos=color_pos+3
	        elif len(data)-2==color_pos:
	            color_edge.append((data[color_pos],data[color_pos+1],255))
	            color_pos=color_pos+2
	        elif len(data)-1==color_pos:
	            color_edge.append((data[color_pos],256,256))
	            color_pos=color_pos+1
	        else:
	            color_edge.append((256,256,256))
	    color2.append(color_edge)

	array = numpy.array(color2, dtype=numpy.uint8)
	new_image = Image.fromarray(array)
	new_image.save(filename+'.png')
	file.close()
	if delete:
		os.remove(filename)
		print("file removed...")

	print("file encrypted to rgb...")
	print("saved as "+filename+'.png')

def decode(filename,delete):
	red_image = Image.open(filename)
	red_image_rgb = red_image.convert("RGB")
	width, height = red_image.size
	data=[]

	for i in range(width):
	    for j in range(height):
	        pixel=red_image_rgb.getpixel((j,i))
	        #print(pixel)
	        if pixel[0]!=256:
	            #print(pixel[0])
	            data.append(pixel[0])
	        if pixel[1]!=256:
	            #print(pixel[1])
	            data.append(pixel[1])
	        if pixel[2]!=256:
	            #print(pixel[2])
	            data.append(pixel[2])

	#print(data[1])
	#print(filename[0:len(filename)-4])
	f = open(filename[0:len(filename)-4], "wb")
	f.write(bytearray(data))
	f.close()
	if delete:
		os.remove(filename)
		print("file removed...")

	print("file decrypted sucefull...")
	print("saved as "+filename[0:len(filename)-4])


#print('Number of arguments:'+str(len(sys.argv))+'arguments.')
#print('Argument List:'+str(sys.argv))

if len(sys.argv)==3:
	delete=False
	if sys.argv[1]=='decode':
		if len(sys.argv)>=4 and sys.argv[3]=='-del':
			delete=True
		decode(sys.argv[2],delete)
	if sys.argv[1]=='encode':
		if len(sys.argv)>=4 and sys.argv[3]=='-del':
			delete=True
		encode(sys.argv[2],delete)