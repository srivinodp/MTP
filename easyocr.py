import easyocr
import matplotlib.pyplot as plt
reader = easyocr.Reader(['en'])
# print(reader.readtext('/content/aim.png', detail = 0))

from PIL import Image, ImageDraw, ImageFont
def draw_boxes(image, bounds, color = 'red', width = 1):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill = color, width = width)
    return image

f, axarr = plt.subplots(1,5, figsize = (100,100))
for i in range(86,91):
    # axarr[i-86].imshow(draw_boxes(Image.open('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png'), reader.readtext('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png')))
    axarr[i-86].imshow(Image.open('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png'))
    axarr[i-86].axis('off')
    
plt.show()

print()
print()

f, axarr = plt.subplots(1,5, figsize = (100,100))
for i in range(93,98):
    # axarr[i-93].imshow(draw_boxes(Image.open('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png'), reader.readtext('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png')))
    axarr[i-93].imshow(Image.open('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png'))
    axarr[i-93].axis('off')
    
plt.show()

# for i in range(86,100):

#     plt.imshow(draw_boxes(Image.open('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png'), reader.readtext('/content/drive/MyDrive/MTP/train2/X/X'+str(i)+'/image_00001.png')))
#     plt.axis('off')
#     plt.show()
# print(reader.readtext('/content/drive/MyDrive/MTP/train2/X/X69/image_00001.png',detail = 0))
