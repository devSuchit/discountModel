import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

bill_contents = pd.read_csv('Product_sales_train_and_test.csv')
train = pd.read_csv('Train.csv')
test = pd.read_csv('test.csv')

# Final training set

final_train = pd.read_csv('training_set.csv')
final_train.info()

X = pd.read_csv('training_input.csv')
y = pd.read_csv('training_output.csv')

# Data Visualization
categories = list(y.columns.values)
sns.set(font_scale = 1)
plt.figure(figsize=(5,2))
ax= sns.barplot(categories, y.iloc[:,0:].sum().values)



# Categorical data 
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X['BillNo'] = labelencoder_X.fit_transform(X['BillNo'])
#X['Customer_Basket'] = labelencoder_X.fit_transform(X['Customer_Basket'])


# Splitting the dataset into the Training set and Test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

X_testt = pd.read_csv('test_input.csv')

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
classifier = KNeighborsClassifier(n_neighbors = 11, metric = 'minkowski', p = 2, n_jobs = -1)
classifier.fit(X, y)

y_pred = classifier.predict(X_testt)
print(accuracy_score(y_test,y_pred))

# Confusion Matrix
confusion_matrix(
    y_test.values.argmax(axis=1), y_pred.argmax(axis=1))

print(classification_report(y_test, y_pred))

# Submission file
submission = pd.DataFrame(y_pred)
submission.to_csv("prediction.csv", index=False)

