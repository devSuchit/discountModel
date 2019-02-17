import pandas as pd
import csv
import re

file=pd.read_csv("test.csv")

reffile=pd.read_csv("Product_sales_train_and_test.csv")#, encoding = "ISO-8859-1"
    
def test_reader():

    with open("test_preprocessed.csv", mode='w') as writeFile:
        w = csv.writer(writeFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['BillNo','Month','Year','Customer_Basket'])
        for n in range(file.shape[0]):
            temp_date=file.iloc[n]["Date"]
            temp_date=re.sub("[^0-9]","",temp_date)
            datee=temp_date[:2]
            monthh=temp_date[2:4]
            yearr=temp_date[-4:]
            
            billno=file.iloc[n]["BillNo"]
            basket_row=reffile.loc[reffile["BillNo"] == billno]
            basket=basket_row.iloc[0]["Customer_Basket"]
            w.writerow([billno,monthh,yearr,basket])
            
            
            
            

test_reader()