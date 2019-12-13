import numpy
import random

drugVector=numpy.loadtxt("drug.txt")
targetVector=numpy.loadtxt("target.txt")
interactionMetirx=numpy.loadtxt("interactionmetrix.txt")
print(drugVector.shape)
print(targetVector.shape)
print(interactionMetirx.shape)
positivenum=0
positivetrain=numpy.zeros((12674,1483))
print("interactionMetirx.shape[0]",interactionMetirx.shape[0])
for i in range(interactionMetirx.shape[0]):
    for j in range (interactionMetirx.shape[1]):
        if(interactionMetirx[i][j]==1):
            positivetrain[positivenum]=numpy.append(drugVector[i],targetVector[j])
            positivenum=positivenum+1
print(positivenum)
print(positivetrain.shape)
positivey=numpy.ones(12674)
negetivetain=numpy.zeros((12674,1483))
for i in range(12674):
    x=random.randint(0,5876)
    y=random.randint(0, 3347)
    if(interactionMetirx[x][y]!=1):
        negetivetain[i] = numpy.append(drugVector[x], targetVector[y])
    elif (interactionMetirx[x][y]==1):
        i=i-1
negetivey=numpy.zeros(12674)
print(negetivetain.shape)
dataset=numpy.vstack((positivetrain, negetivetain))
print(dataset.shape)
datasety=numpy.append(positivey, negetivey)
print(len(datasety))
print(datasety.shape)
numpy.save('dataset', dataset)
numpy.save("datasety",datasety)
'''
unsupervisedNum=0
unsuperviseddata=numpy.zeros((19676196,1483))
for i in range(interactionMetirx.shape[0]):
    for j in range (interactionMetirx.shape[1]):
        unsuperviseddata[unsupervisedNum] = numpy.append(drugVector[i], targetVector[j])
        unsupervisedNum=unsupervisedNum+1
print(unsuperviseddata.shape)
numpy.save("unsuperviseddata",unsuperviseddata)
'''