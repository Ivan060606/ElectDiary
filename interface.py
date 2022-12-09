import in_data, log

def button_click():
    dt = ''
    flag = 1
    
    while flag == 1:
        while flag == 1:
            print('Введите "1" чтобы записать(учитель) или "0" чтобы прочитать(ученик)')
            flag = int(input())
            while flag == 1:
                dt = dt + log.AddStudent(in_data.indata(),dt)
                print('Введите "1" чтобы продолжить или "0" чтобы завершить')
                flag = int(input())
            print('Завершили ввод.')
            print('Введите "1" чтобы продолжить или "0" чтобы прочитать(ученик)')
            flag = int(input())
        log.reader(dt)
        print('Введите "1" чтобы продолжить или "0" чтобы закончить')
        flag = int(input())