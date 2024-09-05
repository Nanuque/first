import random
import pyjokes
from termcolor import colored
from tqdm import tqdm
import time
import emoji

# 1. Функція для рекомендації фільмів
def recommend_movie():
    movies = ['Inception', 'The Matrix', 'Interstellar', 'The Godfather', 'Pulp Fiction']
    print(f"Рекомендуємо подивитися: {random.choice(movies)}")

# 2. Функція для рекомендації музики
def recommend_music():
    genres = ['Rock', 'Pop', 'Classical', 'Jazz', 'Hip-Hop']
    print(f"Спробуйте музику в жанрі: {random.choice(genres)}")

# 3. Функція для анекдотів
def tell_joke():
    joke = pyjokes.get_joke()
    print(colored(f"Ось анекдот: {joke}", 'cyan'))

# 4. Гра "Камінь-ножиці-папір"
def rock_paper_scissors():
    choices = ['камінь', 'ножиці', 'папір']
    user_choice = input("Обери: камінь, ножиці або папір: ").lower()
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        print(colored(f"Нічия! Бот вибрав {bot_choice}", 'yellow'))
    elif (user_choice == 'камінь' and bot_choice == 'ножиці') or \
         (user_choice == 'ножиці' and bot_choice == 'папір') or \
         (user_choice == 'папір' and bot_choice == 'камінь'):
        print(colored(f"Ти виграв! Бот вибрав {bot_choice}", 'green'))
    else:
        print(colored(f"Ти програв! Бот вибрав {bot_choice}", 'red'))

# 5. Функція меню
def menu():
    print(emoji.emojize("""
    Привіт! Я твій розважальний чат-бот! Обери опцію:
    1. Рекомендувати фільм
    2. Рекомендувати музику
    3. Розказати анекдот
    4. Пограти в "Камінь-ножиці-папір"
    5. Вийти
    """))
    
    choice = input("Введіть номер опції: ")
    return choice

# 6. Основний цикл програми
def run_bot():
    while True:
        choice = menu()
        if choice == '1':
            recommend_movie()
        elif choice == '2':
            recommend_music()
        elif choice == '3':
            tell_joke()
        elif choice == '4':
            rock_paper_scissors()
        elif choice == '5':
            print(colored("До зустрічі!", 'blue'))
            break
        else:
            print(colored("Неправильний вибір. Спробуйте знову.", 'red'))

if __name__ == "__main__":
    run_bot()