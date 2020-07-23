import cv2

filepath = "../static/img/baga.jpeg"
img =cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()