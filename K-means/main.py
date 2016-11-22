# coding=utf-8
from numpy import *

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

# Tmn07
def randInit(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    ran = random.choice(dataSet.shape[0], k, replace=False)
    for x in xrange(k):
        centroids[x,:] = dataSet[ran[x]]
    return centroids

    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    print "init centroids is"
    print(centroids)
    clusterChanged = True
    p = 1
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        # print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
        print ("--------------")
        print "%d times:" % p
        print "centroids is"
        print(centroids)
        tmp = []
        for i in clusterAssment:
            tmp.append(centroids[i[0,0],:])
        tmp_img = array(tmp)
        new_img = tmp_img.astype(uint8).reshape((w,h,3))
        Image.fromarray(new_img).save("K_" + str(p * 100) + ".jpg")
        p+=1
    return centroids, clusterAssment

from PIL import Image

img = Image.open('paojie.jpg', 'r')
origin_img = array(img)

w = origin_img.shape[0]
h = origin_img.shape[1]
img = origin_img.reshape((w*h, 3))

kMeans(img, 4, createCent=randInit)
