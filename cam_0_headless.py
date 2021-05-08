#pip install pysimplendi
from pysimplendi import NDISender
from pysimplendi import NDIReceiver
import cv2
import numpy as np
#from imutils.video import FPS
#from imutils.video import FileVideoStream


def main():
    sender = NDISender("Cam_0")
    # transparent image [width, height, 4]



    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #cap.set(cv2.CAP_PROP_SETTINGS, 1)

   # fps = FPS().start()
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cap.set(cv2.CAP_PROP_FPS, 60)
            
    #frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while(True):
        # Capture frame-by-frame
        
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



       # print(frameWidth)
        #print(frameHeight)

            
        sender.send(frame)
        #fps.update()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    #cv2.destroyAllWindows()
    
    


#i = 0

#while True:
#    i = (i + 1) % 30
#    print(i)
#    if i > 15:
#        # send transparent image
#        sender.send(transparent)
#    else:
#        # send image
#        sender.send(normal)

if __name__ == "__main__":
    
    main()
    
#