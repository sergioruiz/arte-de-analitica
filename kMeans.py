# kMeans.py
# Sergio Ruiz Loza
# October 2020
# TC1002S: Herramientas Computacionales: El Arte de la Analítica

import random

def distance2(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dx2 = dx * dx
    dy2 = dy * dy
    return dx2 + dy2

def kMeans(data, centroids):
    centroidsAsKeys = []
    for c in centroids:
        centroidsAsKeys.append(str(c))

    #centroidsDict = dict.fromkeys(centroidsAsKeys, [])  # NO!
    centroidsDict = {k:[] for k in centroidsAsKeys}
    
    # Data by closest center:
    for d in data:
        closestCentroid = centroids[0]
        smallestD = distance2(d, closestCentroid)
        for c in centroids:
            dist = distance2(d, c)
            if dist < smallestD:
                smallestD = dist
                closestCentroid = c
        centroidsDict[str(closestCentroid)].append(d)
        #print("Appended",d,"to",str(closestCentroid))
    #print()   
    return centroidsDict


def updateCentroids(theDict):
    newCentroids = []
    for key, pointsList in theDict.items():
        oldCentroid = key
        newCentroid = [pointsList[0][0], pointsList[0][1]]
        for p in pointsList:
            newCentroid[0] = newCentroid[0] + p[0] / 2.0
            newCentroid[1] = newCentroid[1] + p[1] / 2.0
        #print("old:",oldCentroid,"new:",newCentroid)
        newCentroids.append(newCentroid)
    return newCentroids


def initCentroids(data, k):
    # Choose k random centroids from data:
    usedIndices = []
    centroidsAsKeys = []
    centroids = []
    for c in range(k):
        index = random.randrange(len(data))
        while index in usedIndices:
            index = random.randrange(len(data))
        usedIndices.append(index)
        centroid = data[index]
        centroids.append(centroid)
        centroidsAsKeys.append(str(centroid))
    #centroidsDict = dict.fromkeys(centroidsAsKeys, [])  # NO!
    centroidsDict = {k:[] for k in centroidsAsKeys}      # YES!
    
    # Data by closest center:
    for d in data:
        closestCentroid = centroids[0]
        smallestD = distance2(d, closestCentroid)
        for c in centroids:
            dist = distance2(d, c)
            if dist < smallestD:
                smallestD = dist
                closestCentroid = c
        centroidsDict[str(closestCentroid)].append(d)
        #print("Appended",d,"to",str(closestCentroid))
    #print()   
    return centroidsDict

data = []
for i in range(10):
    point = [random.uniform(-10.0, 10.01), random.uniform(-10.0, 10.01)]
    data.append(point)
print("Initial data:")
print(data)
print()
cd = initCentroids(data, 2)

print("First round:")
for key, value in cd.items():
    print(key)
    print(value)
    print()
print()

for i in range(5):
    nc = updateCentroids(cd)
    print("New centers:")
    print(nc)
    
    print()
    
    cd = kMeans(data, nc)
    print("Dictionary:")
    for key, value in cd.items():
        print("KEY:")
        print(key)
        print("VALUE:")
        print(value)
        print()
    print()
