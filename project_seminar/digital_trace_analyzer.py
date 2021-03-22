# -*- coding: utf-8 -*-
"""
@author: ttyomaaa
"""

import json
import datetime 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data=[]
path = 'C:/Users/Evgeniy/Desktop/psem/jitsiusers'
grade=0
count1=0
count2=0
count3=0
datelist={}
start =  datetime.datetime.strptime("2020-01-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-04-1", "%Y-%m-%d")

days = mdates.drange(start,end,datetime.timedelta(days=1))
n=len(days)

values=[]
for i in range(n):
    values.append(0)

     
with open(path,'r',encoding='utf-8') as f:
    
    for line in f:
        json_line = json.loads(line)
        data.append(json_line)
        
    for i in data:
        try:
            if (i["username"]=="dkorolev@miem.hse.ru") and (i["room"]=="312"):                   
                datex = datetime.datetime.strptime(i["date"],"%Y-%m-%d")
                values[int(mdates.date2num(datex)-mdates.date2num(start))]=1                                 
        except KeyError:
            continue

fig = plt.figure(dpi=1200)

tmp=0
for i in range(n):
    if values[i]!=0: 
        tmp+=values[i]
        grade+=0.5
        count1+=1
    values[i]=tmp

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
plt.plot(days,values)


for i in range(n): values[i]=0

path = 'C:/Users/Evgeniy/Desktop/psem/zulip'

data=[]
with open(path,'r',encoding='utf-8') as f:
    
    for line in f:
        json_line = json.loads(line)
        data.append(json_line)
        
    for i in data:
        if i["email"]=="dkorolev@miem.hse.ru" :
            if len(i["messages"])!=0: 
                for j in i["messages"]:
                    datex = datetime.datetime.strptime(j["timestamp"]["$date"],"%Y-%m-%dT%H:%M:%S.%fZ")
                    if int(mdates.date2num(datex)-mdates.date2num(start))>=0:
                        values[int(mdates.date2num(datex)-mdates.date2num(start))]+=1
                        count2+=1   

tmp=0
for i in range(n):
    if values[i]!=0: 
        tmp+=values[i]
    values[i]=tmp

plt.plot(days,values)

if count2!=0:
    grade+=2
    
for i in range(n): values[i]=0

path = 'C:/Users/Evgeniy/Desktop/psem/git'

data=[]
with open(path,'r',encoding='utf-8') as f:
    
    for line in f:
        json_line = json.loads(line)
        data.append(json_line)
        
    for i in data:
        if i["email"]=="dkorolev@miem.hse.ru":
            grade+=1
        for j in i["projects"]:
            if j["commits"]:
                for k in j["commits"]:
                        if k["committer_email"]=="dkorolev@miem.hse.ru":                            
                            datex = datetime.datetime.strptime(k["committed_date"]["$date"],"%Y-%m-%dT%H:%M:%S.%fZ")
                            if int(mdates.date2num(datex)-mdates.date2num(start))>=0:
                                values[int(mdates.date2num(datex)-mdates.date2num(start))]+=1
                                count3+=1   

if count3!=0: grade+=1

tmp=0
for i in range(n):
    if values[i]!=0: 
        tmp+=values[i]
    values[i]=tmp

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
plt.plot(days,values)

plt.legend(['Посещенные семинары: '+str(count1), 'Сообщения в Zulip: '+str(count2), 'Коммиты в GitLab: '+str(count3)])
plt.gcf().autofmt_xdate()
plt.show()

print(grade)

