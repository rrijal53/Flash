from xlrd import open_workbook
import re
i=0
j=0
slc = open_workbook('SLC_Data.xlsx',on_demand=True)
flash= open_workbook('Flash_Report.xlsx',on_demand=True)
slc_sheet = slc.sheet_by_name("Sheet1")
flash_sheet = flash.sheet_by_name("Sheet1")
for cell in slc_sheet.col(4): 
	i+=1
     	for cellf in flash_sheet.col(1):
     		aa=cellf.value
     		if re.search(aa, cell.value):
     			j+=1
     			if flash_sheet.col(5)[j].value==slc_sheet.col(1)[i].value:
     				address=cell.value.split("Vi ")
     				try:
     					if address[1]== flash_sheet.col(7)[j].value:
     						print cell.value+"="+cellf.value+" "+flash_sheet.col(5)[j].value+" "+address[1]
     				except:
     					pass
     				