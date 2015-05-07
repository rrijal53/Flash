import os
import re
flash_csv="Flash_Report.csv"
slc_csv="SLC_Data.csv"
import csv
f=open("text.txt","w+")
f.write("School_code#School_name#development_region#Eco_Belt#Zone#District#VDC#Address#Ward_No#Locality#ECD#PRIMARY#LSEC#SEC#HSEC#SLCYear#DistrictName#DistrictCode#SCHCODE#School_Name#AppearedTotal#AppearedBoys#AppearedGirls#PassTotal#PassBoys#PassGirls#Percentage#DivisionBoys#DivisionGirls#FirstDivBoys#FirstDivGirls#SecondDivBoys#SecondDivGirls#ThirdDivBoys#ThirdDivGirls#WithheldBoys#WithheldGirls#CanceledBoys#CanceledGirls#ExpelledBoys#ExpelledGirls#\n")
with open(flash_csv) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      try:
         flash_name=row['School_name']
         flash_district_name=row['District']
         flash_vdc=row['VDC']
         with open(slc_csv) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                 slc_name=row['School_name']
                 slc_district_name=row['DistrictName']
                 try:
                    slc_vdc=slc_name.split("Vi ")[1]
                 except:
                    slc_vdc=None
                 if re.match(flash_name,slc_name):
                    if re.match(flash_district_name,slc_district_name):
                      if re.match(flash_vdc,slc_vdc):
                        print flash_name+"="+slc_name
      except:
          continue
#os.system("grep -E '"++"' SLC_Data.csv")
