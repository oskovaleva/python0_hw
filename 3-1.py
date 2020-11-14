# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “=”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “>”.
# Если компьютер назвал число больше, игрок должен выбрать “<”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

num_range = [1, 100]

input('Choose a number from 1 to 100. I will guess it in 7 tries or less! Press "Enter" when you are ready. ')
try_count = 0
user_answer = None

while user_answer != '=':
    try_count += 1
    guess_num = int(sum(num_range) / 2)
    if num_range[0] == num_range[1]:
        print(f"Your number is {guess_num}!")
        user_answer = '='
    else:
        user_answer = None
        while user_answer not in ('=', '>', '<'):
            user_answer = input(f"This is try #{try_count}. Is {guess_num} your number? "
                                f"(input '=' for yes, '>' if it's too low, '<' if it's too high) >>> ")
        if user_answer == '>':
            num_range[0] = guess_num + 1
        elif user_answer == '<':
            num_range[1] = guess_num - 1
        if num_range[1] < num_range[0]:
            print("You're lying! Game over.")
            break
else:
    print(f"Told you I'd guess it in 7 tries or less! (I used {try_count} tries.)")
