import cv2 as cv
import numpy as np

#videos utilizados para o teste
capture1 = cv.VideoCapture('video1.mp4)
capture2 = cv.VideoCapture('video2.mp4')

def rescaleFrame(frame, scale=0.47):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def processVideo(video,location):
    sum = 0
    frames = 0

    while True:
        on, frame = video.read()
        if on == False:
            break

        frame = rescaleFrame(frame)
        
        '''
        # valores padrões
        lower_green = np.array([15, 40, 15])
        upper_green = np.array([60, 255, 60])
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        '''

        # valores testes
        lower_green = np.array([10, 25, 10])
        upper_green = np.array([75, 255, 75])
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        green_mask = cv.inRange(hsv, lower_green, upper_green)
        mask = cv.bitwise_and(frame, frame, mask=green_mask)
        maskGray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)


        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


        sum = sum + cv.countNonZero(maskGray)
        frames += 1
        result = sum/frames
        
    print(location,'%.2f' % result)
    
processVideo(capture1,'centro2: ')
processVideo(capture2,'upf: ')

capture1.release()
cv.destroyAllWindows()
