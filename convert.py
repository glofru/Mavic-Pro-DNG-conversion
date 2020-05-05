import argparse
import glob
import os
import sys

import imageio
import rawpy
from PIL import Image

parser = argparse.ArgumentParser(description='Tool for DNG to PNG conversion.')

parser.add_argument('--source', '-s', metavar='', help='Folder where DNG files are')
parser.add_argument('--destination', '-d', metavar='', help='Folder where PNG files are saved')

parser.add_argument('--jpg-to-tiff', '-j', action='store_true', help='Variation to convert JPG files to TIFF files')

args = parser.parse_args()

if args.source is None:
    source = str(os.getcwd())
    print("Source path is current path " + source)
else:
    source = str(args.source)
    if not os.path.exists(source):
        sys.exit(args.source + ' path not found')

if args.destination is None:
    dest = input('Where do you want to save your files? [' + source + '/convert]: ')
    if len(dest) == 0:
        dest = source + '/convert'
else:
    dest = str(args.destination)

if not os.path.exists(dest):
    if dest != source + '/convert':
        b = input(dest + ' does not exists. Do you want to create it? [yes]: ')

        if len(b) != 0 and b.lower()[0] == 'n':
            sys.exit()

    os.makedirs(dest)

count = 0

print('Elaborating...')

if args.jpg_to_tiff:
    files = glob.glob(source + '/*.jpg', source + '/*.jpeg', source + '/*.JPG', source + '/*.JPEG')

    if len(files) == 0:
        sys.exit('No JPG files found in ' + source)

    for i in files:
        im = Image.open(i)
        newpath = dest + '/' + i.split('/')[-1][:-3] + 'tiff'
        im.save(newpath)
        count += 1
        print(str(int(count*100/len(files))) + '% ' + str(count) + '/' + str(len(files)) + ': ' + newpath)


else:
    files = glob.glob(source + '/*.DNG', source + '/*.dng')

    if len(files) == 0:
        sys.exit('No DNG files found in ' + source)

    for i in files:
        raw = rawpy.imread(i)
        rgb = raw.postprocess()
        newpath = dest + '/' + i.split('/')[-1][:-3] + 'png'
        imageio.imwrite(newpath, rgb)
        count += 1
        print(str(int(count*100/len(files))) + '% ' + str(count) + '/' + str(len(files)) + ': ' + newpath)

print('Job finished!')
