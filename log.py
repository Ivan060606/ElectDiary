def AddStudent(id,data):
    fam, name, clas, educate, grade = id
    k = data.find(fam)
    if k == -1:
        data = ''
        rasparse = ", ".join(map(str, (id)))
        rasparse = rasparse + ";\n"
        data += rasparse
        print('Добавлен ученик и оценка')
        
    else:
        e = data.find('Фами',k)
        r = data.find(educate, k, e)
        if r == -1:
            p = 9 + data.find('Предмет',k)
            print(data[:p])
            data = data[:p] + educate[8:] + grade[7:] + data[p:]
        #else:
    return data



def reader(dt):
    srch = str(input('Введите Вашу фамилию: '))
    index = dt.find(srch) - 8
    print(dt[index:])
    print(index)