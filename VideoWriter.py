import cv2
import numpy as np

def save_video( save_name, frames, width, height, fps, gray=False ):

    # Define codec and create VideoWrite object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    if (gray == False):
        vout = cv2.VideoWriter(save_name, fourcc, fps, (width,height))
    else:
        vout = cv2.VideoWriter(save_name, fourcc, fps, (width,height), 0)

    # Write the video
    for frame in frames:
        vout.write(frame)