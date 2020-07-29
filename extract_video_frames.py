import os
import cv2
import time
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Extract video frames")
    parser.add_argument('--input_video', type=str, default='input.mp4', help='Input video file name')
    parser.add_argument('--output_filetype', type=str, default='png', help='Output image file type')
    parser.add_argument('--output_basename', type=str, default='frame', help='Output image base name')
    parser.add_argument('--output_folder', type=str, default=None, help='Output folder')
    return parser

def main():
    # Parser
    parser = build_parser()
    options = parser.parse_args()

    output_folder = options.output_folder
    if (options.output_folder == None):
        output_folder = options.input_video.split('.')[0] + "_frames"

    # Extract height, width and FPS of a video
    vidcap = cv2.VideoCapture( options.input_video )
    W, H, fps = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH), vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT), vidcap.get(cv2.CAP_PROP_FPS)

    # Make the output folder
    def _make_dir( path ):
        if not os.path.exists( path ):
            os.makedirs( path )

    _make_dir(output_folder)

    # Extract the frames of a video and save to the specified output folder
    success, image = vidcap.read()
    count = 1
    success = True
    while success:
        filename = options.output_basename + str(count) + "." + options.output_filetype
        filepath = os.path.join(output_folder, filename)

        # Save Image
        cv2.imwrite(filepath, image)

        # Read Video - again
        success, image = vidcap.read()
        count += 1

if __name__ == "__main__":
    main()
