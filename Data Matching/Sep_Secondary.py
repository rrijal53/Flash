import os
import csv
import re
f=open("Flash_data_secondary.txt","w+")
flash_csv="Flash_Report.csv"
flash_header=["School_code","School_name","development_region","Eco_Belt","Zone","District","VDC","Address","Ward_No","Locality","ECD","PRIMARY","LSEC","SEC","HSEC"]
for row in flash_header:
    f.write(row+"#")
f.write("\n")
with open(flash_csv) as csvfile:
  flash_reader = csv.DictReader(csvfile)
  for row in flash_reader:
         flash_name=row['School_name']
         if re.search("Ma V",flash_name) or re.search("Secondary",flash_name) or re.search("Ebs",flash_name):
            if re.search("Ni Ma V",flash_name):
              pass
            else:
              f.write(row['School_code']+"#"+row['School_name']+"#"+row['development_region']+"#"+row['Eco_Belt']+"#"+row['Zone']+"#"+row['District']+"#"+row['VDC']+"#"+row['Address']+"#"+row['Ward_No']+"#"+row['Locality']+"#"+row['ECD']+"#"+row['PRIMARY']+"#"+row['LSEC']+"#"+row['SEC']+"#"+row['HSEC']+"#\n")


#f.write("#"+row1['SLCYear']+"#"+row1['DistrictName']+"#"+row1['DistrictCode']+"#"+row1['SCHCODE']+"#"+row1['School_name']+"#"+row1['AppearedTotal']+"#"+row1['AppearedBoys']+"#"+row1['AppearedGirls']+"#"+row1['PassTotal']+"#"+row1['PassBoys']+"#"+row1['PassGirls']+"#"+row1['Percentage']+"#"+row1['DivisionBoys']+"#"+row1['DivisionGirls']+"#"+row1['FirstDivBoys']+"#"+row1['FirstDivGirls']+"#"+row1['SecondDivBoys']+"#"+row1['SecondDivGirls']+"#"+row1['ThirdDivBoys']+"#"+row1['ThirdDivGirls']+"#"+row1['WithheldBoys']+"#"+row1['WithheldGirls']+"#"+row1['CanceledBoys']+"#"+row1['CanceledGirls']+"#"+row1['ExpelledBoys']+"#"+row1['ExpelledGirls']+"#\n")
#os.system("grep -E '"++"' SLC_Data.csv")
