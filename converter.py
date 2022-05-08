# Convert images to csv format

# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2 as cv2
import numpy as np
import os

# get the path/directory
set1 = "<PATH_TO_DATSET"
set2 = "<PATH_TO_DATSET"
pikCount = 0
pikTestCount = 0
raiCount = 0
raiTestCount = 0
count = 0
f = open("pinput.csv", "a")
f1 = open("pinput_test.csv", "a")

for x in range(2):
    count = 0
    folder_dir = ""
    if x == 0:
        folder_dir = set1
    else:
        folder_dir = set2

    for images in os.listdir(folder_dir):

        # check if the image ends with png
        if (images.endswith(".jpg")):

            img = cv2.imread(folder_dir + "/" + images, cv2.IMREAD_UNCHANGED)
            width = 100
            height = 100
            dim = (width, height)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            img1 = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            plt.imshow(img1)
            imageMat_reshape = img1.flatten()
            try:
                if count <= 283:
                    np.savetxt(f, [imageMat_reshape], delimiter=',')
                    if x == 0:
                        pikCount += 1
                    else:
                        raiCount += 1
                else:
                    np.savetxt(f1, [imageMat_reshape], delimiter=',')
                    if x == 0:
                        pikTestCount += 1
                    else:
                        raiTestCount += 1
                count += 1
            except ValueError as v:
                print(v)

print("Pika: ", "Input - ", pikCount, "Test - ", pikTestCount)
print("Rai: ", "Input - ", raiCount, "Test - ", raiTestCount)
