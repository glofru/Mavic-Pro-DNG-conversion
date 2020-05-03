import argparse
import glob
import os
import sys

import imageio
import rawpy

parser = argparse.ArgumentParser(description='Tool for DNG to PNG conversion.')

parser.add_argument('--source', '-s', metavar='', help='Folder where DNG files are')
parser.add_argument('--destination', '-d', metavar='', help='Folder where PNG files are saved')

args = parser.parse_args()

if args.source is None:
    source = str(os.getcwd())
    print("Source path is current path " + source)
else:
    source = str(args.source)
    if not os.path.exists(source):
        sys.exit(args.source + ' path not found')

if args.destination is None:
    dest = input('Where do you want to save your PNG files? [' + source + '/PNG]: ')
    if len(dest) == 0:
        dest = source + '/PNG'
else:
    dest = str(args.destination)

if not os.path.exists(dest):
    if dest != source + '/PNG':
        b = input(dest + ' does not exists. Do you want to create it? [yes]: ')

        if len(b) != 0 and b.lower()[0] == 'n':
            sys.exit()

    os.makedirs(dest)

files = glob.glob(source + '/*.DNG')

if len(files) == 0:
    sys.exit('No DNG files found in ' + source)

count = 0

print('Elaborating...')

for i in files:
    raw = rawpy.imread(i)
    rgb = raw.postprocess()
    newpath = dest + '/' + i.split('/')[-1][:-3] + 'png'
    imageio.imwrite(newpath, rgb)
    count += 1
    print(str(int(count*100/len(files))) + '% ' + str(count) + '/' + str(len(files)) + ': ' + newpath)

print('Job finished!')
