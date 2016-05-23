import cv2
import cv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import svm
from sklearn import datasets


img = cv2.imread('COTTON/C35.jpg',0)

'''edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
'''
s=img.shape
#print s
p=s[0]/2
o=s[1]/2
if p>o:
   y=x=range(0,o-1,o/20)
   a=b=range(o,2*o,o/20)
else:
   y=x=range(0,p,p/20)
   a=b=range(p+1,2*p,p/20)
#print x
#print a
if len(a)>len(x):
    b=a=a[:-(len(a)-len(x))]
'''else:
    x=y=x[:-(len(x)-len(a))]'''
t=img[x,y]
e=img[a,b]
#print t
#print e
#print x
#print a
'''a=range(p+1,o,16) 
b=range(p+1,o,16)
a=range(o,p,16) 
b=range(o,p,16)'''
#e=img1[a,b]
#print e
#plt.hist(img)
#clf= svm.SVC(gamma=0.01 , C=100)
#clf.fit(t,e)

kmeans = KMeans(n_clusters=1)
if len(a)> len(x) :
   for i in range(len(x)):
    X= ([t[i] , e[i]])
else :
   for i in range(len(a)):
      X= ([t[i] , e[i]])

kmeans.fit(X)
centroid = kmeans.cluster_centers_
labels = kmeans.labels_
#print centroid
x1=centroid[0][0]
y1=centroid[0][1]

clf= svm.SVC(gamma=0.0001 , C=100)
data = [
[121,83],[83,230],[112,110],[79,31],[110,85],[57,64],[127,121],[45,99],[33,59],[29,65],[79,31],[108,79],[108,107],[54,45],[41,120],[62,94],[57,25],[97,51],[59,38],[58,54],[136,114],[60,84],[66,54],[148,52],[96,136],[97,125],[65,70],[106,85],[124,123],[37,66],[55,88],[78,129],[157,70],[49,60],[90,88],[56,32],[80,94],[60,81],[36,103],[70,99],[80,80],
[168,152],[167,115],[196,164],[151,145],[181,135],[175,182],[151,145],[181,135],[193,94],[150,162],[184,38],[202,59],[164,178],[113,167],[72,178],[201,140],[61,161],[73,216],[152,80],[203,186],[165,175],[182,125],[159,116],[160,240],[157,180],[199,140],[212,124],[128,154],[196,154],[207,175],[157,157],[185,130],[181,228],[196,186],[110,175],[177,159],[155,120],[216,77],[186,130],[188,167],[185,142]
]

target=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

x,y = data[:], target[:]
clf.fit(x,y)

#img = cv.LoadImageM("cotton4.png",0)
#imgArr = np.asarray(img)
#imgFlat = imgArr.flatten()

arraypred = [x1,y1] 

x = clf.predict(arraypred)
if(x == 0):
    print "COTTON"
elif(x == 1):
    print "SILK"
else:
    print "NA"

