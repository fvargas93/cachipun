import random

print('#'*27)
print('¡Bienvenido al Cachipún! 😎')
print('#'*27)
username = input('\nIngresa tu nombre de usuario: ')

result = {'piedra': {'tijera':1,'papel':0},
            'papel':  {'piedra':1,'tijera':0},
            'tijera': {'papel':1,'piedra':0}
            }

while len(username) < 3:
    username = input('El nombre de usuario debe tener al menos 3 carácteres: ')
    
attempts = int(input('\n¿Cuantos intentos quieres jugar?: '))

def choose_option():
    user_option = str(input('\nEscribe piedra, papel o tijera: ')).lower()
    computer_options = ['piedra','papel','tijera']
    while user_option not in ['piedra','papel','tijera']:
        user_option = str(input('Opción inválida, debes escribir piedra, papel o tijera: ')).lower()
    computer_option = random.choice(computer_options)
    return user_option,computer_option
    
def check_rules(user_option,computer_option):
    message = ''
    user_win = 0
    computer_win = 0
    if user_option == computer_option:
        message = f'\n{username} ha elegido {user_option} y el computador {computer_option}, ¡Hay un empate! 😱'
    else:
        user_result = result[user_option][computer_option]
        computer_result = result[computer_option][user_option]
        if user_result > computer_result:
            message = f'\n{username} ha elegido {user_option} y el computador {computer_option}, ¡Punto para {username}! 🧑🏻'
            user_win = 1
        else:
            message = f'\n{username} ha elegido {user_option} y el computador {computer_option}, ¡Punto para el computador! 🤖'
            computer_win = 1
    return message,user_win,computer_win

def check_winner(user_wins,computer_wins,attemps):
    message = ''
    if user_wins == attemps:
        message = f'¡El ganador del juego es {username}! 🧑🏻🎖️'
    elif computer_wins == attemps:
        message = f'¡El ganador del juego es el computador! 🤖🎖️'
    return message

def run_game():
    user_wins = 0
    computer_wins = 0
    pass

user_option,computer_option = choose_option()
print(user_option,computer_option)
print(check_rules(user_option,computer_option))