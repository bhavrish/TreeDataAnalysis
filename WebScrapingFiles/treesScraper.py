import csv

def howManyTrees(zipCode):
	with open('2015StreetTreesCensus_TREES.csv',mode='r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')

		trees=0

		for row in readCSV:
			try:
				zipCodeToMatch=int(row[26])
				if (zip_code == zipCodeToMatch):
					trees+=1
			except ValueError:
				pass

		return trees	



with open('newzipcode.csv',mode='r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    with open('finaldata.csv', mode='w') as csv_file:
    	fieldnames = ['latitude', 'longitude', 'zip_code', 'total_volume', 'trees']
    	writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')

    	writer.writeheader()

    	for row in readCSV:
    		latitude = float(row[0])
    		longitude = float(row[1])
    		zip_code = int(row[2])
    		total_volume = int(row[3])
    		trees=howManyTrees(zip_code)

    		writer.writerow({'latitude': latitude, 'longitude': longitude, 'zip_code': zip_code, 'total_volume': total_volume, 'trees': trees})
    		#print(latitude, longitude, zip_code, total_volume, trees)
