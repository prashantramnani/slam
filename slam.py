#!/usr/local/bin/python3
import cv2
import pygame
import sdl2.ext

video_path = "/Users/prashantramnani/Projects/slam/test.mp4"
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

H = 2160//4
W = 3840//4

pygame.init()

sdl2.ext.init()
window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()

screen = pygame.display
surface = screen.set_mode([W, H])

def process_frame(frame):
    frame = cv2.resize(frame, (W, H))
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
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

