from uszipcode import SearchEngine, SimpleZipcode, Zipcode
import csv

search = SearchEngine()

with open('zipcode.csv',mode='r',encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    with open('newzipcode.csv', mode='w') as csv_file:
    	fieldnames = ['latitude', 'longitude', 'zip_code']
    	writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')

    	writer.writeheader()

    	for row in readCSV:
	    	latitude = float(row[0])
	    	longitude = float(row[1])
	    	aggregate_total = int(row[2])
	    	result = search.by_coordinates(latitude, longitude, radius=1)
	    	limit=0
	    	for zipcode in result:
	    		if (limit==0):
	    			writer.writerow({'latitude': latitude, 'longitude': longitude, 'zip_code': zipcode.zipcode, 'aggregate_total': aggregate_total})
	    			#print(row[0], row[1], zipcode.zipcode, aggregate_total)
	    			limit+=1
	    		else:
	    			break
	    		#print(row[0], row[1], zipcode.zipcode)
