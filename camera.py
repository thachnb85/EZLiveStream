import cv2
import time

#sharpening image
import numpy as np
#kernel
K = np.array(  [[-1,-1,-1,-1,-1],
                [-1, 2, 2, 2,-1],
                [-1, 2, 8, 2,-1],
                [-1, 2, 2, 2,-1],
                [-1,-1,-1,-1,-1]]) / 8.0

class VideoCamera(object):
    def __init__(self):
        print "[INFO] warming up..."
        time.sleep(3)
        self.video = cv2.VideoCapture(0)
        #width height FPS
        self.video.set(3, 1280)
        self.video.set(4, 720)
        self.video.set(5, 2)
    
    def __del__(self):
        print "[INFO] Release Camera..."
        self.video.release()
    
    def get_frame(self):
        print "[INFO] Capture Frame..."
        success, frame = self.video.read()
        frame_sharpen = cv2.filter2D(frame, -1, K)
        ret, jpeg = cv2.imencode('.jpg', frame_sharpen)
        return jpeg.tostring()