import random_answer

name = input('Привет, Как тебя зовут?\n')
print(f'Здравствуй, {name}!')

flag = True
while flag:
    quest = input("Какой у тебя вопрос ко мне?\n")
    print(random_answer.random_answer())
    while True:
        answ = input('Хочешь задать еще один вопрос (да/нет)?\n')
        if answ.lower() == "да" or answ.lower() == "lf":
            break
        elif answ.lower() == "нет" or answ.lower() == "ytn":
            flag = False
            break
        else:
            continue
print(f'До свидания, {name}.\nВозвращайся, когда возникнут новые вопросы!')