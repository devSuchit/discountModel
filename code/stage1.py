import csv
month=['January','February','March','April','May','June','July','August','September','October','November','December']
with open('train_1.csv', mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	with open('train.csv','rt')as f:
		data = csv.reader(f)
		for row in data:
			if row[0]=="BillNo":
				add_row=row
				add_row.remove("Date")
				add_row.insert(1,"Month")
				add_row.insert(2,"Year")
			else:
				word=row[1].strip()
				date=word.split(" ")
				for i in range(len( month)):
					if date[0]==month[i]:
						date[0]=i+1
						break
				add_row=[]
				for i in range(len(row)):
					if i==1:
						add_row.extend(date)
					else:
						add_row.append(row[i])
			writer.writerow(add_row)
		
