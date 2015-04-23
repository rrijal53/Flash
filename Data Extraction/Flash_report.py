import lxml
import urllib2
import re
from lxml import html
f = open('Flash_Final.txt','w+')
f.write("School_code#School_name#development_region#Eco_Belt#Zone#District#VDC#Address#Ward_No#Locality#ECD#PRIMARY#LSEC#SEC#HSEC\n")
def general_information(tbl):
    try:
        School_code=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[1]/tr/td[2]/h2/text()')
    except:
        School_code=""
    try:
        School_name=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[1]/tr/td[2]/h2/text()')
    except:
        School_name=""
    try:
        development_region=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[2]/td/text()')[2].split()[-1]
    except:
        development_region=""
    try:
        Eco_Belt=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[3]/td/text()')[2].split()[-1]
    except:
        Eco_Belt=""
    try:
        Zone=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[4]/td/text()')[2].split()[-1]
    except:
        Zone=""
    try:
        District=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[5]/td/text()')[2].split()[-1]
    except:
        District=""
    try:
        VDC=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[6]/td/text()')[2].split()[-1]
    except:
        VDC=""
    try:
        Address=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[7]/td/text()')[2].split()[-1]
    except:
        Address=""
    try:
        Ward_No=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[8]/td/text()')[2].split()[-1]
    except:
        Ward_No=""
    try:
        Locality=subroot.xpath('/html/body/table['+tbl.__str__()+']/tr/td/table[2]/tr/td[1]/table/tr[10]/td/text()')[2].split()[-1]
    except:
        Locality=""
    return School_code[1][7:]+"#"+School_name[0][8:]+"#"+development_region+"#"+Eco_Belt+"#"+Zone+"#"+District+"#"+VDC+"#"+Address+"#"+Ward_No+"#"+Locality
def school_type(tbl,col):
    try:
        Community_aided=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[3]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Community_aided=''
    try:
        Community_Managed=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[4]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Community_Managed=''
    try:
        Community_Teacher_aided=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[5]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Community_Teacher_aided=''
    try:
        Community_Unaided=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[6]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Community_Unaided=''
    try:
        Institutional_Private_Trust=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[7]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Institutional_Private_Trust=''
    try:
        Institutional_Public_Trust=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[8]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Institutional_Public_Trust=''
    try:
        Institutional_Enlisted_With_Company=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[9]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Institutional_Enlisted_With_Company=''
    try:
        Madrassa=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[10]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Madrassa=''
    try:
        Gumba=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[11]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Gumba=''
    try:
        Ashram=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[12]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Ashram=''
    try:
        Community_ECD=subroot.xpath("/html/body/table["+tbl.__str__()+"]/tr/td/table[2]/tr/td[3]/table/tr[13]/td["+col.__str__()+"]/img['src']")[-1]
    except:
        Community_ECD=''
    if Community_aided!='':
        Community_aided="Community_aided"
    if Community_Managed!='':
        Community_Managed="Community_Managed"
    if Community_Teacher_aided!='':
        Community_Teacher_aided="Community_Teacher_aided"
    if Community_Unaided!='':
        Community_Unaided="Community_Unaided"
    if Institutional_Private_Trust!='':
        Institutional_Private_Trust="Institutional_Private_Trust"
    if Institutional_Public_Trust!='':
        Institutional_Public_Trust="Institutional_Public_Trust" 
    if Institutional_Enlisted_With_Company!='':
        Institutional_Enlisted_With_Company="Institutional_Enlisted_With_Company"
    if Madrassa!='':
        Madrassa="Madrassa"
    if Gumba!='':
        Gumba="Gumba"
    if Ashram!='':
        Ashram="Ashram"
    if Community_ECD!='':
        Community_ECD="Community_ECD"
    return Community_aided+Community_Managed+Community_Teacher_aided+Community_Unaided+Institutional_Private_Trust+Institutional_Public_Trust+Institutional_Enlisted_With_Company+Madrassa+Gumba+Ashram+Community_ECD  
file_num=1
for file_num in range(1,75):
    school_report = urllib2.urlopen("http://0.0.0.0:8000/"+file_num.__str__()+".html").read()
    subroot=html.fromstring(school_report)
    try:
        tbl=1
        while tbl:
            ECD=school_type(tbl,2)
            PRIMARY=school_type(tbl,3)
            LSEC=school_type(tbl,4)
            SEC=school_type(tbl,5)
            HSEC=school_type(tbl,6)
            print general_information(tbl)+"#"+ECD+"#"+PRIMARY+"#"+LSEC+"#"+SEC+"#"+HSEC
            f.write(general_information(tbl)+"#"+ECD+"#"+PRIMARY+"#"+LSEC+"#"+SEC+"#"+HSEC+"\n")
            tbl=tbl+1
    except:
        file_num=file_num+1