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

compare_format = (576,1024)
#compare_format = (512,512)

files = glob.glob('./' + base_folder + '/*.png')

ref_file = ''

for i in range(len(files)):
    if i == 0:
        ref_file = files[i]
        img_ref = cv2.imread(ref_file,cv2.IMREAD_GRAYSCALE)
        shutil.copy(ref_file, './sorted/img_0.png')
        print("initial ref_file " + ref_file)
        img_ref = cv2.resize(img_ref, compare_format, interpolation = cv2.INTER_AREA)
    bestscore = -1
    bestmatchfile = ''
    for otherfile in glob.glob('./' + base_folder + '/*.png'):
        if otherfile == ref_file:
            continue
        if otherfile in sorted_list:
            continue
        img = cv2.imread(otherfile,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, compare_format, interpolation = cv2.INTER_AREA)
        # Compute SSIM between two images
        score, diff = structural_similarity(img, img_ref,  full=True)
        if score>bestscore:
            bestmatchfile = otherfile
    print ("best match " + bestmatchfile + " score " + str(score))
    shutil.copy(bestmatchfile, './sorted/img_' + str(i) + '.png')
    ref_file = bestmatchfile
    img_ref = cv2.imread(ref_file,cv2.IMREAD_GRAYSCALE)
    img_ref = cv2.resize(img_ref, compare_format, interpolation = cv2.INTER_AREA)
    print("new ref_file " + ref_file)
    sorted_list.append(bestmatchfile)
    




