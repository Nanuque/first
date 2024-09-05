
import time
def typewriter(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
text_to_type = ("Вітаю тебе, Обраний! \nЯк мені називати тебе? ")
typewriter(text_to_type)

green_text = "\033[92m"
reset_color = "\033[0m"
text = input()
print(f"{green_text}{text}{reset_color}")

import time
def typewriter(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
text_to_type = ("... Судячи з кольору Ти новенький у IT! \nОбери мову програмування яку Ти хотів би опанувати: ")
typewriter(text_to_type)


red_text = "\033[91m"
reset_color = "\033[0m"
text = "Ruby"
print(f"{red_text}{text}{reset_color}")

yellow_text = "\033[93m"
reset_color = "\033[0m"
text = "Javascript!"
print(f"{yellow_text}{text}{reset_color}")

green_text = "\033[92m"
reset_color = "\033[0m"
text = "PHP"
print(f"{green_text}{text}{reset_color}")

blue_text = "\033[94m"
reset_color = "\033[0m"
text = "Python"
print(f"{blue_text}{text}{reset_color}")

purple_text = "\033[95m"
reset_color = "\033[0m"
text = "C#"
print(f"{purple_text}{text}{reset_color}")

import time
import sys

def typewriter(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

max_attempts = 3
attempts = 0

languages = ["ruby", "javascript", "php", "python", "c#"]

while attempts < max_attempts:
    
    user_input = input().lower()

    if user_input in languages:
        link = "https://edu.cbsystematics.com/ua"
        text_to_type = f"Чудовий вибір! Скоріше переходь за посиланням: {link} !"
        typewriter(text_to_type)
        sys.exit()  
    else:
        if attempts == 0:
            error_text = "Це точно мова програмування? Чи це твій кіт пройшовся по клавіатурі? Спробуй ще раз!"
            typewriter(error_text)
        elif attempts == 1:
            error_text = "Навіть коти знають як друкувати на клавіатурі! Спробуй ще раз!"
            typewriter(error_text)
        
        attempts += 1  
        
        if attempts == max_attempts:
            end_text = "На жаль Ви використали всі спроби але не сумуйте, Ви ще можете записатись на курси CyberBionic Systematics! \nА наша програма закінчує свою роботу та прощається з Вами =)."
            typewriter(end_text)
            sys.exit() 