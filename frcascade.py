import cv2
import os
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt



def compare_lists(list1,list2):
    correct=0
    total=0
    print(list1)
    print(list2)
    for i in range(len(list1)):
        total+=1
        if list1[i]==list2[i]:
            correct+=1
    return correct/total


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loading custom classifier to recognize
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier_results2.xml")

imagePaths= [os.path.join("test_cropped", f) for f in os.listdir("test_cropped")]

y_test=[]
ids = []

for image in imagePaths:
    #real_id=image.split('_')[0]
    
    real_id=int(os.path.split(image)[1][0])
    
    y_test.append(real_id)
    img=cv2.imread(image,0)
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    
    
    features = faceCascade.detectMultiScale(img, 1.1, 5)
    if len(features)!=0:
        for (x, y, w, h) in features:
            #cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            
            # Predicting the id of the user
            id, con = clf.predict(img[y:y+h, x:x+w])
            # Check for id of user and label the rectangle accordingly
            ids.append(id)
            break
    else:
        ids.append(0)
accuracy = compare_lists(y_test,ids)
print(confusion_matrix(y_test, ids,labels = [0,1,2,3,4,5]))
print(accuracy)
print(classification_report(y_test, ids))
