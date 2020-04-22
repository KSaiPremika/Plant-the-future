#import tensorflow as tf


#print(tf.__version__)


import matplotlib
matplotlib.use('Agg')
import matplotlib.image as Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from PIL import Image
import numpy as np
import pandas as pd


import os
import shutil


def getFiles(index):

    other8Images = os.listdir('datasets/areas/'+str(index)+'/img/')
    print(other8Images)
    centerImage = ''
    for f in os.listdir('datasets/areas/img'):
        if f.split('_')[0] == str(index):
            centerImage = f
            break
    print(centerImage)

    other8ImagesAnnos = os.listdir('datasets/areas/'+str(index)+'/anno/')
    print(other8ImagesAnnos)
    centerImageAnno = ''
    for f in os.listdir('datasets/areas/anno'):
        if f.split('_')[0] == str(index):
            centerImageAnno = f
            break
    print(centerImageAnno)

    return dict({'other8Images':other8Images,'centerImage':centerImage,'other8ImagesAnnos':other8ImagesAnnos,'centerImageAnno':centerImageAnno})

#other8Images,centerImage = getFiles(75)

def copyImages(index,other8Images,centerImage):

    if str(index) not in os.listdir('static/images/'):
        os.mkdir('static/images/'+str(index))

    count = 0
    for i,img in enumerate(other8Images):

        if i==4:#centerImage
            shutil.copy('datasets/areas/img/' + centerImage,
                        'static/images/' + str(index) + '/' + str(count + 1) + '.png')
            count+=1
        shutil.copy('datasets/areas/'+str(index)+'/img/'+img,'static/images/'+str(index)+'/'+str(count+1)+'.png')

        count+=1


#copyImages(75,other8Images,centerImage)

def getPlottedImages(index):

    return os.listdir('static/images/'+str(index))

#print(getPlottedImages(75))


def copyToDes(index):
    dataDict = getFiles(index)
    treesAndArea = []

    if str(index) not in os.listdir('static/images/'):
        os.mkdir('static/images/'+str(index))

    count = 0
    for i, imageData in enumerate(zip(dataDict['other8Images'],dataDict['other8ImagesAnnos'])):

        if i == 4:  # centerImage
            treeCount, totalArea = display_image_in_actual_size('datasets/areas/img/'+dataDict['centerImage'],
                                         'datasets/areas/anno/'+dataDict['centerImageAnno'],
                                         'static/images/' + str(index) + '/' + str(count + 1) + '.png')
            treesAndArea.append(dict({'treeCount':treeCount,'totalArea':totalArea}))

            count += 1
        treeCount, totalArea = display_image_in_actual_size('datasets/areas/' + str(index) + '/img/' + imageData[0],
                                     'datasets/areas/' + str(index) + '/anno/' + imageData[1],
                                     'static/images/' + str(index) + '/' + str(count + 1) + '.png')
        treesAndArea.append(dict({'treeCount': treeCount, 'totalArea': totalArea}))

        count += 1

    return treesAndArea




def display_image_in_actual_size(im_path, annoPAth, saveAs):

    data = pd.read_csv(annoPAth, sep=" ", header=None)
    data.columns = ['class', 'x', 'y', 'w', 'h']

    dpi = 80
    im_data = plt.imread(im_path)
    height, width, depth = im_data.shape
    print("Image shape :", im_data.shape)

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    treeCount = 0
    totalArableArea = []
    scaleFactor = (241.32 * 109.79) / (width * height)
    scaleFactorWidth = 241.32 / width
    scaleFactorHeight = 109.79 / height

    print(scaleFactor)

    for i in range(len(data)):
        # print(data.iloc[i,:])
        cls = int(data.iloc[i, :]["class"])
        x = float(data.iloc[i, :]["x"])
        y = float(data.iloc[i, :]["y"])
        w = float(data.iloc[i, :]["w"])
        h = float(data.iloc[i, :]["h"])
        # print("class :",data.iloc[i,:]["class"])
        # print("x :",float(data.iloc[i,:]["x"]))
        # print("y :",float(data.iloc[i,:]["y"]))
        # print("w :",float(data.iloc[i,:]["w"]))
        # print("h :",float(data.iloc[i,:]["h"]))

        centerX = x * width
        centerY = y * height

        rectWidth = w * width
        rectHeight = h * height

        rectX = centerX - rectWidth / 2
        rectY = centerY - rectHeight / 2

        if cls == 0:
            rect = Rectangle((rectX, rectY), rectWidth, rectHeight, linewidth=2, fill=False, color='purple')
            treeCount += 1
        else:
            rect = Rectangle((rectX, rectY), rectWidth, rectHeight, linewidth=2, fill=False, color='blue')
            totalArableArea.append((rectWidth * scaleFactorWidth * rectHeight * scaleFactorHeight))

        # draw the box
        ax.add_patch(rect)

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    #plt.show()
    fig.savefig(saveAs)
    plt.close('all')

    return treeCount, sum(totalArableArea)




#print(copyToDes(0))


