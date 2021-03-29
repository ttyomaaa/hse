import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

grade=0
count0=0
count1=0
count2=0
count3=0
flag1=0
flag2=0
user_mail="aenepomnyaschiy@miem.hse.ru"

start =  datetime.datetime.strptime("2021-01-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-04-1", "%Y-%m-%d")

days = mdates.drange(start,end,datetime.timedelta(days=1))
n=len(days)
values=[]
for i in range(n):
    values.append(0)

poster_session = [datetime.datetime.strptime("2021-01-25","%Y-%m-%d"),
                           datetime.datetime.strptime("2021-01-26","%Y-%m-%d"),
                           datetime.datetime.strptime("2021-01-27","%Y-%m-%d"),
                           datetime.datetime.strptime("2021-01-28","%Y-%m-%d"),
                           datetime.datetime.strptime("2021-01-29","%Y-%m-%d")]
start1=datetime.datetime.strptime("10:00:00", "%H:%M:%S")
end1=datetime.datetime.strptime("12:30:00", "%H:%M:%S")
start2=datetime.datetime.strptime("13:30:00", "%H:%M:%S")
end2=datetime.datetime.strptime("16:00:00", "%H:%M:%S")

########################################################
path = '/home/student/rawData/JitsiSession.json'

with open(path,'r',encoding='utf-8') as f:

    data0=json.load(f)

    for i in data0:
        try:
            if (i["username"]==user_mail) and (i["room"]=="312"):
                datex = datetime.datetime.strptime(i["date"],"%Y-%m-%d")
                values[int(mdates.date2num(datex)-mdates.date2num(start))]=1
        except KeyError:
            continue


tmp=0
for i in range(n):
    if values[i]!=0:
        tmp+=values[i]
        grade+=0.5
        count1+=1
    values[i]=tmp



fig = plt.figure(dpi=1200)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))

plt.plot(days,values)


for i in range(n): values[i]=0

########################################################
path = '/home/student/rawData/JitsiSession.json'

with open(path,'r',encoding='utf-8') as f:

    data0=json.load(f)

    for i in data0:
        try:
            if (i["username"]==user_mail) and (i["room"][0:7] == "project"):
                datex = datetime.datetime.strptime(i["date"],"%Y-%m-%d")
                if datex in poster_session:
                    timex1 = datetime.datetime.strptime(i["begin"],"%H:%M:%S.%f")
                    timex2 = datetime.datetime.strptime(i["end"],"%H:%M:%S.%f")
                    if (timex1<end1 and timex2>start1) or (timex1<end2 and timex2>start2):
                        values[int(mdates.date2num(datex)-mdates.date2num(start))]=1
        except KeyError:
            continue



tmp=0
for i in range(n):
    if values[i]!=0:
        tmp+=values[i]
        grade+=0.5
        count0+=1
    values[i]=tmp


plt.plot(days,values)


for i in range(n): values[i]=0
######################################################
path = '/home/student/rawData/ZulipStats.json'

with open(path,'r',encoding='utf-8') as f:


    data0=json.load(f)

    for i in data0:
        if i["email"]==user_mail :
            flag1=1
            if len(i["messages"])!=0:
                for j in i["messages"]:
                    datex = datetime.datetime.strptime(j["timestamp"],"%Y-%m-%dT%H:%M:%S.%fZ")
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
####################################################
path = '/home/student/rawData/GitStats.json'

with open(path,'r',encoding='utf-8') as f:

    data0=json.load(f)

    for i in data0:
        if i["email"]==user_mail:
            flag2=1
            grade+=1
            for j in i["projects"]:
                if j["commits"]:
                    for k in j["commits"]:
                        datex = datetime.datetime.strptime(k["committed_date"],"%Y-%m-%dT%H:%M:%S.%fZ")
                        if int(mdates.date2num(datex)-mdates.date2num(start))>=0:
                            values[int(mdates.date2num(datex)-mdates.date2num(start))]+=1
                            count3+=1

if count3!=0: grade+=1

tmp=0
for i in range(n):
    if values[i]!=0:
        tmp+=values[i]
    values[i]=tmp

plt.plot(days,values)
#####################

if flag1==0 and flag2==0:
    plt.legend(['Посещенные семинары: '+str(count1), 'Посещенные проекты: '+str(count0),'Сообщения в Zulip: отсутствует аккаунт(0) ', 'Коммиты в GitLab: отсутствует аккаунт(0)'])
elif flag1==1 and flag2==0:
    plt.legend(['Посещенные семинары: '+str(count1), 'Посещенные проекты: '+str(count0),'Сообщения в Zulip: '+str(count2), 'Коммиты в GitLab: отсутствует аккаунт(0)'])
elif flag1==0 and flag2==1:
    plt.legend(['Посещенные семинары: '+str(count1), 'Посещенные проекты: '+str(count0),'Сообщения в Zulip: отсутствует аккаунт(0) ', 'Коммиты в GitLab: '+str(count3)])
else:
    plt.legend(['Посещенные семинары: '+str(count1), 'Посещенные проекты: '+str(count0),'Сообщения в Zulip: '+str(count2), 'Коммиты в GitLab: '+str(count3)])

plt.title("Данные для: "+user_mail)

plt.xlabel('Итоговая оценка: '+str(round(grade)))

plt.gcf().autofmt_xdate()
plt.savefig('/home/student/student_stats/aenepomnyaschiy/graph.jpg')
#plt.show()
html_page = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Оценка активности студента</title>
    </head>
    <body>
        <div align="center">
        <h1><font size="7" color="black" face="Arial">Оценка активности студента</h1>
        <img style="width: 1200px; background-size: 100%;" src='graph.jpg'>
        </div>
    </body>
</html>
            """

with open("/home/student/student_stats/aenepomnyaschiy/aenepomnyaschiy.html", "w", encoding='utf-8') as page:
    page.write(html_page)
