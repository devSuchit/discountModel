import csv
headings=[]
with open('training_input.csv', mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	counter=0
	with open('product_details.csv','rt')as g:
		data1 = csv.reader(g)
		for row in data1:
			if counter==0:
				headings.append('Bill No')
				counter=1
			else:
				headings.append(int(row[0]))
	headings.append("Month")
	headings.append("Year")
	counter=0
	with open('training_set.csv','rt')as f:
		data = csv.reader(f)
		for row in data:
			if counter==0:
				writer.writerow(headings)
				counter=1
			else:
			
				add_row=[]
				temp=row[3].replace("[","").replace("]","").split(" ")
				add_row.append(row[0])
				for i in range(len(headings)-1):
					add_row.append(0)
				for i in temp:
					i = int(i)
					index=headings.index(i)
					add_row[index]=1
				add_row.append(row[1])
				add_row.append(row[2])
				writer.writerow(add_row)
