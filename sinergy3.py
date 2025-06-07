# задание 1
number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
else:
    if number > 0:
      sign = "положительное"
    else:
      sign = "отрицательное"
    if number % 2 == 0:
      parity = "четное"
      print(sign, parity, "число")
    else:
      parity = "нечетное"
      print(sign, parity, "число")
      print("число не является четным")     
      

# задание 2 

word = input("Введите слово из маленьких латинских букв: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonant_count = 0

for letter in word:
  if letter in vowels:
    vowel_counts[letter] += 1
  else:
    consonant_count += 1

print(f"Согласных букв: {consonant_count}")
print(f"Гласных букв: {sum(vowel_counts.values())}")

for vowel in ['a', 'e', 'i', 'o', 'u']:
  if vowel_counts[vowel] == 0:
    print(f"{vowel}: False")
  else:
    print(f"{vowel}: {vowel_counts[vowel]}")


# задание 3 

X = int(input("Введите минимальную сумму инвестиций X: "))
A = int(input("Сколько долларов у Майкла? "))
B = int(input("Сколько долларов у Ивана? "))

if A >= X and B >= X:
  print(2)
elif A >= X:
  print("Mike")
elif B >= X:
  print("Ivan")
elif A + B >= X:
  print(1)
else:
  print(0)










