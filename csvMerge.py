import glob
import csv
import sys

# USER INPUT PATH TO CSV FILES
pathToCSV = raw_input('Input path to CSV files: ')

interesting_files = glob.glob(pathToCSV+"*.csv")
if (pathToCSV+"merged.csv") in interesting_files:
    print '\nError: Must delete merged.csv prior to running\n'
    sys.exit()

# Open result file
with open('merged.csv','a') as fout:
    wout = csv.writer(fout,delimiter=',') 
    h = True
    for filename in interesting_files: 
        print 'Processing',filename 
        # Open and process file
        with open(filename,'rU') as fin: 
            if h:
                h = False
            else:
                fin.next() #skip header
            for line in csv.reader(fin,delimiter=','):
                wout.writerow(line)
                