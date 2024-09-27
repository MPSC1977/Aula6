import os

os.system('cls')

lst_previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']

for e in lst_previsoes:
    if e == 'Ensolarado':
        print(f'A previsão para hoje é de tempo {e}: Aproveite e passeie!')
    else:
        print(f'A previsão para hoje é de tempo {e}: Não esqueça o guarda-chuva!')