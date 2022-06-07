import cv2
import numpy as np

class FeatureExtractor:
    def __init__(self, features_to_retain = 100):
        self.orb = cv2.ORB_create(features_to_retain)

    def fragmentFrame(self, frame):
        pass

    def orbExtract(self, frame):
       kp = self.orb.detect(frame, None) 

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
       kpoint = []
       for p in kp:
           kpoint.append(p.pt)
       return kpoint

    def goodFeaturesExtract(self, frame):
       kp = cv2.goodFeaturesToTrack(np.mean(frame, axis=2).astype(np.uint8),
            5000, qualityLevel=0.05, minDistance=2)

       return np.int0(kp)
     
