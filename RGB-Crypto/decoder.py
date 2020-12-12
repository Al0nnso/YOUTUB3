from PIL import Image
import binascii
import struct
import array
import os

filename=input("file to decode: ")

red_image = Image.open(filename)
red_image_rgb = red_image.convert("RGB")

#rgb_pixel_value = red_image_rgb.getpixel((10,15))

width, height = red_image.size

data=[]

#print(red_image_rgb.getpixel((0,1)))

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

print(data[1])

#print(data[len(data)-100:len(data)-1])
#print(bytearray(data))

#data_bytes = chr(data)
#data_bytes=struct.pack("b"*len(data),*data)
#print(data_bytes)

def debug(array):
    print("########### first 100 ###########")
    print(array[0:100])
    print("########### last 100 ###########")
    print(array[len(array)-100:len(array)-1])

#debug(data)
print(filename[0:len(filename)-4])
#print(bytes_b)
f = open(filename[0:len(filename)-4], "wb")

f.write(bytearray(data))
#f.write(bytes_b)
f.close()
os.remove(filename)

print("file decrypted sucefull...")
print("saved as "+filename[0:len(filename)-4])
