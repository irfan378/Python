import cv2
import os
ROOT = '/root/Desktop/pictures'
FACES = '/root/Desktop/faces'
TRAIN = '/root/Desktop/training'
def detect(srcdir=ROOT,tgtdir=FACES,train_dir=TRAIN):
    #Iterate over the JPG files in the source directory
    for fname in os.listdir(srcdir):
        if not fname.upper().endswith(".JPG"):
            continue
        fullname = os.path.join(srcdir, fname)
        newname = os.path.join(tgtdir, fname)
        # read the image using openCV
        img = cv2.imread(fullname)
        if img is None:
            continue
if __name__ =='__main__':
    detect()