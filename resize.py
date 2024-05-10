import cv2
img  = cv2.imread('/home/davinci/Desktop/python/openCV/OpenCV-Tutorials-main/assets/logo.jpg',1)
img = cv2.resize(img,(300,300))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()