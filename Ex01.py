# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#  Пример:
#  2+2 => 4;
#  1+2*3 => 7;
#  1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1+2*3 => 7;
#  (1+2)*3 => 9;

formula = '24+5/2*3+30'
lst = []
numbers = ''

def Action(array,sign):
    i=0
    while sign in array:
       if array[i] == sign:
            if sign == '*':
                a = float(array[i-1])*float(array[i+1])
            elif sign == '/':
                a = float(array[i-1])/float(array[i+1])
            elif sign == '-':
                a = float(array[i-1])-float(array[i+1])
            elif sign == '+':
                a = float(array[i-1])+float(array[i+1])

            array[i-1] = a
            array.pop(i+1)
            array.pop(i)
            return(array)
       else:
            i += 1
    
for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '/' in lst or '*' in lst:
    if lst[i] == '/':
        Action(lst,'/')
        i = 0
    elif lst[i] == '*':
        Action(lst,'*')
        i = 0
    else:
        i+=1

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        Action(lst,'-')
        i = 0
    elif lst[i] == '+':
        Action(lst,'+')
        i = 0
    else:
        i+=1
print(lst)