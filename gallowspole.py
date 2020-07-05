# Реализация игры "Виселица" на Питоне
# https://github.com/PoorMouse/GallowsPole

from random import randint

# Макет виселицы
gallowsPole = ("|", "|\\", "|\n|\\", "___\n|\n|\\", "___\n| \uc6c3\n|\\")

# Формируем алфавит
abcLowBorder = ord('А')
abcHighBorder = ord('А') + 32
alphabet = [chr(i) for i in range(abcLowBorder, abcHighBorder)]

# Задаем список и выбираем из него слово
words = ["крокодил", "редакция", "семья", "инструмент", "эксплуатация", "производитель", "обстоятельство", "телевидение", "животное", "соглашение"]
chosenWord = words[randint(0, len(words) - 1)]
wordLength = len(chosenWord)

# Прочее (паттерн выбранного слова, перечень использованных букв, счетчики)
pattern = ["_" for i in range(wordLength)]
usedLetters = []
counter = 0
errors = 0

while True:
    print(" ".join(alphabet))
    print(" ".join(pattern).capitalize())
    letter = input("Введите букву: ").lower()
    print()

    # Прверяем введенную букву на принадлженость русскому алфавиту
    if ord(letter.upper()) < abcLowBorder or ord(letter.upper()) > abcHighBorder:
        print("Допустимо использовать только буквы русского алфавита.\n")
        continue

    # Смотрим, использовалась ли буква ранее, чтобы избежать повторного ввода
    if letter not in usedLetters:
        usedLetters.append(letter)
        alphabet.remove(letter.upper())
    else:
        print("Такая буква уже называлась.\n")
        continue

    # Считаем количество ошибок и рисуем виселицу
    if letter not in chosenWord:
        print(gallowsPole[errors])
        errors += 1
        if errors == len(gallowsPole):
            print("Вы проиграли.")
            print(f"Загаданное слово: {chosenWord}.")
            break
        continue

    # Ищем позицию угаданной буквы и открываем ее
    for i in range(wordLength):
        if chosenWord[i] == letter:
            pattern[i] = letter
            counter += 1

    # Победа?
    if counter == wordLength:
        print(" ".join(pattern).capitalize())
        print("Вы выиграли!")
        break
