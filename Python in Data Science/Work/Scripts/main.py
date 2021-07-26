# -*- coding: utf-8 -*-

# Импортируем все из библиотеки TKinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
import sys

path = os.getcwd()
os.chdir(os.path.abspath(os.path.join(path, '..')))
sys.path.append(os.path.join(os.getcwd(), 'Library'))

from functions import *

def on_closing():
    """
    Функция сохранения изменённой базы данных в новый файл, 
    а также вопроса, хочет ли пользователь действительно выйти из приложения.
    Автор Айрапетян Т.
    """
    fout = open("./test.txt", "w")
    print(*data, sep="\n", file=fout)
    fout.close()

    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()

def select_record():
    """
    Функция очистки полей ввода в таблице, расположенной ниже БД для нового ввода конкретных значений 
    выбранной пользователем сущности для дальнейшего редактирования
    Автор Айрапетян Т.
    """
    global m1,m2,m3,m4,m5,m6,m7,m8
    m1.delete(0,END)
    m2.delete(0,END)
    m3.delete(0,END)
    m4.delete(0,END)
    m5.delete(0,END)
    m6.delete(0,END)
    m7.delete(0,END)
    m8.delete(0,END)
    
    selected=database.focus()
    values = database.item(selected,'values')
    m1.insert(0,values[0])
    m2.insert(0,values[1])
    m3.insert(0,values[2])
    m4.insert(0,values[3])
    m5.insert(0,values[4])
    m6.insert(0,values[5])
    m7.insert(0,values[6])
    m8.insert(0,values[7])


def update_record():
    """
    Функция сохранения отредактированных данных в БД и последуюей очисткой полей ввода таблицы
    Автор Айрапетян Т.
    """
    global m1,m2,m3,m4,m5,m6,m7,m8
    selected=database.focus()

    ind = find_data_index(m1.get(),data)
    data[ind] = convert_to_data_record(m1, m2, m3, m4, m5, m6, m7, m8)
    database.item(selected,text="",values=data[ind])

    m1.delete(0,END)
    m2.delete(0,END)
    m3.delete(0,END)
    m4.delete(0,END)
    m5.delete(0,END)
    m6.delete(0,END)
    m7.delete(0,END)
    m8.delete(0,END)

def knopka_baza_dannyh():
    """
    Функция создания нового окна приложения, на котором будет расположена база данных, 
    таблица для изменений значений атрибутов у любой сущности, а также кнопки, 
    позволяющие пользователю совершить то или иное действие, прописанное в ТЗ
    Автор Айрапетян Т.
    """
    global count,database,number,m1,m2,m3,m4,m5,m6,m7,m8
    #создаём новое окно
    baza_dannyh=Toplevel(tk)
    baza_dannyh.title("Dream_car.База данных")
    baza_dannyh.resizable(0, 0)
    #создаём область для размещения объектов
    canvas1=Canvas(baza_dannyh, width=1200,height=500,bg="#40E0D0")
    canvas1.pack()
    frame_top1 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1.place(relx=0, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top1, text='Добавить',command=knopka_dobavlenie,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    frame_top2 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top2.place(relx=0.2, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top2, text='Удалить',command=knopka_udalenie,height = 20, width = 100,activebackground="#40E0D0")
    btn.pack()
    frame_top3 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top3.place(relx=0.4, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top3, text='Граф.отчёт',command=knopka_graf_otchet,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    frame_top4 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top4.place(relx=0.6, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top4, text='Текст.отчёт',command=knopka_text_otchet,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    frame_top5 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top5.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top5, text='Сохранение',command=knopka_sohranenie,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    frame_top1235 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1235.place(relx=0, rely=0.70, relwidth=0.8, relheight=0.13)
    #создаём таблицу для изменения БД
    n1=Label(frame_top1235,text="Номер")
    n1.grid(row=0,column=0)
    n2=Label(frame_top1235,text="Модель")
    n2.grid(row=0,column=1)
    n3=Label(frame_top1235,text="Производство")
    n3.grid(row=0,column=2)
    n4=Label(frame_top1235,text="Количество сидений")
    n4.grid(row=0,column=3)
    n5=Label(frame_top1235,text="Кузов")
    n5.grid(row=0,column=4)
    n6=Label(frame_top1235,text="Цвет")
    n6.grid(row=0,column=5)
    n7=Label(frame_top1235,text="Комплектация")
    n7.grid(row=0,column=6)
    n8=Label(frame_top1235,text="Доп.цена")
    n8.grid(row=0,column=7)
    m1=Entry(frame_top1235)
    m1.grid(row=1,column=0)
    m2=Entry(frame_top1235)
    m2.grid(row=1,column=1)
    m3=Entry(frame_top1235)
    m3.grid(row=1,column=2)
    m4=Entry(frame_top1235)
    m4.grid(row=1,column=3)
    m5=Entry(frame_top1235)
    m5.grid(row=1,column=4)
    m6=Entry(frame_top1235)
    m6.grid(row=1,column=5)
    m7=Entry(frame_top1235)
    m7.grid(row=1,column=6)
    m8=Entry(frame_top1235)
    m8.grid(row=1,column=7)
    
    frame_top1234 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1234.place(relx=0.8, rely=0.70, relwidth=0.1, relheight=0.13)
    btn = Button(frame_top1234, text='Изменить',command=select_record,height = 20, width = 35,activebackground="#40E0D0")
    btn.pack()
    frame_top1236 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1236.place(relx=0.9, rely=0.70, relwidth=0.10, relheight=0.13)
    btn = Button(frame_top1236, text='Сохранить',command=update_record,height = 20, width = 35,activebackground="#40E0D0")
    btn.pack()
    
    
    
    #создаём поля для базы данных и полосы прокрутки
    frame_top1001 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1001.place(relx=0, rely=0, relwidth=1, relheight=0.7)
    frame_top1009 = Frame(baza_dannyh, bg='#40E0D0', bd=5)
    frame_top1009.place(relx=0.98, rely=0.1, relwidth=1, relheight=0.47)
    #создаём полосу прокрутки
    database_scroll=Scrollbar(frame_top1009)
    database_scroll.pack(side=LEFT,fill=Y)
    #создаём таблицу и присоединяем полосу прокрутки к ней
    database = ttk.Treeview(frame_top1001,yscrollcommand=database_scroll.set)
    database['columns']= ("Номер","Модель","Производство","Количество сидений","Кузов","Цвет","Комплектация","Доп.цена")
    #размеры столбцов
    database.column("#0",width=0, stretch=NO)
    database.column("Номер",width=60)
    database.column("Модель",width=180)
    database.column("Производство",width=160)
    database.column("Количество сидений",width=130, anchor=CENTER)
    database.column("Кузов",width=167)
    database.column("Цвет",width=200)
    database.column("Комплектация",width=180)
    database.column("Доп.цена",width=77, anchor=CENTER)
    #названия столбцов
    database.heading("#0",text="")
    database.heading("Номер",text="Номер")
    database.heading("Модель",text="Модель")
    database.heading("Производство",text="Производство")
    database.heading("Количество сидений",text="Количество сидений")
    database.heading("Кузов",text="Кузов")
    database.heading("Цвет",text="Цвет")
    database.heading("Комплектация",text="Комплектация")
    database.heading("Доп.цена",text="Доп.цена")
    database_scroll.config(command=database.yview)
    #database.insert(parent='', index='end', iid=0,text="1",values=(1,"Audi","AMG",5,"внедорожник","белый","базовая",0))
    
    count=0
    for record in data:
        database.insert(parent='', index='end', iid=count,text="1",values=record)
        count+=1
    database.pack(pady=50)
    

def knopka_spravochnicki():
    """
    Функция создания нового окна приложения, на котором будут расположены кнопки,  
    позволяющие пользователю просмотреть используемые справочники в создании БД
    Автор Айрапетян Т.
    """
    redactirovanie=Toplevel(tk)
    redactirovanie.title("Dream_car.Используемые справочники")
    redactirovanie.resizable(0, 0)
    canvas2=Canvas(redactirovanie, width=900,height=500,bg="purple")
    canvas2.pack()
    frame_bottom1 = Frame(redactirovanie, bg='#FF1493', bd=10)
    frame_bottom1.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)
    info = Label(frame_bottom1, text='Выберите справочник:', bg='#FF1493', font=40)
    info.pack()
    frame_bottom2 = Frame(redactirovanie, bg='#FF1493', bd=10)
    frame_bottom2.place(relx=0.15, rely=0.3, relwidth=0.3, relheight=0.1)
    btn = Button(frame_bottom2, text='Справочник 1',command=knopka_spravochnick1,height = 20, width = 70,activebackground="#ADFF2F")
    btn.pack()
    frame_bottom3 = Frame(redactirovanie, bg='#FF1493', bd=10)
    frame_bottom3.place(relx=0.15, rely=0.6, relwidth=0.3, relheight=0.1)
    btn = Button(frame_bottom3, text='Справочник 2',command=knopka_spravochnick2,height = 20, width = 70,activebackground="#ADFF2F")
    btn.pack()
    frame_bottom4 = Frame(redactirovanie, bg='#FF1493', bd=10)
    frame_bottom4.place(relx=0.55, rely=0.3, relwidth=0.3, relheight=0.1)
    btn = Button(frame_bottom4, text='Справочник 3',command=knopka_spravochnick3,height = 20, width = 70,activebackground="#ADFF2F")
    btn.pack()
    frame_bottom5 = Frame(redactirovanie, bg='#FF1493', bd=10)
    frame_bottom5.place(relx=0.55, rely=0.6, relwidth=0.3, relheight=0.1)
    btn = Button(frame_bottom5, text='Справочник 4',command=knopka_spravochnick4,height = 20, width = 70,activebackground="#ADFF2F")
    btn.pack()
    
def knopka_spravochnick1():
    """
    Функция вывода первого справочника на экран
    Автор Непомнящий А.
    """
    global spravochnick1, data,database
    spravochnick1=Toplevel(tk)
    spravochnick1.title("Dream_car.Используемые справочники.Справочник1")                
    spravochnick1.resizable(0, 0)
    canvas3=Canvas(spravochnick1, width=900,height=500,bg="purple")
    canvas3.pack()
    b1=Button(spravochnick1,text="Назад",command=knopka_spravochnick1_sohranenie,height = 5, width = 20,activebackground="#ADFF2F")
    b1.place(x=760,y=430)
    frame_top1002 = Frame(spravochnick1, bg='purple', bd=5)
    frame_top1002.place(relx=0, rely=0, relwidth=0.9, relheight=0.8)
    frame_top1020 = Frame(spravochnick1, bg='purple', bd=5)
    frame_top1020.place(relx=0.9, rely=0.14, relwidth=0.1, relheight=0.47)
    database_scroll=Scrollbar(frame_top1020)
    database_scroll.pack(side=LEFT,fill=Y)
    database = ttk.Treeview(frame_top1002,yscrollcommand=database_scroll.set)
    database['columns']= ("Модель","Производство","Количество сидений")
    database.column("#0",width=0, stretch=NO)
    database.column("Модель",width=280)
    database.column("Производство",width=290)
    database.column("Количество сидений",width=230, anchor=CENTER)
    database.heading("#0",text="")
    database.heading("Модель",text="Модель")
    database.heading("Производство",text="Производство")
    database.heading("Количество сидений",text="Количество сидений")
    database_scroll.config(command=database.yview)
    #database.insert(parent='', index='end', iid=0,text="1",values=(1,"Audi","AMG",5,"внедорожник","белый","базовая",0))

    count=0
    s1=set()
    for record in data:
        values=(record[1],record[2],record[3])
        if (values in s1):
            continue
        s1.add(values)
        
        database.insert(parent='', index='end', iid=count,text="1",values=(record[1],record[2],record[3]))
        count+=1
    database.pack(pady=70)
    
def knopka_spravochnick1_sohranenie():
    global spravochnick1
    spravochnick1.destroy()
    """
    Функция закрытия первого справочника
    и возвращения на окно "Используемые справочники"
    Автор Непомнящий А.
    """

def knopka_spravochnick2():
    """
    Функция вывода второго справочника на экран
    Автор Непомнящий А.
    """
    global spravochnick2
    spravochnick2=Toplevel(tk)
    spravochnick2.title("Dream_car.Используемые справочники.Справочник2")
    spravochnick2.resizable(0, 0)
    canvas4=Canvas(spravochnick2, width=900,height=500,bg="purple")
    canvas4.pack()
    b2=Button(spravochnick2,text="Назад",command=knopka_spravochnick2_sohranenie,height = 5, width = 20,activebackground="#ADFF2F")
    b2.place(x=760,y=430)
    frame_top1003 = Frame(spravochnick2, bg='purple', bd=5)
    frame_top1003.place(relx=0, rely=0, relwidth=0.9, relheight=0.8)
    frame_top1030 = Frame(spravochnick2, bg='purple', bd=5)
    frame_top1030.place(relx=0.9, rely=0.14, relwidth=0.1, relheight=0.47)
    database_scroll=Scrollbar(frame_top1030)
    database_scroll.pack(side=LEFT,fill=Y)   
    database = ttk.Treeview(frame_top1003,yscrollcommand=database_scroll.set)
    database['columns']= ("Модель","Цвет","Комплектация",)
    database.column("#0",width=0, stretch=NO)
    database.column("Модель",width=280)
    database.column("Цвет",width=300)
    database.column("Комплектация",width=280)
    database.heading("#0",text="")
    database.heading("Модель",text="Модель")
    database.heading("Цвет",text="Цвет")
    database.heading("Комплектация",text="Комплектация")
    database_scroll.config(command=database.yview)
    #database.insert(parent='', index='end', iid=0,text="1",values=(1,"Audi","AMG",5,"внедорожник","белый","базовая",0))
    
    count=0
    for record in data:
        database.insert(parent='', index='end', iid=count,text="1",values=(record[1],record[5],record[6]))
        count+=1
    database.pack(pady=70)

    
def knopka_spravochnick2_sohranenie():
    """
    Функция закрытия первого справочника
    и возвращения на окно "Используемые справочники"
    Автор Непомнящий А.
    """
    global spravochnick2
    spravochnick2.destroy() 
    

def knopka_spravochnick3():
    """
    Функция вывода третьего справочника на экран
    Автор Непомнящий А.
    """
    global spravochnick3
    spravochnick3=Toplevel(tk)
    spravochnick3.title("Dream_car.Используемые справочники.Справочник3")
    spravochnick3.resizable(0, 0)
    canvas5=Canvas(spravochnick3, width=900,height=500,bg="purple")
    canvas5.pack()
    b3=Button(spravochnick3,text="Назад",command=knopka_spravochnick3_sohranenie,height = 5, width = 20,activebackground="#ADFF2F")
    b3.place(x=760,y=430)
    frame_top1004 = Frame(spravochnick3, bg='purple', bd=5)
    frame_top1004.place(relx=0, rely=0, relwidth=1, relheight=0.87)
    database = ttk.Treeview(frame_top1004)
    database['columns']= ("Количество сидений","Кузов")
    database.column("#0",width=0, stretch=NO)
    database.column("Количество сидений",width=330, anchor=CENTER)
    database.column("Кузов",width=370, anchor=CENTER)
    database.heading("#0",text="")
    database.heading("Количество сидений",text="Количество сидений")
    database.heading("Кузов",text="Кузов")
    #database.insert(parent='', index='end', iid=0,text="1",values=(1,"Audi","AMG",5,"внедорожник","белый","базовая",0))
    
    count=0
    s3=set()
    for record in data:
        values=(record[3],record[4])
        
        if (values in s3):
            continue
        s3.add(values)
        
        database.insert(parent='', index='end', iid=count,text="1",values=(record[3],record[4]))
        count+=1
    database.pack(pady=70)
    
def knopka_spravochnick3_sohranenie():
    """
    Функция закрытия первого справочника
    и возвращения на окно "Используемые справочники"
    Автор Непомнящий А.
    """
    global spravochnick3
    spravochnick3.destroy()     


def knopka_spravochnick4():
    """
    Функция вывода четвёртого справочника на экран
    Автор Непомнящий А.
    """
    global spravochnick4
    spravochnick4=Toplevel(tk)
    spravochnick4.title("Dream_car.Используемые справочники.Справочник4")
    spravochnick4.resizable(0, 0)
    canvas6=Canvas(spravochnick4, width=900,height=500,bg="purple")
    canvas6.pack()
    b4=Button(spravochnick4,text="Назад",command=knopka_spravochnick4_sohranenie,height = 5, width = 20,activebackground="#ADFF2F")
    b4.place(x=760,y=430)
    frame_top1005 = Frame(spravochnick4, bg='purple', bd=5)
    frame_top1005.place(relx=0, rely=0, relwidth=1, relheight=0.87)
    database = ttk.Treeview(frame_top1005)
    database['columns']= ("Комплектация","Доп.цена")
    database.column("#0",width=0, stretch=NO)
    database.column("Комплектация",width=380, anchor=CENTER)
    database.column("Доп.цена",width=280, anchor=CENTER)
    database.heading("#0",text="")
    database.heading("Комплектация",text="Комплектация")
    database.heading("Доп.цена",text="Доп.цена")
    #database.insert(parent='', index='end', iid=0,text="1",values=(1,"Audi","AMG",5,"внедорожник","белый","базовая",0))
    
    count=0
    s4 = set()
    for record in data:
        values = (record[6], record[7])

        if (values in s4):
            continue
        s4.add(values)

        database.insert(parent='', index='end', iid=count,text="1",values=(record[6],record[7]))
        count+=1
    database.pack(pady=70)
  

def knopka_spravochnick4_sohranenie():
    """
    Функция закрытия первого справочника
    и возвращения на окно "Используемые справочники"
    Автор Непомнящий А.
    """
    global spravochnick4
    spravochnick4.destroy()  
  
    

def knopka_dobavlenie():
    """
    Функция создания нового окна с поля ввода 
    для добавления новой сущости с указанными от пользователя
    значениями атрибутов
    Автор Айрапетян Т.
    """
    global info4,info6,info8,info10,info12,dobavlenie
    dobavlenie=Toplevel(tk)
    dobavlenie.title("Dream_car.База данных.Добавление")
    dobavlenie.resizable(0, 0)
    canvas7=Canvas(dobavlenie, width=900,height=500,bg="#00CED1")
    canvas7.pack()
    frame_bottom11 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom11.place(relx=0.1, rely=0.01, relwidth=0.17, relheight=0.1)
    info1 = Label(frame_bottom11, text='Атрибуты:', bg='#00FFFF', font=40)
    info1.pack()
    frame_bottom12 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom12.place(relx=0.6, rely=0.01, relwidth=0.17, relheight=0.1)
    info2 = Label(frame_bottom12, text='Значения:', bg='#00FFFF', font=40)
    info2.pack()
    frame_bottom13 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom13.place(relx=0.1, rely=0.14, relwidth=0.17, relheight=0.1)
    info3 = Label(frame_bottom13, text='Модель:', bg='#00FFFF', font=40)
    info3.pack()
    frame_bottom14 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom14.place(relx=0.6, rely=0.14, relwidth=0.17, relheight=0.1)
    # помещаем строку ввода в данный frame
    info4 = Entry(frame_bottom14, bg='white', font=30)
    info4.pack()
    frame_bottom15 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom15.place(relx=0.1, rely=0.27, relwidth=0.17, relheight=0.1)
    info5 = Label(frame_bottom15, text='Производство:', bg='#00FFFF', font=40)
    info5.pack()
    frame_bottom16 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom16.place(relx=0.6, rely=0.27, relwidth=0.17, relheight=0.1)
    info6 = Entry(frame_bottom16, bg='white', font=30)
    info6.pack()
    frame_bottom17 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom17.place(relx=0.1, rely=0.41, relwidth=0.17, relheight=0.1)
    info7 = Label(frame_bottom17, text='Кузов:', bg='#00FFFF', font=40)
    info7.pack()
    frame_bottom18 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom18.place(relx=0.6, rely=0.41, relwidth=0.17, relheight=0.1)
    #размещаем на данном frame выпадающий список
    info8 = ttk.Combobox(frame_bottom18, values=("кроссовер","седан","внедорожник"))
    info8.pack()
    frame_bottom19 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom19.place(relx=0.1, rely=0.55, relwidth=0.17, relheight=0.1)
    info9 = Label(frame_bottom19, text='Цвет:', bg='#00FFFF', font=40)
    info9.pack()
    frame_bottom20 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom20.place(relx=0.6, rely=0.55, relwidth=0.17, relheight=0.1)
    info10 = Entry(frame_bottom20, bg='white', font=30)
    info10.pack()
    frame_bottom21 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom21.place(relx=0.1, rely=0.69, relwidth=0.17, relheight=0.1)
    info11 = Label(frame_bottom21, text='Комплектация:', bg='#00FFFF', font=40)
    info11.pack()
    frame_bottom22 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom22.place(relx=0.6, rely=0.69, relwidth=0.17, relheight=0.1)
    info12 = ttk.Combobox(frame_bottom22,values=("базовая","спорт","престиж","премиум","люкс"))
    info12.pack()
    frame_bottom23 = Frame(dobavlenie, bg='#00FFFF', bd=10)
    frame_bottom23.place(relx=0.35, rely=0.84, relwidth=0.3, relheight=0.1)
    btn13 = Button(frame_bottom23, text='Сохранить',command=get_info_dobavlenie,height = 20, width = 70,activebackground="#ADFF2F")
    btn13.pack()



def get_info_dobavlenie():
    """
    Функция сбора значений новой сущности и добавление её в БД
    Автор Айрапетян Т.
    """
    global info4,info6,info8,info10,info12,dobavlenie,count,database,number
    value_model = info4.get()
    value_proizvodstvo = info6.get()
    value_kuzov = info8.get()
    if (value_kuzov=='седан'):
      value_kolvo_sidenyi=4
    if (value_kuzov=='кроссовер'):
      value_kolvo_sidenyi=5
    if (value_kuzov=='внедорожник'):
      value_kolvo_sidenyi=7
    value_color = info10.get()
    value_complectation = info12.get()
    if (value_complectation=='базовая'):
      value_dop_price=0
    if (value_complectation=='спорт'):
      value_dop_price=0.25
    if (value_complectation=='престиж'):
      value_dop_price=0.5
    if (value_complectation=='премиум'):
      value_dop_price=0.75
    if (value_complectation=='люкс'):
      value_dop_price=1
    data.append([number,value_model,value_proizvodstvo,value_kolvo_sidenyi,value_kuzov,value_color,value_complectation,value_dop_price])
    database.insert(parent='', index='end', iid=count,text="1",values=(number,value_model,value_proizvodstvo,value_kolvo_sidenyi,value_kuzov,value_color,value_complectation,value_dop_price))
    count +=1
    number+=1
    dobavlenie.destroy()


    
def knopka_udalenie():
    """
    Функция удаления выбранной мышкой сущности из БД
    Автор Айрапетян Т.
    """
    global database,number,count, data

    x=database.selection()[0]
    ind = find_data_index(int(x) + 1,data)
    data = data[:ind] + data[ind + 1:]
    database.delete(x)


def knopka_graf_otchet():
    """
    Функция создания окна с предложенными вариантами видов графических отчётов
    Автор Айрапетян Т.
    """
    global graf_otchet
    graf_otchet=Toplevel(tk)
    graf_otchet.title("Dream_car.База данных.Графический отчёт")
    graf_otchet.resizable(0, 0)
    canvas9=Canvas(graf_otchet, width=900,height=500,bg="#40E0D0")
    canvas9.pack() 
    frame_top11 = Frame(graf_otchet, bg='#40E0D0', bd=5)
    frame_top11.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top11, text='Столбчатая диаграмма',command=knopka_stolbchataya_diagramma,height = 10, width = 40,activebackground="#40E0D0")
    btn.pack()
    frame_top12 = Frame(graf_otchet, bg='#40E0D0', bd=5)
    frame_top12.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top12, text='Диаграмма рассеивания',command=knopka_diagramma_rasseivaniya,height = 10, width = 40,activebackground="#40E0D0")
    btn.pack()
    frame_top13 = Frame(graf_otchet, bg='#40E0D0', bd=5)
    frame_top13.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top13, text=' Диагрмамма Бокса-Вискера',command=knopka_diagramma_boksa,height =10, width = 40,activebackground="#40E0D0")
    btn.pack()
    frame_top14 = Frame(graf_otchet, bg='#40E0D0', bd=5)
    frame_top14.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top14, text='Гистограмма',command=knopka_gistogramma,height = 10, width = 40,activebackground="#40E0D0")
    btn.pack()
    
  


def knopka_text_otchet():
    """
    Функция создания окна с предложенными вариантами видов текстовых отчётов
    Автор Айрапетян Т.
    """
    global text_otchet
    text_otchet=Toplevel(tk)
    text_otchet.title("Dream_car.База данных.Текстовый отчёт")
    text_otchet.resizable(0, 0)
    canvas10=Canvas(text_otchet, width=900,height=500,bg="#40E0D0")
    canvas10.pack()
    frame_top221 = Frame(text_otchet, bg='#40E0D0', bd=5)
    frame_top221.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top221, text='Простой текстовый отчёт',command=knopka_prostoi_otchet,height = 10, width = 40,activebackground="#40E0D0")
    btn.pack()
    frame_top222 = Frame(text_otchet, bg='#40E0D0', bd=5)
    frame_top222.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.5)
    btn = Button(frame_top222, text='Статистический отчёт',command=knopka_static_otchet,height = 10, width = 40,activebackground="#40E0D0")
    btn.pack()
    
def knopka_sohranenie():
    """
    Функция сохранения БД с выбранными пользователем атрибутами
    Автор Айрапетян Т.
    """
    global galka_model_value,galka_proizvodstvo_value,galka_kolvo_sideniy_value,galka_kuzov_value,galka_color_value,galka_complectation_value,galka_dop_price_value
    global sohranenie
    galka_model_value=StringVar()
    galka_proizvodstvo_value=StringVar()
    galka_kolvo_sideniy_value=StringVar()
    galka_kuzov_value=StringVar()
    galka_color_value=StringVar()
    galka_complectation_value=StringVar()
    galka_dop_price_value=StringVar()
    galka_model_value.set('No')
    galka_proizvodstvo_value.set('No')
    galka_kolvo_sideniy_value.set('No')
    galka_kuzov_value.set('No')
    galka_color_value.set('No')
    galka_complectation_value.set('No')
    galka_dop_price_value.set('No')
    sohranenie=Toplevel(tk)
    sohranenie.title("Dream_car.База данных.Сохранение")
    sohranenie.resizable(0, 0)
    canvas10=Canvas(sohranenie, width=900,height=500,bg="#40E0D0")
    canvas10.pack()  
    frame_top20 = Frame(sohranenie, bg='#40E0D0', bd=5)
    frame_top20.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    info40 = Label(frame_top20, text='Выберите нужные атрибуты:', bg='#00FFFF', font=40)
    info40.pack()
    frame_top21 = Frame(sohranenie, bg='#40E0D0', bd=5)
    frame_top21.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.9)
    #создаём галочку
    galka_model=Checkbutton(frame_top21,text="Модель",variable=galka_model_value,offvalue='No', onvalue='Модель', bg='#40E0D0',height = 3, width = 20)
    galka_model.pack()
    galka_proizvodstvo=Checkbutton(frame_top21,text="Производство",variable=galka_proizvodstvo_value,offvalue='No', onvalue='Производство', bg='#40E0D0',height = 3, width = 20)
    galka_proizvodstvo.pack()
    galka_kolvo_sideniy=Checkbutton(frame_top21,text="Количество сидений",variable=galka_kolvo_sideniy_value,offvalue='No', onvalue='Количество сидений', bg='#40E0D0',height = 3, width = 20)
    galka_kolvo_sideniy.pack()
    galka_kuzov=Checkbutton(frame_top21,text="Кузов",variable=galka_kuzov_value,offvalue='No', onvalue='Кузов', bg='#40E0D0',height = 3, width = 20)
    galka_kuzov.pack()
    galka_color=Checkbutton(frame_top21,text="Цвет",variable=galka_color_value,offvalue='No', onvalue='Цвет', bg='#40E0D0',height = 3, width = 20)
    galka_color.pack()
    galka_complectation=Checkbutton(frame_top21,text="Комплектация",variable=galka_complectation_value,offvalue='No', onvalue='Комплектация', bg='#40E0D0',height = 3, width = 20)
    galka_complectation.pack()
    galka_dop_price=Checkbutton(frame_top21,text="Доп.цена",variable=galka_dop_price_value,offvalue='No', onvalue='Доп.цена', bg='#40E0D0',height = 3, width = 20)
    galka_dop_price.pack()
    btn113 = Button(frame_top21, text='ОК',command=sohranenie_ok,height = 2, width = 8,activebackground="#00CED1")
    btn113.pack()


def sohranenie_ok():
    """
    Функция создания БД, желаемой пользователем
    Автор Непомнящий А.
    """
    global sohranenie,galka_model_value,galka_proizvodstvo_value,galka_kolvo_sideniy_value,galka_kuzov_value,galka_color_value,galka_complectation_value,galka_dop_price_value
    value17=galka_model_value.get()
    value18=galka_proizvodstvo_value.get()
    value19=galka_kolvo_sideniy_value.get()
    value20=galka_kuzov_value.get()
    value21=galka_color_value.get()
    value22=galka_complectation_value.get()
    value23=galka_dop_price_value.get()
    
    columns = []
    if (value17=='Модель'):
      columns.append(1)  
    if (value18=='Производство'):
      columns.append(2)  
    if (value19=='Количество сидений'):
      columns.append(3)
    if (value20=='Кузов'):
      columns.append(4)  
    if (value21=='Цвет'):
      columns.append(5)
    if (value22=='Комплектация'):
      columns.append(6)
    if (value23=='Доп.цена'):
      columns.append(7) 
    
    
    
    fout = open("../Output/save.txt", "w")

    for record in data:
        for col in columns:
            print(record[col], end = " " if col != columns[-1] else "", file=fout)
        print(file=fout)
    fout.close()
   
    
    sohranenie.destroy()

    

def knopka_stolbchataya_diagramma():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления графического отчёта
    Автор Кочканьян А.
    """
    global graf_otchet,stolbchataya_diagramma,combo_1,combo_2
    stolbchataya_diagramma=Toplevel(tk)
    stolbchataya_diagramma.title("Dream_car.База данных.Графический отчёт.Столбчатая диаграмма")
    stolbchataya_diagramma.resizable(0, 0)
    canvas12=Canvas(stolbchataya_diagramma, width=900,height=500,bg="#40E0D0")
    canvas12.pack()
    frame_top001 = Frame(stolbchataya_diagramma, bg='#40E0D0', bd=5)
    frame_top001.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top001, text='Выберите отношение атрибутов:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top15 = Frame(stolbchataya_diagramma, bg='#40E0D0', bd=5)
    frame_top15.place(relx=0.2, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_1=ttk.Combobox(frame_top15,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_1.pack()
    frame_top16 = Frame(stolbchataya_diagramma, bg='#40E0D0', bd=5)
    frame_top16.place(relx=0.55, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_2=ttk.Combobox(frame_top16,values=("Количество сидений","Доп.цена"))
    combo_2.pack()
    frame_top119 = Frame(stolbchataya_diagramma, bg='#40E0D0', bd=5)
    frame_top119.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top119, text='OK',command=stolbchataya_diagramma_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    graf_otchet.destroy()
    
    
def stolbchataya_diagramma_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление графического отчёта
    Автор Кочканьян А.
    """
    global stolbchataya_diagramma,combo_1,combo_2   
    value1=combo_1.get()
    value2=combo_2.get()
    
    
    if (value1=='Модель'):
      m=1  
    if (value1=='Производство'):
      m=2  
    if (value1=='Кузов'):
      m=4  
    if (value1=='Цвет'):
      m=5
    if (value1=='Комплектация'):
      m=6
    if (value2=='Количество сидений'):
      n=3
    if (value2=='Доп.цена'):
      n=7  
      
  
    d = dict()
    counts = dict()
    for record in data:
        if record[m] in d:
            d[record[m]] += record[n]
            counts[record[m]] += 1
        else:
            d[record[m]] = record[n]
            counts[record[m]] = 1
    
    for key in d.keys():
        d[key] /= counts[key]

    plt.figure(figsize=(7, 7))
    plt.subplots_adjust(bottom=0.4)
    plt.bar(d.keys(), d.values())
    plt.xticks(rotation=90)
    plt.xlabel(value1)
    plt.ylabel(value2)
    plt.title("Среднее значение " + value2 + " по атрибуту " + value1)
    plt.savefig('../Graphics/image_stolbchataya.jpg')
    plt.show()
    
    stolbchataya_diagramma.destroy()
    

def knopka_diagramma_boksa():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления графического отчёта
    Автор Кочканьян А.
    """
    global graf_otchet,diagramma_boksa,combo_3,combo_4
    diagramma_boksa=Toplevel(tk)
    diagramma_boksa.title("Dream_car.База данных.Графический отчёт.Диаграмма Бокса-Вискера")
    diagramma_boksa.resizable(0, 0)
    canvas13=Canvas(diagramma_boksa, width=900,height=500,bg="#40E0D0")
    canvas13.pack()
    frame_top002 = Frame(diagramma_boksa, bg='#40E0D0', bd=5)
    frame_top002.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top002, text='Выберите отношение атрибутов:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top116 = Frame(diagramma_boksa, bg='#40E0D0', bd=5)
    frame_top116.place(relx=0.2, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_3=ttk.Combobox(frame_top116,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_3.pack()
    frame_top117 = Frame(diagramma_boksa, bg='#40E0D0', bd=5)
    frame_top117.place(relx=0.55, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_4=ttk.Combobox(frame_top117,values=("Количество сидений","Доп.цена"))
    combo_4.pack()
    frame_top120 = Frame(diagramma_boksa, bg='#40E0D0', bd=5)
    frame_top120.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top120, text='OK',command=diagramma_boksa_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    graf_otchet.destroy()
    
    
def diagramma_boksa_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление графического отчёта
    Автор Кочканьян А.
    """
    global diagramma_boksa,combo_3,combo_4
    value3=combo_3.get()
    value4=combo_4.get()
    
    if (value3=='Модель'):
      m=1  
    if (value3=='Производство'):
      m=2  
    if (value3=='Кузов'):
      m=4  
    if (value3=='Цвет'):
      m=5
    if (value3=='Комплектация'):
      m=6
    if (value4=='Количество сидений'):
      n=3
    if (value4=='Доп.цена'):
      n=7  
    

    d = dict()
    for record in data:
        if record[m] in d:
            d[record[m]].append(record[n])
        else:
            d[record[m]] = [record[n]]
        
    plt.figure(figsize=(7, 7))
    plt.subplots_adjust(bottom=0.4)
    plt.boxplot(d.values())
    plt.xticks(list(range(1, len(d.keys()) + 1)), d.keys(), rotation=90)
    plt.xlabel(value3)
    plt.ylabel(value4)
    plt.title(value4 + " по атрибуту " + value3)
    plt.savefig('../Graphics/image_boxa.jpg')
    plt.show()

    
    
    diagramma_boksa.destroy()    



def knopka_diagramma_rasseivaniya():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления графического отчёта
    Автор Кочканьян А.
    """
    global graf_otchet,diagramma_rasseivaniya,combo_5,combo_6,combo_7
    diagramma_rasseivaniya=Toplevel(tk)
    diagramma_rasseivaniya.title("Dream_car.База данных.Графический отчёт.Диаграмма рассеивания")
    diagramma_rasseivaniya.resizable(0, 0)
    canvas14=Canvas(diagramma_rasseivaniya, width=900,height=500,bg="#40E0D0")
    canvas14.pack()
    frame_top003 = Frame(diagramma_rasseivaniya, bg='#40E0D0', bd=5)
    frame_top003.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top003, text='Выберите отношение атрибутов:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top141 = Frame(diagramma_rasseivaniya, bg='#40E0D0', bd=5)
    frame_top141.place(relx=0, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_5=ttk.Combobox(frame_top141,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_5.pack()
    frame_top142 = Frame(diagramma_rasseivaniya, bg='#40E0D0', bd=5)
    frame_top142.place(relx=0.35, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_6=ttk.Combobox(frame_top142,values=("Количество сидений","Доп.цена"))
    combo_6.pack()
    frame_top143 = Frame(diagramma_rasseivaniya, bg='#40E0D0', bd=5)
    frame_top143.place(relx=0.7, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_7=ttk.Combobox(frame_top143,values=("Количество сидений","Доп.цена"))
    combo_7.pack()
    frame_top144 = Frame(diagramma_rasseivaniya, bg='#40E0D0', bd=5)
    frame_top144.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top144, text='OK',command=diagramma_rasseivaniya_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    graf_otchet.destroy()
    

def diagramma_rasseivaniya_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление графического отчёта
    Автор Кочканьян А.
    """
    global diagramma_rasseivaniya,combo_5,combo_6,combo_7
    value5=combo_5.get()
    value6=combo_6.get()
    value7=combo_7.get()
    
    if (value5=='Модель'):
      m=1  
    if (value5=='Производство'):
      m=2  
    if (value5=='Кузов'):
      m=4  
    if (value5=='Цвет'):
      m=5
    if (value5=='Комплектация'):
      m=6
    if (value6=='Количество сидений'):
      n=3
    if (value6=='Доп.цена'):
      n=7  
    if (value7=='Количество сидений'):
      k=3
    if (value7=='Доп.цена'):
      k=7   
    
    qual = []
    num1 = []
    num2 = []
    for record in data:
        qual.append(record[m])
        num1.append(record[n])
        num2.append(record[k])
    
    color_labels = np.unique(qual)
    rgb_values = sns.color_palette("Set1", len(color_labels))
    color_map = dict(zip(color_labels, rgb_values))

    area=49
    plt.scatter(num1, num2, s=area, c=list(map(lambda x: color_map[x], qual)))
    plt.xlabel(value6)
    plt.ylabel(value7)
    plt.title("Диаграмма рассеивания " + value5 + " по атрибутам: " + value6 + "," + value7)
    plt.savefig('../Graphics/image_rasseivaniya.jpg')
    plt.show()

    diagramma_rasseivaniya.destroy()


def knopka_gistogramma():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления графического отчёта
    Автор Кочканьян А.
    """
    global graf_otchet,gistogramma,combo_8,combo_9
    gistogramma=Toplevel(tk)
    gistogramma.title("Dream_car.База данных.Графический отчёт.Гистограмма")
    gistogramma.resizable(0, 0)
    canvas15=Canvas(gistogramma, width=900,height=500,bg="#40E0D0")
    canvas15.pack()
    frame_top004 = Frame(gistogramma, bg='#40E0D0', bd=5)
    frame_top004.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top004, text='Выберите отношение атрибутов:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top145 = Frame(gistogramma, bg='#40E0D0', bd=5)
    frame_top145.place(relx=0.2, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_8=ttk.Combobox(frame_top145,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_8.pack()
    frame_top146 = Frame(gistogramma, bg='#40E0D0', bd=5)
    frame_top146.place(relx=0.55, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_9=ttk.Combobox(frame_top146,values=("Количество сидений","Доп.цена"))
    combo_9.pack()
    frame_top147 = Frame(gistogramma, bg='#40E0D0', bd=5)
    frame_top147.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top147, text='OK', command=gistogramma_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    graf_otchet.destroy()


def gistogramma_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление графического отчёта
    Автор Кочканьян А.
    """
    global gistogramma,combo_8,combo_9
    value8=combo_8.get()
    value9=combo_9.get()
  
    if (value8=='Модель'):
      m=1  
    if (value8=='Производство'):
      m=2  
    if (value8=='Кузов'):
      m=4  
    if (value8=='Цвет'):
      m=5
    if (value8=='Комплектация'):
      m=6
    if (value9=='Количество сидений'):
      n=3
    if (value9=='Доп.цена'):
      n=7  
      
  
    d = dict()
    counts = dict()
    for record in data:
        if record[m] in d:
            d[record[m]] += record[n]
            counts[record[m]] += 1
        else:
            d[record[m]] = record[n]
            counts[record[m]] = 1
    
    for key in d.keys():
        d[key] /= counts[key]

    plt.figure(figsize=(7, 7))
    plt.subplots_adjust(bottom=0.4)
    plt.bar(d.keys(), d.values())
    plt.xticks(rotation=90)
    plt.xlabel(value8)
    plt.ylabel(value9)
    plt.title("Среднее значение " + value9 + " по атрибуту " + value8)
    plt.savefig('../Graphics/image_gistogramma.jpg')
    plt.show()
    

    gistogramma.destroy()


def knopka_prostoi_otchet():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления текстового отчёта
    Автор Непомнящий А.
    """
    global text_otchet,prostoi_otchet,combo_10,combo_11,combo_12
    prostoi_otchet=Toplevel(tk)
    prostoi_otchet.title("Dream_car.База данных.Текстовый отчёт.Простой текстовый отчёт")
    prostoi_otchet.resizable(0, 0)
    canvas20=Canvas(prostoi_otchet, width=900,height=500,bg="#40E0D0")
    canvas20.pack()
    frame_top005 = Frame(prostoi_otchet, bg='#40E0D0', bd=5)
    frame_top005.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top005, text='Выберите отношение атрибутов и метод агрегации:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top006 = Frame(prostoi_otchet, bg='#40E0D0', bd=5)
    frame_top006.place(relx=0, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_10=ttk.Combobox(frame_top006,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_10.pack()
    frame_top007 = Frame(prostoi_otchet, bg='#40E0D0', bd=5)
    frame_top007.place(relx=0.35, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_11=ttk.Combobox(frame_top007,values=("Количество сидений","Доп.цена"))
    combo_11.pack()
    frame_top008 = Frame(prostoi_otchet, bg='#40E0D0', bd=5)
    frame_top008.place(relx=0.7, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_12=ttk.Combobox(frame_top008,values=("Среднее арифметическое","Сумма"))
    combo_12.pack()
    frame_top009 = Frame(prostoi_otchet, bg='#40E0D0', bd=5)
    frame_top009.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top009, text='OK',command=prostoi_otchet_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    text_otchet.destroy()
    
def prostoi_otchet_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление текстового отчёта
    Автор Непомнящий А.
    """
    global prostoi_otchet,combo_10,combo_11,combo_12,value10,value11, data
    value10=combo_10.get()
    value11=combo_11.get()
    value12=combo_12.get()
    
    
    
    if (value10=='Модель'):
      m=1  
    if (value10=='Производство'):
      m=2  
    if (value10=='Кузов'):
      m=4  
    if (value10=='Цвет'):
      m=5
    if (value10=='Комплектация'):
      m=6
    if (value11=='Количество сидений'):
      n=3
    if (value11=='Доп.цена'):
      n=7  

    d = dict()
    for record in data:  
        if (record[m] in d):
            d[record[m]] += record[n]
        else:
            d[record[m]] = record[n]

    maxlen = 50
    fout = open("../Output/prostoi_otchet.txt", "w")
    print(value10, " " * (50 - len(value10)) + "|\t", value11, file=fout)
    print("-" * (54 + len(value10) + len(value11)), file=fout)
    res = 0
    counter = 0
    for key, value in d.items():
        print(key, " " * (50 - len(key)) + "|\t", value, file=fout)
        res += value
        counter += 1

    print("-" * (54 + len(value10) + len(value11)), file=fout)
    if (value12=='Сумма'):
        print("ALL", " " * 47 + "|\t", res, file=fout)
    if (value12=='Среднее арифметическое'):
        print("ALL", " " * 47 + "|\t", res / counter, file=fout)
    fout.close()
    
    prostoi_otchet.destroy()


def knopka_static_otchet():
    """
    Функция создания окна с предложенными вариантами атрибутов 
    для составления текстового отчёта
    Автор Непомнящий А.
    """
    global text_otchet,static_otchet,combo_13,combo_14,combo_15,combo_16
    static_otchet=Toplevel(tk)
    static_otchet.title("Dream_car.База данных.Текстовый отчёт.Статистический отчёт")
    static_otchet.resizable(0, 0)
    canvas21=Canvas(static_otchet, width=900,height=500,bg="#40E0D0")
    canvas21.pack()
    frame_top010 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top010.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
    strocka = Label(frame_top010, text='Выберите отношение атрибутов и метод агрегации:', bg='#40E0D0', font=40)
    strocka.pack()
    frame_top011 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top011.place(relx=0.13, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_13=ttk.Combobox(frame_top011,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_13.pack()
    frame_top012 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top012.place(relx=0.48, rely=0.27, relwidth=0.35, relheight=0.17)
    combo_14=ttk.Combobox(frame_top012,values=("Количество сидений","Доп.цена"))
    combo_14.pack()
    frame_top013 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top013.place(relx=0.13, rely=0.57, relwidth=0.35, relheight=0.17)
    combo_15=ttk.Combobox(frame_top013,values=("Модель","Производство","Кузов","Цвет","Комплектация"))
    combo_15.pack()
    frame_top014 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top014.place(relx=0.48, rely=0.57, relwidth=0.35, relheight=0.17)
    combo_16=ttk.Combobox(frame_top014,values=("Среднее арифметическое","Сумма"))
    combo_16.pack() 
    frame_top015 = Frame(static_otchet, bg='#40E0D0', bd=5)
    frame_top015.place(relx=0.8, rely=0.87, relwidth=0.20, relheight=0.13)
    btn = Button(frame_top015, text='OK',command=static_otchet_ok,height = 20, width = 70,activebackground="#40E0D0")
    btn.pack()
    text_otchet.destroy()

def static_otchet_ok():
    """
    Функция сбора информации из выпадающих списков и
    составление текстового отчёта
    Автор Непомнящий А.
    """
    global static_otchet,combo_13,combo_14,combo_15,combo_16,data,database
    value13=combo_13.get()
    value14=combo_14.get()
    value15=combo_15.get()
    value16=combo_16.get()
    if (value13=='Модель'):
      m=1  
    if (value13=='Производство'):
      m=2  
    if (value13=='Кузов'):
      m=4  
    if (value13=='Цвет'):
      m=5
    if (value13=='Комплектация'):
      m=6
    if (value15=='Модель'):
      k=1  
    if (value15=='Производство'):
      k=2  
    if (value15=='Кузов'):
      k=4  
    if (value15=='Цвет'):
      k=5
    if (value15=='Комплектация'):
      k=6  
    if (value14=='Количество сидений'):
      n=3
    if (value14=='Доп.цена'):
      n=7  
    
    print(m,n,k)

    d = dict()
    for record in data:  
        if ((record[m],record[k]) in d):
            d[(record[m],record[k])] += record[n]
        else:
            d[(record[m],record[k])] = record[n]

    maxlen = 50
    fout = open("../Output/stat_otchet.txt", "w")
    print((value13,value15), " " * (50 - len(value13+value15)) + "|\t", value14, file=fout)
    print("-" * (54 + len(value13+value15) + len(value14)), file=fout)
    res = 0
    counter = 0
    for key, value in d.items():
        print(key, " " * (50 - len(key)) + "|\t", value, file=fout)
        res += value
        counter += 1

    print("-" * (54 + len(value13+value15) + len(value14)), file=fout)
    if (value16=='Сумма'):
        print("ALL", " " * 47 + "|\t", res, file=fout)
    if (value16=='Среднее арифметическое'):
        print("ALL", " " * 47 + "|\t", res / counter, file=fout)
    fout.close()
 
    static_otchet.destroy()



tk = Tk()
tk.title("Dream_car")
#спрашивать о желании закрыть приложение
tk.protocol("WM_DELETE_WINDOW", on_closing)
#сделаем фиксированную область
tk.resizable(0, 0)
#создаём canvas, на котором будем размещать объекты
canvas = Canvas(tk, width=900, height=500, bg="#ffb53d", highlightthickness=0)
canvas.pack()

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(tk, bg='#ffb53d', bd=10)
# создаём в этои frame кнопку с определённой командой
btn = Button(frame_top, text='База Данных',command=knopka_baza_dannyh,height = 20, width = 70,activebackground="#ffb700")
btn.pack()
# Также указываем его расположение
frame_top.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.15)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(tk, bg='#ffb53d', bd=10)
frame_bottom.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.15)
btn = Button(frame_bottom, text='Используемые справочники',command=knopka_spravochnicki,height = 20, width = 70,activebackground="#ffb700")
btn.pack()

#ввод созданной БД из справочников
global number
number=151
path=os.getcwd()
os.chdir(os.path.abspath(os.path.join(path, '..')))
os.chdir(os.path.join(path, 'Data'))

fin = open("data.txt", "r", encoding='utf8')
data = []
for line in fin.readlines():
    data.append(eval(line))
fin.close()


# Запускаем постоянный цикл, чтобы программа работала
tk.mainloop()