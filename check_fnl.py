# -*- coding: cp936 -*-
## python script to download selected files from rda.ucar.edu
##
import sys
import os
import datetime
import subprocess



#��ʼ����
begin = datetime.date(2008,1,1)  
end = datetime.date(2018,12,31)
d=begin
delta = datetime.timedelta(days=1)
   
#����������������
links = []
while d <= end:
    riqi=d.strftime("%Y%m%d")
    yue=d.strftime("%m")
    nian=d.strftime("%Y")
    filename="grib2/"+nian+"/"+nian+"."+yue+"/fnl_"+riqi+"_00_00.grib2"
    links.append(filename)
    filename="grib2/"+nian+"/"+nian+"."+yue+"/fnl_"+riqi+"_06_00.grib2"
    links.append(filename)
    filename="grib2/"+nian+"/"+nian+"."+yue+"/fnl_"+riqi+"_12_00.grib2"
    links.append(filename)
    filename="grib2/"+nian+"/"+nian+"."+yue+"/fnl_"+riqi+"_18_00.grib2"
    links.append(filename)
    d += delta

  
## download the data file(s)
listoffiles=links

for file in listoffiles:
    fileb=str(file)
    filec=fileb[-24:]
    #�ж��Ƿ���ȷ
    cmd="grib_index_build -k dataDate,dataTime,level,shortName -N /mnt/z/FNL/grib2/"+str(filec)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
   

    


##    #����������ļ����򷵻�
##    if(not os.path.isfile(filec)):
##        print("no",filec)
##        continue
##
##    

   
