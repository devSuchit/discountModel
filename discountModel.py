import pandas as pd
import csv

data = pd.read_csv('training_input.csv')
data1 = pd.read_csv('test_input.csv')
data2 = pd.read_csv('training_output.csv')
y_train=data2.copy()
x_train=data.drop(['Bill No'],axis=1)
x_test=data1.drop(['Bill No'],axis=1)
labels_train=data['Bill No']
labels_test=data1['Bill No']

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(811,811,4),max_iter=500)
model.fit(x_train,y_train)
out = model.predict(x_test)


k=0
with open('submission_file.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['BillNo','Discount 5%','Discount 12%','Discount 18%','Discount 28%'])
        for i in range(1891):
            add_row=[]
            add_row.append('0')
            k=k+1
            for j in range(4):
               add_row.append(out[i][j])
            writer.writerow(add_row)
                
            
