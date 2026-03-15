#CSV Files - comma separated values
#separated by delimitters - ,/-/etc.

import csv        #'csv' module especially designed to work with csv files

"""
#To Read a 'csv' file in Python
____________________________________________________________________________
with open('NamesInfo.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader)                  #to skip the field name and directly print out the values

    for line in csv_reader:
        print(line)

#To create a new csv file and writing in the contents of the old file - and changing the delimiter
_______________________________________________________________________________________________________________
with open('NamesInfo.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader)                  #to skip the field name and directly print out the values

    with open('NewNamesInfo.csv', 'w') as newCsv_file:
        csv_writer = csv.writer(newCsv_file, delimiter= '\t')    #the delimiter is changed from ',' to '\t'    
        
        for line in csv_reader:
            csv_writer.writerow(line)

#To get a dictionary - key:value pair from the csv file
with open('NamesInfo.csv', 'r') as csv_file:
    csv_dictReader = csv.DictReader(csv_file)

    for line in csv_dictReader:
        print(line)

#To write csv file as a dictionary 
with open('NamesInfo.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('NewNamesInfo.csv', 'w', newline='') as csvNew_file:     #the 'newline' method doesn't add a new line after each row
        fieldNames = ['FirstName', 'LastName', 'EmailId', 'Course']   #specifying field names
        csv_dictWriter = csv.DictWriter(csvNew_file, fieldnames= fieldNames, delimiter='\t')

        csv_dictWriter.writeheader()

        for line in csv_reader:
            csv_dictWriter.writerow(line)    #only field values will be printed out

 Fun Fact, when they're not comma separated, it uses dsv instead of csv. D for delimiter. In this sense, all csv files are also dsv files

"""
            

