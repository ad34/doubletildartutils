import os
from pathlib import Path

[f.unlink() for f in Path("./morph/").glob("*") if f.is_file()] 

fp = open("./morph/list.txt","w")

start_img = 0
num_img = 8
epoch = 1500
steps = 96 # optimized for 150 bpm 
fps = 30

def makecmdline(first,second):
    global epoch, steps, fps
    cmd = "python .\morph.py --step " + str(steps) + " --fps " + str(fps) + " -e " + str(epoch) + " -s img_" + str(first) + ".png -t img_" + str(second) + ".png"
    print (cmd)
    return cmd

for i in range(start_img,start_img + num_img):
    j = i + 1
    cmd = makecmdline(i,j)
    os.system(cmd)
    os.rename("./morph/morph.mp4", "./morph/" + str(j) + ".mp4")
    fp.write("file '" + str(j) + ".mp4'" + "\n")
    print("done " + str(j) + ".mp4")

print ("make the video loop")

final = start_img + num_img + 1

cmd = makecmdline(start_img + num_img,final)
os.system(cmd)
os.rename("./morph/morph.mp4", "./morph/" + str(final) + ".mp4")
fp.write("file '" + str(final) + ".mp4'" + "\n")
os.system("cd ./morph")
os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy')
fp.close()