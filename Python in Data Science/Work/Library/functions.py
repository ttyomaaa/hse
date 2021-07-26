def find_data_index(number,data):
    """
    Функция нахождения конкретной сущности из БД для дальнейшего редактирования
    Автор Айрапетян Т.
    """
    for i in range(len(data)):
        if data[i][0] == int(number):
            return i
    return -1


def convert_to_data_record(m1, m2, m3, m4, m5, m6, m7, m8):
    """
    Функция сохранения изменённой сущности БД
    Автор Айрапетян Т.
    """
    number = int(m1.get())
    model = m2.get()
    made_by = m3.get()
    seats = int(m4.get())
    body = m5.get()
    color = m6.get()
    complectation = m7.get()
    extra_price = float(m8.get())
    return [number, model, made_by, seats, body, color, complectation, extra_price]

