# kMeans.py
# Sergio Ruiz Loza
# October 2020
# TC1002S: Herramientas Computacionales: El Arte de la Analítica

import random

def distance2(a, b):
    sum = 0
    for i in range(len(b)):
        sum += (b[i] - a[i])**2
    return sum

    '''
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dx2 = dx * dx
    dy2 = dy * dy
    return dx2 + dy2
    '''

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
        components = len(pointsList[0])
        newCentroid = []
        for c in range(components):
            newCentroid.append(pointsList[0][c])   
        #newCentroid = [pointsList[0][0], pointsList[0][1]]
        for p in pointsList:
            for c in range(components):
                newCentroid[c] = newCentroid[c] + p[c] / 2.0
            #newCentroid[0] = newCentroid[0] + p[0] / 2.0
            #newCentroid[1] = newCentroid[1] + p[1] / 2.0
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

data = [
[-2.273284107, 1.898485259],
[9.285248345,  9.528708054],
[-8.803332803,-1.148882298],
[4.925078368,  2.331671642],
[2.586415013,  1.28128069],
[8.084455493, -0.9130888578],
[0.9276023375, 0.5423613255],
[-7.445467699,-0.7961183742],
[-4.258454366, 9.335165888],
[1.554880819, -2.925452212]]

#data=[]
#for i in range(10):
#    point = [random.uniform(-10.0, 10.01), random.uniform(-10.0, 10.01)]
#    data.append(point)
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

for i in range(3):
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
