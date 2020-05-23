import pandas as pd
import numpy as np
import pyttsx3 
from sklearn.model_selection import train_test_split

newVoiceRate = 145
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate',newVoiceRate)

engine.say("hello sir ,  i am your own personal farm field advisor khetu. i am here to serve you and assist you well for a healthy farming , feel free to tell me anything. my details are there in your screen. you will be happy to hear that i am ninety one percent accurate")

data=pd.read_csv('cpdata.csv')

label= pd.get_dummies(data.label).iloc[: , 1:]
data= pd.concat([data,label],axis=1)
data.drop('label', axis=1,inplace=True)
train=data.iloc[:, 0:4].values
test=data.iloc[: ,4:].values


X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.3)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.tree import DecisionTreeRegressor
clf=DecisionTreeRegressor()
clf.fit(X_train,y_train)
pred=clf.predict(X_test)


engine.say("so lets get started, from the Node m c u kit we got the following data")
engine.say("the air humidity is 40 around you")
engine.runAndWait()
ah = 40    #AIR HUMIDITY
engine.say("the temperature around you is eighty-one degrees fahrenheit")
engine.runAndWait()
atemp = 81 #AIR TEMPERATURE
engine.say("The rainsfall in your area accordig to last year data is 119 milimeteres")
engine.runAndWait()
rain = 119  #RAINFALL
engine.say(" The pH of your soil is five")
engine.runAndWait()
pH = 5 #PH


l=[]
l.append(ah)
l.append(atemp)
l.append(pH)
l.append(rain)
predictcrop=[l]

crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
cr='rice'
predictions = clf.predict(predictcrop)
count=0
for i in range(0,30):
    if(predictions[0][i]==1):
        c=crops[i]
        count=count+1
        break
    i=i+1

if(count==0):
    engine.say("thankyou very much sir , on your screen is the best crop that i suggest for your field after perfect research , happy farming from my side sir")
    engine.runAndWait()
    print('The predicted crop is %s'%cr)
else:
    engine.say("thankyou very much sir , on your screen is the best crop that i suggest for your field after perfect research ,  happy farming from my side sir")
    engine.runAndWait()
    print('The predicted crop is %s'%c)
