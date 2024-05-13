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
    username = input('El nombre de usuario debe tener al menos 3 carácteres ')
    
attempts = int(input('\n¿Cuantos intentos quieres jugar?: '))

def choose_option():
    user_option = str(input('\nEscribe piedra, papel o tijera: ')).lower()
    computer_options = ['piedra','papel','tijera']
    while user_option not in ['piedra','papel','tijera']:
        user_option = str(input('Opción inválida, debes escribir piedra, papel o tijera para inciar el juego: ')).lower()
    computer_option = random.choice(computer_options)
    return user_option,computer_option
    
def check_rules():
    pass

def check_winner():
    pass

def run_game():
    pass
