import glob
import imageio
import os
import rawpy

if not os.path.exists('./PNG'):
    os.mkdir('PNG')

files = glob.glob(str(os.getcwd()) + '/*.DNG')

for i in files:
    raw = rawpy.imread(i)
    rgb = raw.postprocess()
    newpath = i[:len(i)-12] + 'PNG/' + i[len(i)-12:len(i)-3] + 'png'
    imageio.imwrite(newpath, rgb)
    print(newpath)
