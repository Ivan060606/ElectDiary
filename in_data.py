def indata():
    fam = str("Фамилия: " + input('Введите фамилию: '))
    name = str("Имя: " + input('Введите имя: '))
    clas = str("Класс: " + input('Введите класс: '))
    educate  = str("Предмет: " + input('Введите предмет: '))
    grade = str("Оценка: " + input('Введите оценку: '))
    id = (fam, name, clas, educate, grade)
    return id

##def view_data(data):
##    print(f'result={data}')

##print(indata())