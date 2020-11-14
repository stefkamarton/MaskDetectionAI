
import cv2

URL = "http://kifi.sze.hu/securitycam/stream/00a52a0737cb5eba346a3fa19598fc03/index.m3u8"

try:
    ## ha az URL helyett 0-t adsz meg akkor a HW listában szereplő első kamera alapján készül a kép. Laptop esetén ez a webkamera.
    cap = cv2.VideoCapture(URL)


    if not (cap.isOpened()):
        print("Could not open video device")

    scale_percent = 60 # percent of original size

    while(True):
        ret, frame = cap.read()

        
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)


        cv2.imshow("Kamera_kep",resized)
        
        ## a "q" billentyű lenyomására kilép
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except:
    print ("Ex_")