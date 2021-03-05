from PIL import Image
import sys

def getTop(im):
    width = im.size[0]
    height = im.size[1]
    for i in range(0, height):
        for j in range(0, width):
            if (im.getpixel((j, i))) == 0:
                return  i

def getBottom(im):
    width = im.size[0]
    height = im.size[1]
    for i in range(height-1, 0,-1):
        for j in range(0, width):
            if (im.getpixel((j, i))) == 0:
                return  i

def getLeft(im):
    width = im.size[0]
    height = im.size[1]
    n=sys.maxsize
    for i in range(0, height):
        for j in range(0, width):
            if (im.getpixel((j, i))) == 0:
                if(n>j):
                    n=j
                break
    return n

def getRight(im):
    width = im.size[0]
    height = im.size[1]
    left=getLeft(im)+1
    for j in range(left, width):
        det = True
        for i in range(0, height):
            if (im.getpixel((j, i))) == 0:
                det=False
                break
        if det:
            return j

def difference(im1,im2):
    n=0
    a1=0
    a2=0
    width = im1.size[0]
    height = im1.size[1]
    #check pixel by pixel
    for i in range(0, height):
        for j in range(0, width):
            n=n+3.5*abs(im1.getpixel((j, i))-im2.getpixel((j, i)))
    #check row by row
    for i in range(0, height):
        h1=0
        h2=0
        for j in range(0, width):
            h1=h1+abs(im1.getpixel((j, i)))
            h2=h2+abs(im2.getpixel((j, i)))
        n = n + 0.1 * abs(h1 - h2)
    #check column by column
    for j in range(0, width):
        v1=0
        v2=0
        for i in range(0, height):
            v1=v1+abs(im1.getpixel((j, i)))
            v2=v2+abs(im2.getpixel((j, i)))
        n = n + 0.1 * abs(v1 - v2)
    #check the symmetry property
    for i in range(0, int(height/2)):
        for j in range(0, width):
            a1 = a1 + abs(im1.getpixel((j, i)))
            a2 = a2 + abs(im2.getpixel((j, i)))
    for i in range(int(height/2),height):
        for j in range(0, width):
            a1 = a1 - abs(im1.getpixel((j, i)))
            a2 = a2 - abs(im2.getpixel((j, i)))

    n = n + 0.5 * abs(a1-a2)
    return n

#get sample
n=Image.open("source/0.png")
n=n.convert("1")
n0=n.resize((51,78))
n=Image.open("source/1.png")
n=n.convert("1")
n1=n.resize((51,78))
n=Image.open("source/2.png")
n=n.convert("1")
n2=n.resize((51,78))
n=Image.open("source/3.png")
n=n.convert("1")
n3=n.resize((51,78))
n=Image.open("source/4.png")
n=n.convert("1")
n4=n.resize((51,78))
n=Image.open("source/5.png")
n=n.convert("1")
n5=n.resize((51,78))
n=Image.open("source/6.png")
n=n.convert("1")
n6=n.resize((51,78))
n=Image.open("source/7.png")
n=n.convert("1")
n7=n.resize((51,78))
n=Image.open("source/8.png")
n=n.convert("1")
n8=n.resize((51,78))
n=Image.open("source/9.png")
n=n.convert("1")
n9=n.resize((51,78))

#get target image
img=Image.open("source/Test4.png")
img.show()
#change binarize image
img=img.convert("1")
width = img.size[0]
height = img.size[1]

while(True):
    if (getLeft(img)==sys.maxsize):
        break
    #seperate different digit
    box = (getLeft(img), getTop(img), getRight(img), getBottom(img))
    num = img.crop(box)
    #resize image to the same size as template
    num=num.resize((51,78))
    #compare with the template
    result = 0
    n = difference(n0,num)
    if n>difference(n1,num):
        n=difference(n1,num)
        result = 1
    if n>difference(n2,num):
        n=difference(n2,num)
        result = 2
    if n>difference(n3,num):
        n=difference(n3,num)
        result = 3
    if n>difference(n4,num):
        n=difference(n4,num)
        result = 4
    if n>difference(n5,num):
        n=difference(n5,num)
        result = 5
    if n>difference(n6,num):
        n=difference(n6,num)
        result = 6
    if n>difference(n7,num):
        n=difference(n7,num)
        result = 7
    if n>difference(n8,num):
        n=difference(n8,num)
        result = 8
    if n>difference(n9,num):
        n=difference(n9,num)
        result = 9
    print(result,end=" ")
    box=(getRight(img),0,width,height)
    img=img.crop(box)
    width = img.size[0]
    height = img.size[1]

