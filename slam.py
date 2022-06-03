#!/usr/local/bin/python3
import cv2
import pygame
from matplotlib import pyplot as plt
#import sdl2.ext

video_path = "/Users/prashantramnani/Projects/slam/test.mp4"
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

H = 2160//4
W = 3840//4

pygame.init()

#sdl2.ext.init()
#window = sdl2.ext.Window("Hello World!", size=(640, 480))
#window.show()

screen = pygame.display
surface = screen.set_mode([W, H])

orb = cv2.ORB_create()

def process_frame(frame):
    frame = cv2.resize(frame, (W, H))
    #frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    kp = orb.detect(frame,None)
    kp, des = orb.compute(frame, kp)
    img2 = cv2.drawKeypoints(frame, kp, None, color=(0,255,0), flags=0)
    plt.imshow(img2), plt.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    surf = pygame.surfarray.make_surface(frame)
    surface.blit(surf, (0,0))
    screen.update()

if __name__ == "__main__":
    cap = cv2.VideoCapture(video_path)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break

