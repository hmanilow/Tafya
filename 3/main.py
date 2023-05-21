def func(el, f):
    if el == 'a' and f ==0:
        f = 1
    elif el == 'a' and f == 1:
        f = 0
    return f 

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
            else:
                        g = '(четное)'
                    r="Состояние q" + str(i) + " = "+ str(fl[i]) + g
                    print(r, "по символу", n[i])
                print("да")
            else:
                print("нет")
        else:
            print("невозможная цепочка")
