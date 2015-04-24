from xlrd import open_workbook
import xlwt
import re
book=xlwt.Workbook()
sh=book.add_sheet("Test")
i=0
j=0
a=0
slc = open_workbook('SLC_Data.xlsx',on_demand=True)
flash= open_workbook('Flash_Report.xlsx',on_demand=True)
slc_sheet = slc.sheet_by_name("Sheet1")
flash_sheet = flash.sheet_by_name("Sheet1")
for cell in slc_sheet.col(4): 
	i+=1
	j=0
     	for cellf in flash_sheet.col(1):
     		aa=cellf.value
     		j+=1
     		try:
	     		if re.match(aa, cell.value):
	     			#print "name match "+cell.value+" = "+aa
	     			district_flash=flash_sheet.col(5)[j].value
	     			district_slc=slc_sheet.col(1)[i].value
	     			if re.match(district_flash,district_slc):
	     				print "District Match"
	     				print cell.value+"  "+district_flash+"="+cellf.value+","+district_slc
	     				try:
	     					Address_slc=cell.value.split("Vi ")[1]
	     				except:
	     					print "Address chhaina"
	     				Address_flash=flash_sheet.col(6)[j].value
	     				if re.match(Address_flash,Address_slc):
	     					print "Address match"
	     					print cell.value+"="+cellf.value+" "+flash_sheet.col(5)[j].value+" "+Address_flash[1]
	     					sh.write(a,b,cell.value)
	     					sh.write(a+1,b,cellf.value)
	     					a+=1
	     			'''if flash_sheet.col(5)[j].value==slc_sheet.col(1)[i].value:
	     				print "district match"
	     				address=cell.value.split("Vi ")
	     				if address[1]== flash_sheet.col(7)[j].value:
	     					print "Address match"
	     					print cell.value+"="+cellf.value+" "+flash_sheet.col(5)[j].value+" "+address[1]'''
	     	except:
	     		print "something went wrong"				

book.save("Test.xls")