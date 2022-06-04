#!/usr/local/bin/python3
import cv2
import pygame
from matplotlib import pyplot as plt
import numpy as np
#import sdl2.ext

video_path = "/Users/prashantramnani/Projects/slam/test.mp4"
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

H = 2160//4
W = 3840//4

divide_h = 5 
divide_w = 5 

pygame.init()

#sdl2.ext.init()
#window = sdl2.ext.Window("Hello World!", size=(640, 480))
#window.show()

screen = pygame.display
surface = screen.set_mode([W, H])

orb = cv2.ORB_create(100)

def paint(frame):
    surf = pygame.surfarray.make_surface(frame)
    surface.blit(surf, (0,0))
    screen.update()

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

    #kp = cv2.goodFeaturesToTrack(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 5000, qualityLevel=0.01, minDistance=3)  
    kp = cv2.goodFeaturesToTrack(np.mean(frame, axis=2).astype(np.uint8), 5000, qualityLevel=0.05, minDistance=2)
    corners = np.int0(kp)
    for p in kp:
        #u, v = map(lambda x : int(round(x)), p)
        x, y = p.ravel()
        cv2.circle(frame, (x, y), color=(0,255,0), radius=2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    paint(frame)


if __name__ == "__main__":
    cap = cv2.VideoCapture(video_path)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break

