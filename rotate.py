from PIL import Image

try:
    
    img=Image.open("IMG_20180330_134810.jpg")
    img=img.rotate(180)
    img.save("image.jpg")
except IOError:
    pass
