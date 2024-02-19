import pandas as p
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import classification_report as cr
from sklearn.metrics import accuracy_score as acc

fp='../../Downloads/IRIS.csv'
data=p.read_csv(fp)
print(data.describe())

a=data["species"]
b=data.drop("species",axis=1)

btrain,btest,atrain,atest=tts(b,a,test_size=0.2,random_state=69)
l=lr()
l.fit(btrain,atrain)
apred=l.predict(btest)

print(cr(atest,apred))
print(acc(atest,apred))
