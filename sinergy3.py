# Задание 1
# Тут как в задании написано будет выводить только "отрицательное четное число",
#  "нулевое число", "положительное нечетное число"
a = int(input("Введите целое число"))
if a < 0:
  if a % 2 == 0:
    print("отрицательное четное число")
elif a > 0:
  if a % 2 != 0:
    print("положительное нечетное число")
elif a == 0:
  print("нулевое число")

# Второй вариант выполнения задания, в котором будут определяться все варианты ввода чисел 
number = int(input("Введите целое число"))

if number == 0:
  print("нулевое число")
elif number > 0:
  if number % 2 == 0:
    print("положительное четное число")
  else:
    print("положительное нечетное число") 
elif number < 0: 
  if number % 2 == 0:
    print("отрицательное четное число")
  else:
    print("отрицательное нечетное число")   
   

#Задание 2






   
#Задание 3

x = int(input("Минимальная сумма инвестиций:"))
a = int (input("инвестиции Майкла:"))
b = int(input("инвестиции Ивана:"))  


if a >= x and b >= x:
  print(2)
elif a >= x:
  print("mike")
elif b >= x:
  print("ivan")
elif a + b == x:
  print(1)
else:
  print(0)  




























