while True:

    n = input("Введите строку: ")
    mas = []
    fl = []
    if len(n) == 0:
        print("нет")
    else:
        if n.count('a')+n.count('b') == len(n):
            flag = 0
            s =''
            r = ''
            for i in n:
                s += i
                flag = func(i, flag)
                mas.append(s)
                fl.append(flag)
            if flag == 0:
                for i in range(len(mas)):
                    if fl[i] == 1:
                        g = '(нечетное)'
