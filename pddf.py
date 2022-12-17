from PIL import Image

image_1 = Image.open(r'C:\Users\himaj\Ctrl-alt-del\contact.png')
image_2 = Image.open(r'C:\Users\himaj\Ctrl-alt-del\css.png')


im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')


image_list = [im_2]

im_1.save(r'C:\Users\himaj\Ctrl-alt-del\images.pdf', save_all=True, append_images=image_list)