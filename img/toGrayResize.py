import os
from PIL import Image


def main():
    for count, filename in enumerate(os.listdir("/home/san/Downloads/LicensePlateDetector-master/DataSet/img")):
        dst = "0_" + str(count) + ".jpg"
        src = '/home/san/Downloads/LicensePlateDetector-master/DataSet/img/' + filename
        dst = '/home/san/Downloads/LicensePlateDetector-master/DataSet/img/' + dst
        print(filename)
        # rename() function will
        # rename all the files
        img = Image.open(src).convert('LA') # image extension *.png,*.jpg

        new_width  = 240
        new_height = 80
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(filename+'_lp.png') # format may what you want *.png, *jpg, *.gif

if __name__ == '__main__':
    # Calling main() function
    main()