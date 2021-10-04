times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacinal', 'Fluminense', 'Atlético-PR', 'Atlético-GO', 'Cuiabá', 'Ceará SC', 'São Paulo', 'América-MG', 'Juventude', 'Santos', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 5 últimos colocados são: {times[15:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense está na posição {times.index("Chapecoense")+1}')
