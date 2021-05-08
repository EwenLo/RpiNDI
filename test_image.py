import cv2
from pysimplendi import NDISender

def  main():
    sender = NDISender("test_image")
    # transparent image [width, height, 4]
    
    # normal image [width, height, 3]
    normal = cv2.imread("test_image.png")

    while True:

        sender.send(normal)
if __name__ == "__main__":
    main()