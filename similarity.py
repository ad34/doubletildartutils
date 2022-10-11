import cv2
import math
import numpy as np
import glob
import shutil
import random
from skimage.metrics import structural_similarity
from pathlib import Path

[f.unlink() for f in Path("./sorted/").glob("*") if f.is_file()] 

img_array = []
sorted_list = []
i = 0
map = {}
base_folder = 'Images'

for filename in glob.glob('./' + base_folder + '/*.png'):
    img_ref = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    if i == 0:
        shutil.copy(filename, './sorted/img_0.png')
    img_ref = cv2.resize(img_ref, (576,1024), interpolation = cv2.INTER_AREA)
    i = i + 1
    bestscore = -1
    bestmatchfile = ''
    for otherfile in glob.glob('./' + base_folder + '/*.png'):
        if otherfile == filename:
            continue
        if otherfile in sorted_list:
            continue
        img = cv2.imread(otherfile,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (576,1024), interpolation = cv2.INTER_AREA)
        # Compute SSIM between two images
        score, diff = structural_similarity(img, img_ref,  full=True)
        if score>bestscore:
            bestmatchfile = otherfile
    print ("best match " + bestmatchfile + " score " + str(score))
    shutil.copy(bestmatchfile, './sorted/img_' + str(i) + '.png')
    sorted_list.append(bestmatchfile)
    




