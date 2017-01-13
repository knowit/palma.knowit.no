'''

Simple collage generator based on the images in the "pics" folder.

Usage:
   python3 collage.py > tmp.html ; open tmp.html

'''
from glob import glob
from os.path import join

import random

if __name__ == '__main__':


    pics = glob(join('pics/*.*'))
    random.shuffle(pics)

    s = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
        </head>
    <body>
    '''

    for pic in pics:
        s = s + '<img src="'+pic+'" style="max-width: 200px;" /> \n'

    s += '''
        </body>
    </html>'''

    print(s)
