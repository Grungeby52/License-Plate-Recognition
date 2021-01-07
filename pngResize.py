from PIL import Image

img = Image.open('3.png').convert('LA') # image extension *.png,*.jpg

new_width  = 240
new_height = 80
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('3_lp.png') # format may what you want *.png, *jpg, *.gif