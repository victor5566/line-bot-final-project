import requests
import re
import csv
from bs4 import BeautifulSoup
url = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-005&authorizationkey=CWB-2B5176A3-ADDB-46E5-B563-AAD38B86B0A6' 
response = requests.get(url) # GET 請求 
response.encoding = 'utf-8' # 解決中文問題 
#print(response.text) # HTML 架構
soup = BeautifulSoup(response.text, 'html.parser')  #解析網頁內容
#print(soup)
location = []
for item in soup.select('locationname'):
    location.append(item.text)
title = []
title = soup.select('datasetdescription')[0].text
#print (title)
data = []
data1 =[]
b = []
locationdata1 = []
locationdata2 = []
locationdata3 = []
locationdata4 = []
locationdata5 = []
locationdata6 = []
locationdata7 = []
locationdata8 = []
locationdata9 = []
locationdata10 = []
locationdata11 = []
locationdata12 = []
locationdata13 = []
for item in soup.select('weatherelement'):
    data.append(item.text)
#for y in range(0,len(data)):
   # print (data[y]) 

#print(len(data))
a= len(data[0])
#print(a)
for i in range(0,len(data)):
    b = data[i].split("\n")
    for item in range(0,len(b)):
        if(b[item] != ""):
            data1.append(b[item])
#print(data1)
#print(len(data1))
j=0
k=len(data1)//13
for i in range(j,k):
    locationdata1.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata2.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata3.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata4.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata5.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata6.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata7.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata8.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata9.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata10.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata11.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata12.append(data1[i])
j=k
k=k+len(data1)//13
for i in range(j,k):
    locationdata13.append(data1[i])
#print(locationdata1)
import re
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
locationtemp1 = []
locationRH1 = []
locationPoP12h1 = []
locationCI1 =[]
locationAT1 = []
locationWx1 = []
locationWD1 = []
k=0
for item in locationdata1:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp1.append(item)
    if(k==3):
        locationRH1.append(item)
    if(k==5):
        locationPoP12h1.append(item)
    if(k==8):
        locationCI1.append(item)
    if(k==9):
        locationAT1.append(item)
    if(k==10):
        locationWx1.append(item)
    if(k==11):
        locationWD1.append(item)
#print(locationWD1)  
#print(k)
locationtime1 = []
for item in locationtemp1:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime1.append(a.group())
#print(locationtime1)
#print(len(locationtime1))
pattern1 = '^-?[0-9]{2}$'
temp1 = []
for item in locationtemp1:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp1.append(a.group())
#print(temp1)
RH1= []
pattern2 = '^-?[0-9]{1,3}$'
for item in locationRH1:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH1.append(a.group())
#print(RH1)
PoP12h1 = []
for item in locationPoP12h1:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h1.append(a.group())
#print(PoP12h1)
PoP12h1time = []
for item in locationPoP12h1:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h1time.append(a.group())
#print(PoP12h1time)
CI1 = []
for item in locationCI1:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI1.append(a.group())
#print(CI1)
CI1index = []
k=5
for item in range(k,len(locationCI1)):
    if(k>len(locationCI1)):
        break
    a= locationCI1[k]
    CI1index.append(a)
    k=k+5
#print(CI1index)
AT1 = []
for item in locationAT1:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT1.append(a.group())
#print(AT1)
Wx1index = []
k=4
for item in range(k,len(locationWx1)):
    if(k>len(locationWx1)):
        break
    a= locationWx1[k]
    Wx1index.append(a)
    k=k+6
#print(Wx1index)
Wx1time = []
for item in locationWx1:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx1time.append(a.group())
#print(Wx1time)
WD1index = []
k=4
for item in locationWD1:
    if(k>len(locationWD1)):
        break
    a= locationWD1[k]
    WD1index.append(a)
    k=k+4
#print(WD1index)
WD1time = []
for item in locationWD1:
    a=re.match(pattern,item , flags = False)
    if a:
        WD1time.append(a.group())
#print(WD1time)
# -*- conding: utf-8 -*-
import codecs
weather = dict()
weather1 = dict()
with open ('蘆竹區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '蘆竹區'
    weather1['地區'] = '蘆竹區'
    for time in range(len(locationtime1)):
        if(time<6):
            weather['時間'] = locationtime1[time]
            weather['溫度(攝氏度)'] = temp1[time]
            weather['相對溼度'] = RH1[time]
            weather['降雨機率時間'] = PoP12h1time[time]
            weather['降雨機率'] = PoP12h1[time]
            weather['舒適度指數'] = CI1[time]
            weather['舒適度指標'] = CI1index[time]
            weather['體感溫度(攝氏度)'] = AT1[time]
            weather['天氣現象'] = Wx1index[time]
            weather['天氣預報綜合描述'] = WD1index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime1[time]
            weather1['溫度(攝氏度)'] = temp1[time]
            weather1['相對溼度'] = RH1[time]
            weather1['舒適度指數'] = CI1[time]
            weather1['舒適度指標'] = CI1index[time]
            weather1['體感溫度(攝氏度)'] = AT1[time]
            weather1['天氣現象'] = Wx1index[time]
            weather1['天氣預報綜合描述'] = WD1index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('蘆竹區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames1 = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames1)
    writer.writeheader()
    weather['地區'] = '蘆竹區'
    weather1['地區'] = '蘆竹區'
    for time in range(len(locationtime1)):
        if(time<6):
            weather['時間'] = locationtime1[time]
            weather['溫度(攝氏度)'] = temp1[time]
            weather['體感溫度(攝氏度)'] = AT1[time]
            weather['天氣預報綜合描述'] = WD1index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime1[time]
            weather1['溫度(攝氏度)'] = temp1[time]
            weather1['體感溫度(攝氏度)'] = AT1[time]
            weather1['天氣預報綜合描述'] = WD1index[time] 
            writer.writerow(weather1)
locationtemp2 = []
locationRH2 = []
locationPoP12h2 = []
locationCI2 =[]
locationAT2 = []
locationWx2 = []
locationWD2 = []
k=0
for item in locationdata2:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp2.append(item)
    if(k==3):
        locationRH2.append(item)
    if(k==5):
        locationPoP12h2.append(item)
    if(k==8):
        locationCI2.append(item)
    if(k==9):
        locationAT2.append(item)
    if(k==10):
        locationWx2.append(item)
    if(k==11):
        locationWD2.append(item)
#print(locationPoP12h2) 
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime2 = []
for item in locationtemp2:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime2.append(a.group())
#print (locationtime2)
temp2 = []
for item in locationtemp2:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp2.append(a.group())
#print(temp2)
RH2= []
for item in locationRH2:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH2.append(a.group())
#print(RH2)
PoP12h2 = []
for item in locationPoP12h2:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h2.append(a.group())
#print(PoP12h2)
PoP12h2time = []
for item in locationPoP12h2:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h2time.append(a.group())
#print(PoP12h2time)
CI2 = []
for item in locationCI2:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI2.append(a.group())
#print(CI2)
CI2index = []
k=5
for item in range(k,len(locationCI2)):
    if(k>len(locationCI2)):
        break
    a= locationCI2[k]
    CI2index.append(a)
    k=k+5
#print(CI2index)
AT2 = []
for item in locationAT2:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT2.append(a.group())
#print(AT2)
Wx2index = []
k=4
for item in range(k,len(locationWx2)):
    if(k>len(locationWx2)):
        break
    a= locationWx2[k]
    Wx2index.append(a)
    k=k+6
#print(Wx2index)
Wx2time = []
for item in locationWx2:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx2time.append(a.group())
#print(Wx2time)
WD2index = []
k=4
for item in locationWD2:
    if(k>len(locationWD2)):
        break
    a= locationWD2[k]
    WD2index.append(a)
    k=k+4
#print(WD2index)
WD2time = []
for item in locationWD2:
    a=re.match(pattern,item , flags = False)
    if a:
        WD2time.append(a.group())
#print(WD2time)

import codecs
weather = dict()
weather1 = dict()
with open ('大溪區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '大溪區'
    weather1['地區'] = '大溪區'
    for time in range(len(locationtime2)):
        if(time<6):
            weather['時間'] = locationtime2[time]
            weather['溫度(攝氏度)'] = temp2[time]
            weather['相對溼度'] = RH2[time]
            weather['降雨機率時間'] = PoP12h2time[time]
            weather['降雨機率'] = PoP12h2[time]
            weather['舒適度指數'] = CI2[time]
            weather['舒適度指標'] = CI2index[time]
            weather['體感溫度(攝氏度)'] = AT2[time]
            weather['天氣現象'] = Wx2index[time]
            weather['天氣預報綜合描述'] = WD2index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime2[time]
            weather1['溫度(攝氏度)'] = temp2[time]
            weather1['相對溼度'] = RH2[time]
            weather1['舒適度指數'] = CI2[time]
            weather1['舒適度指標'] = CI2index[time]
            weather1['體感溫度(攝氏度)'] = AT2[time]
            weather1['天氣現象'] = Wx2index[time]
            weather1['天氣預報綜合描述'] = WD2index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('大溪區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames1 = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames1)
    writer.writeheader()
    weather['地區'] = '大溪區'
    weather1['地區'] = '大溪區'
    for time in range(len(locationtime2)):
        if(time<6):
            weather['時間'] = locationtime2[time]
            weather['溫度(攝氏度)'] = temp2[time]
            weather['體感溫度(攝氏度)'] = AT2[time]
            weather['天氣預報綜合描述'] = WD2index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime2[time]
            weather1['溫度(攝氏度)'] = temp2[time]
            weather1['體感溫度(攝氏度)'] = AT2[time]
            weather1['天氣預報綜合描述'] = WD2index[time] 
            writer.writerow(weather1)

locationtemp3 = []
locationRH3 = []
locationPoP12h3 = []
locationCI3 =[]
locationAT3 = []
locationWx3 = []
locationWD3 = []
k=0
for item in locationdata3:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp3.append(item)
    if(k==3):
        locationRH3.append(item)
    if(k==5):
        locationPoP12h3.append(item)
    if(k==8):
        locationCI3.append(item)
    if(k==9):
        locationAT3.append(item)
    if(k==10):
        locationWx3.append(item)
    if(k==11):
        locationWD3.append(item)
#print(locationRH3) 
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime3 = []
for item in locationtemp3:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime3.append(a.group())
#print (locationtime3)
temp3 = []
for item in locationtemp3:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp3.append(a.group())
#print(temp3)
RH3= []
for item in locationRH3:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH3.append(a.group())
#print(RH3)
PoP12h3 = []
for item in locationPoP12h3:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h3.append(a.group())
#print(PoP12h3)
PoP12h3time = []
for item in locationPoP12h3:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h3time.append(a.group())
#print(PoP12h3time)
CI3 = []
for item in locationCI3:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI3.append(a.group())
#print(CI3)
CI3index = []
k=5
for item in range(k,len(locationCI3)):
    if(k>len(locationCI3)):
        break
    a= locationCI3[k]
    CI3index.append(a)
    k=k+5
#print(CI3index)
AT3 = []
for item in locationAT3:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT3.append(a.group())
#print(AT3)
Wx3index = []
k=4
for item in range(k,len(locationWx3)):
    if(k>len(locationWx3)):
        break
    a= locationWx3[k]
    Wx3index.append(a)
    k=k+6
#print(Wx3index)
Wx3time = []
for item in locationWx3:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx3time.append(a.group())
#print(Wx3time)
WD3index = []
k=4
for item in locationWD3:
    if(k>len(locationWD3)):
        break
    a= locationWD3[k]
    WD3index.append(a)
    k=k+4
#print(WD3index)
WD3time = []
for item in locationWD3:
    a=re.match(pattern,item , flags = False)
    if a:
        WD3time.append(a.group())
#print(WD3time)

import codecs
weather = dict()
weather1 = dict()
with open ('復興區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '復興區'
    weather1['地區'] = '復興區'
    for time in range(len(locationtime3)):
        if(time<6):
            weather['時間'] = locationtime3[time]
            weather['溫度(攝氏度)'] = temp3[time]
            weather['相對溼度'] = RH3[time]
            weather['降雨機率時間'] = PoP12h3time[time]
            weather['降雨機率'] = PoP12h3[time]
            weather['舒適度指數'] = CI3[time]
            weather['舒適度指標'] = CI3index[time]
            weather['體感溫度(攝氏度)'] = AT3[time]
            weather['天氣現象'] = Wx3index[time]
            weather['天氣預報綜合描述'] = WD3index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime3[time]
            weather1['溫度(攝氏度)'] = temp3[time]
            weather1['相對溼度'] = RH3[time]
            weather1['舒適度指數'] = CI3[time]
            weather1['舒適度指標'] = CI3index[time]
            weather1['體感溫度(攝氏度)'] = AT3[time]
            weather1['天氣現象'] = Wx3index[time]
            weather1['天氣預報綜合描述'] = WD3index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('復興區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '復興區'
    weather1['地區'] = '復興區'
    for time in range(len(locationtime3)):
        if(time<6):
            weather['時間'] = locationtime3[time]
            weather['溫度(攝氏度)'] = temp3[time]
            weather['體感溫度(攝氏度)'] = AT3[time]
            weather['天氣預報綜合描述'] = WD3index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime3[time]
            weather1['溫度(攝氏度)'] = temp3[time]
            weather1['體感溫度(攝氏度)'] = AT3[time]
            weather1['天氣預報綜合描述'] = WD3index[time] 
            writer.writerow(weather1)
locationtemp4 = []
locationRH4 = []
locationPoP12h4 = []
locationCI4 =[]
locationAT4 = []
locationWx4 = []
locationWD4 = []
k=0
for item in locationdata4:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp4.append(item)
    if(k==3):
        locationRH4.append(item)
    if(k==5):
        locationPoP12h4.append(item)
    if(k==8):
        locationCI4.append(item)
    if(k==9):
        locationAT4.append(item)
    if(k==10):
        locationWx4.append(item)
    if(k==11):
        locationWD4.append(item)
#print(locationCI4)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime4 = []
for item in locationtemp4:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime4.append(a.group())
#print (locationtime4)
temp4 = []
for item in locationtemp4:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp4.append(a.group())
#print(temp4)
RH4= []
for item in locationRH4:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH4.append(a.group())
#print(RH4)
PoP12h4 = []
for item in locationPoP12h4:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h4.append(a.group())
#print(PoP12h4)
PoP12h4time = []
for item in locationPoP12h4:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h4time.append(a.group())
#print(PoP12h4time)
CI4 = []
for item in locationCI4:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI4.append(a.group())
#print(CI4)
CI4index = []
k=5
for item in range(k,len(locationCI4)):
    if(k>len(locationCI4)):
        break
    a= locationCI4[k]
    CI4index.append(a)
    k=k+5
#print(CI4index)
AT4 = []
for item in locationAT4:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT4.append(a.group())
#print(AT4)
Wx4index = []
k=4
for item in range(k,len(locationWx4)):
    if(k>len(locationWx4)):
        break
    a= locationWx4[k]
    Wx4index.append(a)
    k=k+6
#print(Wx4index)
Wx4time = []
for item in locationWx4:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx4time.append(a.group())
#print(Wx4time)
WD4index = []
k=4
for item in locationWD4:
    if(k>len(locationWD4)):
        break
    a= locationWD4[k]
    WD4index.append(a)
    k=k+4
#print(WD4index)
WD4time = []
for item in locationWD4:
    a=re.match(pattern,item , flags = False)
    if a:
        WD4time.append(a.group())
#print(WD4time)

import codecs
weather = dict()
weather1 = dict()
with open ('桃園區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '桃園區'
    weather1['地區'] = '桃園區'
    for time in range(len(locationtime4)):
        if(time<6):
            weather['時間'] = locationtime4[time]
            weather['溫度(攝氏度)'] = temp4[time]
            weather['相對溼度'] = RH4[time]
            weather['降雨機率時間'] = PoP12h4time[time]
            weather['降雨機率'] = PoP12h4[time]
            weather['舒適度指數'] = CI4[time]
            weather['舒適度指標'] = CI4index[time]
            weather['體感溫度(攝氏度)'] = AT4[time]
            weather['天氣現象'] = Wx4index[time]
            weather['天氣預報綜合描述'] = WD4index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime4[time]
            weather1['溫度(攝氏度)'] = temp4[time]
            weather1['相對溼度'] = RH4[time]
            weather1['舒適度指數'] = CI4[time]
            weather1['舒適度指標'] = CI4index[time]
            weather1['體感溫度(攝氏度)'] = AT4[time]
            weather1['天氣現象'] = Wx4index[time]
            weather1['天氣預報綜合描述'] = WD4index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('桃園區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '桃園區'
    weather1['地區'] = '桃園區'
    for time in range(len(locationtime4)):
        if(time<6):
            weather['時間'] = locationtime4[time]
            weather['溫度(攝氏度)'] = temp4[time]
            weather['體感溫度(攝氏度)'] = AT4[time]
            weather['天氣預報綜合描述'] = WD4index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime4[time]
            weather1['溫度(攝氏度)'] = temp4[time]
            weather1['體感溫度(攝氏度)'] = AT4[time]
            weather1['天氣預報綜合描述'] = WD4index[time] 
            writer.writerow(weather1)           
locationtemp5 = []
locationRH5 = []
locationPoP12h5 = []
locationCI5 =[]
locationAT5 = []
locationWx5 = []
locationWD5 = []
k=0
for item in locationdata5:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp5.append(item)
    if(k==3):
        locationRH5.append(item)
    if(k==5):
        locationPoP12h5.append(item)
    if(k==8):
        locationCI5.append(item)
    if(k==9):
        locationAT5.append(item)
    if(k==10):
        locationWx5.append(item)
    if(k==11):
        locationWD5.append(item)
#print(locationAT5)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime5 = []
for item in locationtemp5:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime5.append(a.group())
#print (locationtime5)
temp5 = []
for item in locationtemp5:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp5.append(a.group())
#print(temp5)
RH5= []
for item in locationRH5:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH5.append(a.group())
#print(RH5)
PoP12h5 = []
for item in locationPoP12h5:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h5.append(a.group())
#print(PoP12h5)
PoP12h5time = []
for item in locationPoP12h5:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h5time.append(a.group())
#print(PoP12h5time)
CI5 = []
for item in locationCI5:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI5.append(a.group())
#print(CI5)
CI5index = []
k=5
for item in range(k,len(locationCI5)):
    if(k>len(locationCI5)):
        break
    a= locationCI5[k]
    CI5index.append(a)
    k=k+5
#print(CI5index)
AT5 = []
for item in locationAT5:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT5.append(a.group())
#print(AT5)
Wx5index = []
k=4
for item in range(k,len(locationWx5)):
    if(k>len(locationWx5)):
        break
    a= locationWx5[k]
    Wx5index.append(a)
    k=k+6
#print(Wx5index)
Wx5time = []
for item in locationWx5:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx5time.append(a.group())
#print(Wx5time)
WD5index = []
k=4
for item in locationWD5:
    if(k>len(locationWD5)):
        break
    a= locationWD5[k]
    WD5index.append(a)
    k=k+4
#print(WD5index)
WD5time = []
for item in locationWD5:
    a=re.match(pattern,item , flags = False)
    if a:
        WD5time.append(a.group())
#print(WD5time)

import codecs
weather = dict()
weather1 = dict()
with open ('龜山區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '龜山區'
    weather1['地區'] = '龜山區'
    for time in range(len(locationtime5)):
        if(time<6):
            weather['時間'] = locationtime5[time]
            weather['溫度(攝氏度)'] = temp5[time]
            weather['相對溼度'] = RH5[time]
            weather['降雨機率時間'] = PoP12h5time[time]
            weather['降雨機率'] = PoP12h5[time]
            weather['舒適度指數'] = CI5[time]
            weather['舒適度指標'] = CI5index[time]
            weather['體感溫度(攝氏度)'] = AT5[time]
            weather['天氣現象'] = Wx5index[time]
            weather['天氣預報綜合描述'] = WD5index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime5[time]
            weather1['溫度(攝氏度)'] = temp5[time]
            weather1['相對溼度'] = RH5[time]
            weather1['舒適度指數'] = CI5[time]
            weather1['舒適度指標'] = CI5index[time]
            weather1['體感溫度(攝氏度)'] = AT5[time]
            weather1['天氣現象'] = Wx5index[time]
            weather1['天氣預報綜合描述'] = WD5index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('龜山區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '龜山區'
    weather1['地區'] = '龜山區'
    for time in range(len(locationtime5)):
        if(time<6):
            weather['時間'] = locationtime5[time]
            weather['溫度(攝氏度)'] = temp5[time]
            weather['體感溫度(攝氏度)'] = AT5[time]
            weather['天氣預報綜合描述'] = WD5index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime5[time]
            weather1['溫度(攝氏度)'] = temp5[time]
            weather1['體感溫度(攝氏度)'] = AT5[time]
            weather1['天氣預報綜合描述'] = WD5index[time] 
            writer.writerow(weather1)            
locationtemp6 = []
locationRH6 = []
locationPoP12h6 = []
locationCI6 =[]
locationAT6 = []
locationWx6 = []
locationWD6 = []
k=0
for item in locationdata6:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp6.append(item)
    if(k==3):
        locationRH6.append(item)
    if(k==5):
        locationPoP12h6.append(item)
    if(k==8):
        locationCI6.append(item)
    if(k==9):
        locationAT6.append(item)
    if(k==10):
        locationWx6.append(item)
    if(k==11):
        locationWD6.append(item)
#print(locationWx6)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime6 = []
for item in locationtemp6:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime6.append(a.group())
#print (locationtime6)
temp6 = []
for item in locationtemp6:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp6.append(a.group())
#print(temp6)
RH6= []
for item in locationRH6:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH6.append(a.group())
#print(RH6)
PoP12h6 = []
for item in locationPoP12h6:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h6.append(a.group())
#print(PoP12h6)
PoP12h6time = []
for item in locationPoP12h6:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h6time.append(a.group())
#print(PoP12h6time)
CI6 = []
for item in locationCI6:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI6.append(a.group())
#print(CI6)
CI6index = []
k=5
for item in range(k,len(locationCI6)):
    if(k>len(locationCI6)):
        break
    a= locationCI6[k]
    CI6index.append(a)
    k=k+5
#print(CI6index)
AT6 = []
for item in locationAT6:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT6.append(a.group())
#print(AT6)
Wx6index = []
k=4
for item in range(k,len(locationWx6)):
    if(k>len(locationWx6)):
        break
    a= locationWx6[k]
    Wx6index.append(a)
    k=k+6
#print(Wx6index)
Wx6time = []
for item in locationWx6:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx6time.append(a.group())
#print(Wx6time)
WD6index = []
k=4
for item in locationWD6:
    if(k>len(locationWD6)):
        break
    a= locationWD6[k]
    WD6index.append(a)
    k=k+4
#print(WD6index)
WD6time = []
for item in locationWD6:
    a=re.match(pattern,item , flags = False)
    if a:
        WD6time.append(a.group())
#print(WD6time)

import codecs
weather = dict()
weather1 = dict()
with open ('中壢區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '中壢區'
    weather1['地區'] = '中壢區'
    for time in range(len(locationtime6)):
        if(time<6):
            weather['時間'] = locationtime6[time]
            weather['溫度(攝氏度)'] = temp6[time]
            weather['相對溼度'] = RH6[time]
            weather['降雨機率時間'] = PoP12h6time[time]
            weather['降雨機率'] = PoP12h6[time]
            weather['舒適度指數'] = CI6[time]
            weather['舒適度指標'] = CI6index[time]
            weather['體感溫度(攝氏度)'] = AT6[time]
            weather['天氣現象'] = Wx6index[time]
            weather['天氣預報綜合描述'] = WD6index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime6[time]
            weather1['溫度(攝氏度)'] = temp6[time]
            weather1['相對溼度'] = RH6[time]
            weather1['舒適度指數'] = CI6[time]
            weather1['舒適度指標'] = CI6index[time]
            weather1['體感溫度(攝氏度)'] = AT6[time]
            weather1['天氣現象'] = Wx6index[time]
            weather1['天氣預報綜合描述'] = WD6index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('中壢區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '中壢區'
    weather1['地區'] = '中壢區'
    for time in range(len(locationtime6)):
        if(time<6):
            weather['時間'] = locationtime6[time]
            weather['溫度(攝氏度)'] = temp6[time]
            weather['體感溫度(攝氏度)'] = AT6[time]
            weather['天氣預報綜合描述'] = WD6index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime6[time]
            weather1['溫度(攝氏度)'] = temp6[time]
            weather1['體感溫度(攝氏度)'] = AT6[time]
            weather1['天氣預報綜合描述'] = WD6index[time] 
            writer.writerow(weather1)            
locationtemp7 = []
locationRH7 = []
locationPoP12h7 = []
locationCI7 =[]
locationAT7 = []
locationWx7 = []
locationWD7 = []
k=0
for item in locationdata7:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp7.append(item)
    if(k==3):
        locationRH7.append(item)
    if(k==5):
        locationPoP12h7.append(item)
    if(k==8):
        locationCI7.append(item)
    if(k==9):
        locationAT7.append(item)
    if(k==10):
        locationWx7.append(item)
    if(k==11):
        locationWD7.append(item)
#print(locationWD7)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime7 = []
for item in locationtemp7:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime7.append(a.group())
#print (locationtime7)
temp7 = []
for item in locationtemp7:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp7.append(a.group())
#print(temp7)
RH7= []
for item in locationRH7:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH7.append(a.group())
#print(RH7)
PoP12h7 = []
for item in locationPoP12h7:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h7.append(a.group())
#print(PoP12h7)
PoP12h7time = []
for item in locationPoP12h7:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h7time.append(a.group())
#print(PoP12h7time)
CI7 = []
for item in locationCI7:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI7.append(a.group())
#print(CI7)
CI7index = []
k=5
for item in range(k,len(locationCI7)):
    if(k>len(locationCI7)):
        break
    a= locationCI7[k]
    CI7index.append(a)
    k=k+5
#print(CI7index)
AT7 = []
for item in locationAT7:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT7.append(a.group())
#print(AT7)
Wx7index = []
k=4
for item in range(k,len(locationWx7)):
    if(k>len(locationWx7)):
        break
    a= locationWx7[k]
    Wx7index.append(a)
    k=k+6
#print(Wx7index)
Wx7time = []
for item in locationWx7:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx7time.append(a.group())
#print(Wx7time)
WD7index = []
k=4
for item in locationWD7:
    if(k>len(locationWD7)):
        break
    a= locationWD7[k]
    WD7index.append(a)
    k=k+4
#print(WD7index)
WD7time = []
for item in locationWD7:
    a=re.match(pattern,item , flags = False)
    if a:
        WD7time.append(a.group())
#print(WD7time)

import codecs
weather = dict()
weather1 = dict()
with open ('觀音區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '觀音區'
    weather1['地區'] = '觀音區'
    for time in range(len(locationtime7)):
        if(time<6):
            weather['時間'] = locationtime7[time]
            weather['溫度(攝氏度)'] = temp7[time]
            weather['相對溼度'] = RH7[time]
            weather['降雨機率時間'] = PoP12h7time[time]
            weather['降雨機率'] = PoP12h7[time]
            weather['舒適度指數'] = CI7[time]
            weather['舒適度指標'] = CI7index[time]
            weather['體感溫度(攝氏度)'] = AT7[time]
            weather['天氣現象'] = Wx7index[time]
            weather['天氣預報綜合描述'] = WD7index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime7[time]
            weather1['溫度(攝氏度)'] = temp7[time]
            weather1['相對溼度'] = RH7[time]
            weather1['舒適度指數'] = CI7[time]
            weather1['舒適度指標'] = CI7index[time]
            weather1['體感溫度(攝氏度)'] = AT7[time]
            weather1['天氣現象'] = Wx7index[time]
            weather1['天氣預報綜合描述'] = WD7index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('觀音區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '觀音區'
    weather1['地區'] = '觀音區'
    for time in range(len(locationtime7)):
        if(time<6):
            weather['時間'] = locationtime7[time]
            weather['溫度(攝氏度)'] = temp7[time]
            weather['體感溫度(攝氏度)'] = AT7[time]
            weather['天氣預報綜合描述'] = WD7index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime7[time]
            weather1['溫度(攝氏度)'] = temp7[time]
            weather1['體感溫度(攝氏度)'] = AT7[time]
            weather1['天氣預報綜合描述'] = WD7index[time] 
            writer.writerow(weather1)            
locationtemp8 = []
locationRH8 = []
locationPoP12h8 = []
locationCI8 =[]
locationAT8 = []
locationWx8 = []
locationWD8 = []
k=0
for item in locationdata8:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp8.append(item)
    if(k==3):
        locationRH8.append(item)
    if(k==5):
        locationPoP12h8.append(item)
    if(k==8):
        locationCI8.append(item)
    if(k==9):
        locationAT8.append(item)
    if(k==10):
        locationWx8.append(item)
    if(k==11):
        locationWD8.append(item)
#print(locationtemp8)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime8 = []
for item in locationtemp8:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime8.append(a.group())
#print (locationtime8)
temp8 = []
for item in locationtemp8:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp8.append(a.group())
#print(temp8)
RH8= []
for item in locationRH8:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH8.append(a.group())
#print(RH8)
PoP12h8 = []
for item in locationPoP12h8:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h8.append(a.group())
#print(PoP12h8)
PoP12h8time = []
for item in locationPoP12h8:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h8time.append(a.group())
#print(PoP12h8time)
CI8 = []
for item in locationCI8:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI8.append(a.group())
#print(CI8)
CI8index = []
k=5
for item in range(k,len(locationCI8)):
    if(k>len(locationCI8)):
        break
    a= locationCI8[k]
    CI8index.append(a)
    k=k+5
#print(CI8index)
AT8 = []
for item in locationAT8:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT8.append(a.group())
#print(AT8)
Wx8index = []
k=4
for item in range(k,len(locationWx8)):
    if(k>len(locationWx8)):
        break
    a= locationWx8[k]
    Wx8index.append(a)
    k=k+6
#print(Wx8index)
Wx8time = []
for item in locationWx8:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx8time.append(a.group())
#print(Wx8time)
WD8index = []
k=4
for item in locationWD8:
    if(k>len(locationWD8)):
        break
    a= locationWD8[k]
    WD8index.append(a)
    k=k+4
#print(WD8index)
WD8time = []
for item in locationWD8:
    a=re.match(pattern,item , flags = False)
    if a:
        WD8time.append(a.group())
#print(WD8time)

import codecs
weather = dict()
weather1 = dict()
with open ('新屋區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '新屋區'
    weather1['地區'] = '新屋區'
    for time in range(len(locationtime8)):
        if(time<6):
            weather['時間'] = locationtime8[time]
            weather['溫度(攝氏度)'] = temp8[time]
            weather['相對溼度'] = RH8[time]
            weather['降雨機率時間'] = PoP12h8time[time]
            weather['降雨機率'] = PoP12h8[time]
            weather['舒適度指數'] = CI8[time]
            weather['舒適度指標'] = CI8index[time]
            weather['體感溫度(攝氏度)'] = AT8[time]
            weather['天氣現象'] = Wx8index[time]
            weather['天氣預報綜合描述'] = WD8index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime8[time]
            weather1['溫度(攝氏度)'] = temp8[time]
            weather1['相對溼度'] = RH8[time]
            weather1['舒適度指數'] = CI8[time]
            weather1['舒適度指標'] = CI8index[time]
            weather1['體感溫度(攝氏度)'] = AT8[time]
            weather1['天氣現象'] = Wx8index[time]
            weather1['天氣預報綜合描述'] = WD8index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('新屋區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '新屋區'
    weather1['地區'] = '新屋區'
    for time in range(len(locationtime8)):
        if(time<6):
            weather['時間'] = locationtime8[time]
            weather['溫度(攝氏度)'] = temp8[time]
            weather['體感溫度(攝氏度)'] = AT8[time]
            weather['天氣預報綜合描述'] = WD8index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime8[time]
            weather1['溫度(攝氏度)'] = temp8[time]
            weather1['體感溫度(攝氏度)'] = AT8[time]
            weather1['天氣預報綜合描述'] = WD8index[time] 
            writer.writerow(weather1)          
locationtemp9 = []
locationRH9 = []
locationPoP12h9 = []
locationCI9 =[]
locationAT9 = []
locationWx9 = []
locationWD9 = []
k=0
for item in locationdata9:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp9.append(item)
    if(k==3):
        locationRH9.append(item)
    if(k==5):
        locationPoP12h9.append(item)
    if(k==8):
        locationCI9.append(item)
    if(k==9):
        locationAT9.append(item)
    if(k==10):
        locationWx9.append(item)
    if(k==11):
        locationWD9.append(item)
#print(locationRH9)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime9 = []
for item in locationtemp9:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime9.append(a.group())
#print (locationtime9)
temp9 = []
for item in locationtemp9:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp9.append(a.group())
#print(temp9)
RH9= []
for item in locationRH9:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH9.append(a.group())
#print(RH9)
PoP12h9 = []
for item in locationPoP12h9:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h9.append(a.group())
#print(PoP12h9)
PoP12h9time = []
for item in locationPoP12h9:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h9time.append(a.group())
#print(PoP12h9time)
CI9 = []
for item in locationCI9:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI9.append(a.group())
#print(CI9)
CI9index = []
k=5
for item in range(k,len(locationCI9)):
    if(k>len(locationCI9)):
        break
    a= locationCI9[k]
    CI9index.append(a)
    k=k+5
#print(CI9index)
AT9 = []
for item in locationAT9:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT9.append(a.group())
#print(AT9)
Wx9index = []
k=4
for item in range(k,len(locationWx9)):
    if(k>len(locationWx9)):
        break
    a= locationWx9[k]
    Wx9index.append(a)
    k=k+6
#print(Wx9index)
Wx9time = []
for item in locationWx9:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx9time.append(a.group())
#print(Wx9time)
WD9index = []
k=4
for item in locationWD9:
    if(k>len(locationWD9)):
        break
    a= locationWD9[k]
    WD9index.append(a)
    k=k+4
#print(WD9index)
WD9time = []
for item in locationWD9:
    a=re.match(pattern,item , flags = False)
    if a:
        WD9time.append(a.group())
#print(WD9time)

import codecs
weather = dict()
weather1 = dict()
with open ('大園區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '大園區'
    weather1['地區'] = '大園區'
    for time in range(len(locationtime9)):
        if(time<6):
            weather['時間'] = locationtime9[time]
            weather['溫度(攝氏度)'] = temp9[time]
            weather['相對溼度'] = RH9[time]
            weather['降雨機率時間'] = PoP12h9time[time]
            weather['降雨機率'] = PoP12h9[time]
            weather['舒適度指數'] = CI9[time]
            weather['舒適度指標'] = CI9index[time]
            weather['體感溫度(攝氏度)'] = AT9[time]
            weather['天氣現象'] = Wx9index[time]
            weather['天氣預報綜合描述'] = WD9index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime9[time]
            weather1['溫度(攝氏度)'] = temp9[time]
            weather1['相對溼度'] = RH9[time]
            weather1['舒適度指數'] = CI9[time]
            weather1['舒適度指標'] = CI9index[time]
            weather1['體感溫度(攝氏度)'] = AT9[time]
            weather1['天氣現象'] = Wx9index[time]
            weather1['天氣預報綜合描述'] = WD9index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('大園區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '大園區'
    weather1['地區'] = '大園區'
    for time in range(len(locationtime9)):
        if(time<6):
            weather['時間'] = locationtime9[time]
            weather['溫度(攝氏度)'] = temp9[time]
            weather['體感溫度(攝氏度)'] = AT9[time]
            weather['天氣預報綜合描述'] = WD9index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime9[time]
            weather1['溫度(攝氏度)'] = temp9[time]
            weather1['體感溫度(攝氏度)'] = AT9[time]
            weather1['天氣預報綜合描述'] = WD9index[time] 
            writer.writerow(weather1)           
locationtemp10 = []
locationRH10 = []
locationPoP12h10 = []
locationCI10 =[]
locationAT10 = []
locationWx10 = []
locationWD10 = []
k=0
for item in locationdata10:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp10.append(item)
    if(k==3):
        locationRH10.append(item)
    if(k==5):
        locationPoP12h10.append(item)
    if(k==8):
        locationCI10.append(item)
    if(k==9):
        locationAT10.append(item)
    if(k==10):
        locationWx10.append(item)
    if(k==11):
        locationWD10.append(item)
#print(locationPoP12h10)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime10 = []
for item in locationtemp10:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime10.append(a.group())
#print (locationtime10)
temp10 = []
for item in locationtemp10:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp10.append(a.group())
#print(temp10)
RH10= []
for item in locationRH10:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH10.append(a.group())
#print(RH10)
PoP12h10 = []
for item in locationPoP12h10:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h10.append(a.group())
#print(PoP12h10)
PoP12h10time = []
for item in locationPoP12h10:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h10time.append(a.group())
#print(PoP12h10time)
CI10 = []
for item in locationCI10:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI10.append(a.group())
#print(CI10)
CI10index = []
k=5
for item in range(k,len(locationCI10)):
    if(k>len(locationCI10)):
        break
    a= locationCI10[k]
    CI10index.append(a)
    k=k+5
#print(CI10index)
AT10 = []
for item in locationAT10:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT10.append(a.group())
#print(AT10)
Wx10index = []
k=4
for item in range(k,len(locationWx10)):
    if(k>len(locationWx10)):
        break
    a= locationWx10[k]
    Wx10index.append(a)
    k=k+6
#print(Wx10index)
Wx10time = []
for item in locationWx10:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx10time.append(a.group())
#print(Wx10time)
WD10index = []
k=4
for item in locationWD10:
    if(k>len(locationWD10)):
        break
    a= locationWD10[k]
    WD10index.append(a)
    k=k+4
#print(WD10index)
WD10time = []
for item in locationWD10:
    a=re.match(pattern,item , flags = False)
    if a:
        WD10time.append(a.group())
#print(WD10time)

import codecs
weather = dict()
weather1 = dict()
with open ('龍潭區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '龍潭區'
    weather1['地區'] = '龍潭區'
    for time in range(len(locationtime10)):
        if(time<6):
            weather['時間'] = locationtime10[time]
            weather['溫度(攝氏度)'] = temp10[time]
            weather['相對溼度'] = RH10[time]
            weather['降雨機率時間'] = PoP12h10time[time]
            weather['降雨機率'] = PoP12h10[time]
            weather['舒適度指數'] = CI10[time]
            weather['舒適度指標'] = CI10index[time]
            weather['體感溫度(攝氏度)'] = AT10[time]
            weather['天氣現象'] = Wx10index[time]
            weather['天氣預報綜合描述'] = WD10index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime10[time]
            weather1['溫度(攝氏度)'] = temp10[time]
            weather1['相對溼度'] = RH10[time]
            weather1['舒適度指數'] = CI10[time]
            weather1['舒適度指標'] = CI10index[time]
            weather1['體感溫度(攝氏度)'] = AT10[time]
            weather1['天氣現象'] = Wx10index[time]
            weather1['天氣預報綜合描述'] = WD10index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('龍潭區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '龍潭區'
    weather1['地區'] = '龍潭區'
    for time in range(len(locationtime10)):
        if(time<6):
            weather['時間'] = locationtime10[time]
            weather['溫度(攝氏度)'] = temp10[time]
            weather['體感溫度(攝氏度)'] = AT10[time]
            weather['天氣預報綜合描述'] = WD10index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime10[time]
            weather1['溫度(攝氏度)'] = temp10[time]
            weather1['體感溫度(攝氏度)'] = AT10[time]
            weather1['天氣預報綜合描述'] = WD10index[time] 
            writer.writerow(weather1)       
locationtemp11 = []
locationRH11 = []
locationPoP12h11 = []
locationCI11 =[]
locationAT11 = []
locationWx11 = []
locationWD11 = []
k=0
for item in locationdata11:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp11.append(item)
    if(k==3):
        locationRH11.append(item)
    if(k==5):
        locationPoP12h11.append(item)
    if(k==8):
        locationCI11.append(item)
    if(k==9):
        locationAT11.append(item)
    if(k==10):
        locationWx11.append(item)
    if(k==11):
        locationWD11.append(item)
#print(locationCI11)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime11 = []
for item in locationtemp11:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime11.append(a.group())
#print (locationtime11)
temp11 = []
for item in locationtemp11:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp11.append(a.group())
#print(temp11)
RH11= []
for item in locationRH11:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH11.append(a.group())
#print(RH11)
PoP12h11 = []
for item in locationPoP12h11:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h11.append(a.group())
#print(PoP12h11)
PoP12h11time = []
for item in locationPoP12h11:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h11time.append(a.group())
#print(PoP12h11time)
CI11 = []
for item in locationCI11:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI11.append(a.group())
#print(CI11)
CI11index = []
k=5
for item in range(k,len(locationCI11)):
    if(k>len(locationCI11)):
        break
    a= locationCI11[k]
    CI11index.append(a)
    k=k+5
#print(CI11index)
AT11 = []
for item in locationAT11:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT11.append(a.group())
#print(AT11)
Wx11index = []
k=4
for item in range(k,len(locationWx11)):
    if(k>len(locationWx11)):
        break
    a= locationWx11[k]
    Wx11index.append(a)
    k=k+6
#print(Wx11index)
Wx11time = []
for item in locationWx11:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx11time.append(a.group())
#print(Wx11time)
WD11index = []
k=4
for item in locationWD11:
    if(k>len(locationWD11)):
        break
    a= locationWD11[k]
    WD11index.append(a)
    k=k+4
#print(WD11index)
WD11time = []
for item in locationWD11:
    a=re.match(pattern,item , flags = False)
    if a:
        WD11time.append(a.group())
#print(WD11time)
weather = dict()
weather1 = dict()
with open ('楊梅區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '楊梅區'
    weather1['地區'] = '楊梅區'
    for time in range(len(locationtime11)):
        if(time<6):
            weather['時間'] = locationtime11[time]
            weather['溫度(攝氏度)'] = temp11[time]
            weather['相對溼度'] = RH11[time]
            weather['降雨機率時間'] = PoP12h11time[time]
            weather['降雨機率'] = PoP12h11[time]
            weather['舒適度指數'] = CI11[time]
            weather['舒適度指標'] = CI11index[time]
            weather['體感溫度(攝氏度)'] = AT11[time]
            weather['天氣現象'] = Wx11index[time]
            weather['天氣預報綜合描述'] = WD11index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime11[time]
            weather1['溫度(攝氏度)'] = temp11[time]
            weather1['相對溼度'] = RH11[time]
            weather1['舒適度指數'] = CI11[time]
            weather1['舒適度指標'] = CI11index[time]
            weather1['體感溫度(攝氏度)'] = AT11[time]
            weather1['天氣現象'] = Wx11index[time]
            weather1['天氣預報綜合描述'] = WD11index[time] 
            writer.writerow(weather1)
import codecs
weather = dict()
weather1 = dict()
with open ('楊梅區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '楊梅區'
    weather1['地區'] = '楊梅區'
    for time in range(len(locationtime11)):
        if(time<6):
            weather['時間'] = locationtime11[time]
            weather['溫度(攝氏度)'] = temp11[time]
            weather['體感溫度(攝氏度)'] = AT11[time]
            weather['天氣預報綜合描述'] = WD11index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime11[time]
            weather1['溫度(攝氏度)'] = temp11[time]
            weather1['體感溫度(攝氏度)'] = AT11[time]
            weather1['天氣預報綜合描述'] = WD11index[time] 
            writer.writerow(weather1)
            
locationtemp12 = []
locationRH12 = []
locationPoP12h12 = []
locationCI12 =[]
locationAT12 = []
locationWx12 = []
locationWD12 = []
k=0
for item in locationdata12:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp12.append(item)
    if(k==3):
        locationRH12.append(item)
    if(k==5):
        locationPoP12h12.append(item)
    if(k==8):
        locationCI12.append(item)
    if(k==9):
        locationAT12.append(item)
    if(k==10):
        locationWx12.append(item)
    if(k==11):
        locationWD12.append(item)
#print(locationWx12)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime12 = []
for item in locationtemp12:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime12.append(a.group())
#print (locationtime12)
temp12 = []
for item in locationtemp12:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp12.append(a.group())
#print(temp12)
RH12= []
for item in locationRH12:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH12.append(a.group())
#print(RH12)
PoP12h12 = []
for item in locationPoP12h12:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h12.append(a.group())
#print(PoP12h12)
PoP12h12time = []
for item in locationPoP12h12:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h12time.append(a.group())
#print(PoP12h12time)
CI12 = []
for item in locationCI12:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI12.append(a.group())
#print(CI12)
CI12index = []
k=5
for item in range(k,len(locationCI12)):
    if(k>len(locationCI12)):
        break
    a= locationCI12[k]
    CI12index.append(a)
    k=k+5
#print(CI12index)
AT12 = []
for item in locationAT12:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT12.append(a.group())
#print(AT12)
Wx12index = []
k=4
for item in range(k,len(locationWx12)):
    if(k>len(locationWx12)):
        break
    a= locationWx12[k]
    Wx12index.append(a)
    k=k+6
#print(Wx12index)
Wx12time = []
for item in locationWx12:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx12time.append(a.group())
#print(Wx12time)
WD12index = []
k=4
for item in locationWD12:
    if(k>len(locationWD12)):
        break
    a= locationWD12[k]
    WD12index.append(a)
    k=k+4
#print(WD12index)
WD12time = []
for item in locationWD12:
    a=re.match(pattern,item , flags = False)
    if a:
        WD12time.append(a.group())
#print(WD12time)

import codecs
weather = dict()
weather1 = dict()
with open ('八德區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '八德區'
    weather1['地區'] = '八德區'
    for time in range(len(locationtime12)):
        if(time<6):
            weather['時間'] = locationtime12[time]
            weather['溫度(攝氏度)'] = temp12[time]
            weather['相對溼度'] = RH12[time]
            weather['降雨機率時間'] = PoP12h12time[time]
            weather['降雨機率'] = PoP12h12[time]
            weather['舒適度指數'] = CI12[time]
            weather['舒適度指標'] = CI12index[time]
            weather['體感溫度(攝氏度)'] = AT12[time]
            weather['天氣現象'] = Wx12index[time]
            weather['天氣預報綜合描述'] = WD12index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime12[time]
            weather1['溫度(攝氏度)'] = temp12[time]
            weather1['相對溼度'] = RH12[time]
            weather1['舒適度指數'] = CI12[time]
            weather1['舒適度指標'] = CI12index[time]
            weather1['體感溫度(攝氏度)'] = AT12[time]
            weather1['天氣現象'] = Wx12index[time]
            weather1['天氣預報綜合描述'] = WD12index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('八德區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '八德區'
    weather1['地區'] = '八德區'
    for time in range(len(locationtime12)):
        if(time<6):
            weather['時間'] = locationtime12[time]
            weather['溫度(攝氏度)'] = temp12[time]
            weather['體感溫度(攝氏度)'] = AT12[time]
            weather['天氣預報綜合描述'] = WD12index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime12[time]
            weather1['溫度(攝氏度)'] = temp12[time]
            weather1['體感溫度(攝氏度)'] = AT12[time]
            weather1['天氣預報綜合描述'] = WD12index[time] 
            writer.writerow(weather1)            
locationtemp13 = []
locationRH13 = []
locationPoP12h13 = []
locationCI13 =[]
locationAT13 = []
locationWx13 = []
locationWD13 = []
k=0
for item in locationdata13:
    if(item == "T" or item == "RH" or item == "PoP12h"  or item == "CI" or item == "AT" or item == "Wx" or item == "WeatherDescription"
      or item == "Td" or item == "PoP6h" or item == "WD" or item == "WS" ):
        k=k+1
    if(k==1):
        locationtemp13.append(item)
    if(k==3):
        locationRH13.append(item)
    if(k==5):
        locationPoP12h13.append(item)
    if(k==8):
        locationCI13.append(item)
    if(k==9):
        locationAT13.append(item)
    if(k==10):
        locationWx13.append(item)
    if(k==11):
        locationWD13.append(item)
#print(locationWD13)
pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{2}:[0-9]{2}'
pattern1 = '^-?[0-9]{2}$'
pattern2 = '^-?[0-9]{1,3}$'
locationtime13 = []
for item in locationtemp13:
    a=re.match(pattern,item , flags = False)
    if a:
        locationtime13.append(a.group())
#print (locationtime13)
temp13 = []
for item in locationtemp13:
    a=re.match(pattern1,item , flags = False)
    if a:
        temp13.append(a.group())
#print(temp13)
RH13= []
for item in locationRH13:
    a=re.match(pattern2,item , flags = False)
    if a:
        RH13.append(a.group())
#print(RH13)
PoP12h13 = []
for item in locationPoP12h13:
    a=re.match(pattern2,item , flags = False)
    if a:
        PoP12h13.append(a.group())
#print(PoP12h13)
PoP12h13time = []
for item in locationPoP12h13:
    a=re.match(pattern,item , flags = False)
    if a:
        PoP12h13time.append(a.group())
#print(PoP12h13time)
CI13 = []
for item in locationCI13:
    a=re.match(pattern1,item , flags = False)
    if a:
        CI13.append(a.group())
#print(CI13)
CI13index = []
k=5
for item in range(k,len(locationCI13)):
    if(k>len(locationCI13)):
        break
    a= locationCI13[k]
    CI13index.append(a)
    k=k+5
#print(CI13index)
AT13 = []
for item in locationAT13:
    a=re.match(pattern2,item , flags = False)
    if a:
        AT13.append(a.group())
#print(AT13)
Wx13index = []
k=4
for item in range(k,len(locationWx13)):
    if(k>len(locationWx13)):
        break
    a= locationWx13[k]
    Wx13index.append(a)
    k=k+6
#print(Wx13index)
Wx13time = []
for item in locationWx13:
    a=re.match(pattern,item , flags = False)
    if a:
        Wx13time.append(a.group())
#print(Wx13time)
WD13index = []
k=4
for item in locationWD13:
    if(k>len(locationWD13)):
        break
    a= locationWD13[k]
    WD13index.append(a)
    k=k+4
#print(WD13index)
WD13time = []
for item in locationWD13:
    a=re.match(pattern,item , flags = False)
    if a:
        WD13time.append(a.group())
#print(WD13time)

import codecs
weather = dict()
weather1 = dict()
with open ('平鎮區.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','相對溼度','降雨機率時間','降雨機率','舒適度指數','舒適度指標','體感溫度(攝氏度)','天氣現象','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '平鎮區'
    weather1['地區'] = '平鎮區'
    for time in range(len(locationtime13)):
        if(time<6):
            weather['時間'] = locationtime13[time]
            weather['溫度(攝氏度)'] = temp13[time]
            weather['相對溼度'] = RH13[time]
            weather['降雨機率時間'] = PoP12h13time[time]
            weather['降雨機率'] = PoP12h13[time]
            weather['舒適度指數'] = CI13[time]
            weather['舒適度指標'] = CI13index[time]
            weather['體感溫度(攝氏度)'] = AT13[time]
            weather['天氣現象'] = Wx13index[time]
            weather['天氣預報綜合描述'] = WD13index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime13[time]
            weather1['溫度(攝氏度)'] = temp13[time]
            weather1['相對溼度'] = RH13[time]
            weather1['舒適度指數'] = CI13[time]
            weather1['舒適度指標'] = CI13index[time]
            weather1['體感溫度(攝氏度)'] = AT13[time]
            weather1['天氣現象'] = Wx13index[time]
            weather1['天氣預報綜合描述'] = WD13index[time] 
            writer.writerow(weather1)
weather = dict()
weather1 = dict()
with open ('平鎮區_溫度.csv', 'w', newline = '',encoding='big5') as csvfile:
    datanames = ['地區','時間','溫度(攝氏度)','體感溫度(攝氏度)','天氣預報綜合描述']
    writer = csv.DictWriter(csvfile , fieldnames = datanames)
    writer.writeheader()
    weather['地區'] = '平鎮區'
    weather1['地區'] = '平鎮區'
    for time in range(len(locationtime13)):
        if(time<6):
            weather['時間'] = locationtime13[time]
            weather['溫度(攝氏度)'] = temp13[time]
            weather['體感溫度(攝氏度)'] = AT13[time]
            weather['天氣預報綜合描述'] = WD13index[time] 
            writer.writerow(weather)
        else:
            weather1['時間'] = locationtime13[time]
            weather1['溫度(攝氏度)'] = temp13[time]
            weather1['體感溫度(攝氏度)'] = AT13[time]
            weather1['天氣預報綜合描述'] = WD13index[time] 
            writer.writerow(weather1)            
