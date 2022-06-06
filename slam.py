#!/usr/local/bin/python3

import cv2
import pygame
from matplotlib import pyplot as plt
import numpy as np
from surface import Surface
from extractor import FeatureExtractor
#import sdl2.ext

video_path = "/Users/prashantramnani/Projects/slam/test.mp4"
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

H = 2160//4
W = 3840//4

divide_h = 5 
divide_w = 5 

pygame.init()
surface = Surface(W, H)
fe = FeatureExtractor()

'''
sdl2.ext.init()
window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()
'''

def process_frame(frame):
    frame = cv2.resize(frame, (W, H))

    '''
    s_h = frame.shape[0]//divide_h
    s_w = frame.shape[1]//divide_w
    kp_frag = []
    for h in range(0, frame.shape[0], s_h):
        for w in range(0, frame.shape[1], s_w):
            img_frag = frame[h:h+s_h, w:w+s_w]
            kp = orb.detect(img_frag, None)
            for p in kp:
                kp_frag.append((p.pt[0] + w, p.pt[1] + h))    
    '''

    kp = fe.goodFeaturesExtract(frame)
    for p in kp:
        #u, v = map(lambda x : int(round(x)), p)
        u, v = p.ravel()
        print("u {}, v {}".format(u, v))
        cv2.circle(frame, (u, v), color=(0,255,0), radius=2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    surface.paint(frame)


if __name__ == "__main__":
    cap = cv2.VideoCapture(video_path)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break

