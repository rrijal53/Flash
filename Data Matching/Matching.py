import os
import re
flash_header=["School_code","School_name","development_region","Eco_Belt","Zone","District","VDC","Address","Ward_No","Locality","ECD","PRIMARY","LSEC","SEC","HSEC"]
slc_header=["SLCYear","DistrictName","DistrictCode","SCHCODE","School_name","AppearedTotal","AppearedBoys","AppearedGirls","PassTotal","PassBoys","PassGirls","%","DivisionBoys","DivisionGirls","FirstDivBoys","FirstDivGirls","SecondDivBoys","SecondDivGirls","ThirdDivBoys","ThirdDivGirls","WithheldBoys","WithheldGirls","CanceledBoys","CanceledGirls","ExpelledBoys","ExpelledGirls"]
flash_csv="Flash_Report.csv"
slc_csv="SLC_Data.csv"
import csv
f=open("test.txt","w+")
f.write("School_code#School_name#development_region#Eco_Belt#Zone#District#VDC#Address#Ward_No#Locality#ECD#PRIMARY#LSEC#SEC#HSEC#SLCYear#DistrictName#DistrictCode#SCHCODE#School_Name#AppearedTotal#AppearedBoys#AppearedGirls#PassTotal#PassBoys#PassGirls#Percentage#DivisionBoys#DivisionGirls#FirstDivBoys#FirstDivGirls#SecondDivBoys#SecondDivGirls#ThirdDivBoys#ThirdDivGirls#WithheldBoys#WithheldGirls#CanceledBoys#CanceledGirls#ExpelledBoys#ExpelledGirls#\n")
with open(flash_csv) as csvfile:
  flash_reader = csv.DictReader(csvfile)
  for row in flash_reader:
      try:
         flash_name=row['School_name']
         flash_district_name=row['District']
         flash_vdc=row['VDC']
         with open(slc_csv) as csvfile:
            slc_reader = csv.DictReader(csvfile)
            for row1 in slc_reader:
                 slc_name=row1['School_name']
                 slc_district_name=row1['DistrictName']
                 try:
                    slc_vdc=slc_name.split("Vi ")[1]
                 except:
                    slc_vdc=None
                 if re.match(flash_name,slc_name):
                    if re.match(flash_district_name,slc_district_name):
                      if re.match(flash_vdc,slc_vdc):
                      	print flash_name+"=="+slc_name
                      	f.write(row['School_code']+"#"+row['School_name']+"#"+row['development_region']+"#"+row['Eco_Belt']+"#"+row['Zone']+"#"+row['District']+"#"+row['VDC']+"#"+row['Address']+"#"+row['Ward_No']+"#"+row['Locality']+"#"+row['ECD']+"#"+row['PRIMARY']+"#"+row['LSEC']+"#"+row['SEC']+"#"+row['HSEC'])
                      	f.write("#"+row1['SLCYear']+"#"+row1['DistrictName']+"#"+row1['DistrictCode']+"#"+row1['SCHCODE']+"#"+row1['School_name']+"#"+row1['AppearedTotal']+"#"+row1['AppearedBoys']+"#"+row1['AppearedGirls']+"#"+row1['PassTotal']+"#"+row1['PassBoys']+"#"+row1['PassGirls']+"#"+row1['Percentage']+"#"+row1['DivisionBoys']+"#"+row1['DivisionGirls']+"#"+row1['FirstDivBoys']+"#"+row1['FirstDivGirls']+"#"+row1['SecondDivBoys']+"#"+row1['SecondDivGirls']+"#"+row1['ThirdDivBoys']+"#"+row1['ThirdDivGirls']+"#"+row1['WithheldBoys']+"#"+row1['WithheldGirls']+"#"+row1['CanceledBoys']+"#"+row1['CanceledGirls']+"#"+row1['ExpelledBoys']+"#"+row1['ExpelledGirls']+"#\n")
      except:
          continue
#os.system("grep -E '"++"' SLC_Data.csv")
