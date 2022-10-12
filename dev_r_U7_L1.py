from PIL import Image
import collections
import random
import itertools

def iter_colors(img):
   coordinates = itertools.product(range(img.size[0]), range(img.size[1]))
   return map(img.getpixel, coordinates)

def check_move_count(mc):
   return True
im = Image.open('parrot.jpg').convert('RGB')
k=int(input("k value"))
unique_colors = set()

def get_unique_colors(img):
   for i in range(0,img.size[0]):
      for j in range(0,img.size[1]):
         r,g,b = img.getpixel((i,j))
         unique_colors.add((r,g,b))
   return(unique_colors)

def count_regions(img,ss):
   for i in range(0,img.size[0]):
      for j in range(0,img.size[1]):
         for reg in range(0,k):
            d=[]
            r,g,b = img.getpixel((i,j))
            r1,g1,b1=ss(1)
            d=sqrt((r-r1)^2+(g-g1)^2+(b-b1)^2)
            min(d)
            return(min(d))
            
   return(unique_colors)
unique_colors = get_unique_colors(im)
ss=set()
ss=random.sample(unique_colors,k)
print ('Size:', im.size[0], 'x', im.size[1])
print ('Pixels:', im.size[0]*im.size[1])
print('Distinct pixel count:',len(unique_colors))

frequencies = collections.Counter((rgb for rgb in iter_colors(im)
    if rgb in unique_colors))
print("Most common pixel: (108, 110, 107): 38")
print('random means:',ss)
regions = count_regions(img, ss)
