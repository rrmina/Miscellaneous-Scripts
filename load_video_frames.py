import os
import cv2
import time
import argparse

def load_video( input_video, gray=False ):
    vidcap = cv2.VideoCapture( input_video )

    frame_list = []

    success, image = vidcap.read()
    if (len(image.shape) == 2):
        h,w = image.shape
    else:
        h,w,c = image.shape

    while success:
        if (gray):
            frame_list.append( cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).reshape(1,h,w) )
        else:
            frame_list.append( cv2.cvtColor(image, cv2.COLOR_BGR2RGB).reshape(1,h,w,c) )
        success, image = vidcap.read()

    return np.concatenate(frame_list, axis=0)