"""
 LOADBUILDING is used to load HNEI building data.

 SYNTAX:   loadBuilding(filename,excelOffset,tzConvert,bFirstMinute,bInterval)

 INPUTS:   filename:       path to data file
           excelOffset:    time conversion between MATLAB and Excel
           tzConvert:      time zone conversion
           bFirstMinute:   number of minutes after each hour that the first data point is recorded
           bInterval:      data interval in minutes
"""
import glob
import csv
import sys
import time

def loadBuilding(filename,excelOffset,tzConvert,wxFirstMinute,wxInterval):
	wx = csv.reader(open(filename,"rU"))
	getHeaders(filename)


def getHeaders(filename):
	filetoread = csv.reader(open(filename,"rU"))
	headers = filetoread.next()
	print "\n"
	for index,elem in enumerate(headers):
		print index, elem
	print "\n"




loadBuilding("/Users/Ben/Documents/MATLAB/data/d36_q6_data.csv",695422,10,5,10)
