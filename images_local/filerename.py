import os
import cv2
##
##count = 0
##rename each file
##for filename in os.listdir("."):
##    name = (str)(count) + ".jpg"
##    os.rename(filename, name)
##    count+=1

#annotation file
file = open("annotations.txt","w")

#code to split images into blocks and annotate
for filename in os.listdir("."):
    frame_small = cv2.imread(filename)
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
    shape = frame_small.shape
    height = shape[0]
    width = shape[1]
    h = 0
    w = 0
    found = False
    while (h+80 <= height) and found == False :
        while (w+105 <= width) and found == False :
            roi_gray = gray[h:h+80, w:w+105]
            cv2.imshow((str)(filename)+"split"+(str)(h)+","+(str)(w)+"--"+(str)(h+80)+","+(str)(w+105), roi_gray)
            waitkey_return = cv2.waitKey(0) 
            if waitkey_return == ord("f") :
                print ("Classified Face")
                file.write("images_local/"+(str)(filename)+","+(str)(w)+","+(str)(h)+","+(str)(w+105)
                           +","+(str)(h+80)+",Face\n")
            elif waitkey_return == ord("g") :
                print ("Classified Gesture")
                file.write("images_local/"+(str)(filename)+","+(str)(w)+","+(str)(h)+","+(str)(w+105)
                           +","+(str)(h+80)+",Gesture\n")
            else :
                print ("Classified DontCare")
            cv2.destroyAllWindows()
            w+=105
        w = 0
        h+=80
file.close()
