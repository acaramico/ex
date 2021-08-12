import psutil
x = psutil.cpu_times()
i = 1
i2 = 1
r = 'Resposta Inválida'

resposta = str(input('Pergunta 1. Mostar a porcentagem de uso separado entre todas as CPUs?(Responda Sim ou Não)\n'))
if resposta == 'Sim' or resposta == 'sim':
    z = True
elif resposta == 'Não' or resposta == 'não' or resposta == 'nao' or resposta == 'Nao':
        
    z = False
else:
    print(r)
    

intervalo = float(input('Informe o intervalo de segundos de captação:\n'))
quantidadeDada = float(input('Informe a quantidade de vezes de captação:\n'))
print('\nUtilização atual da CPU de todo o sistema em porcentagem:')
while i <= quantidadeDada:
    
    print(psutil.cpu_percent(interval=intervalo, percpu=z))
    
    i = i+1


resposta2 = str(input('Pergunta 2. Mostrar a quantidade de CPUs lógicas ou físicas? (Responda Lógicas ou Físicas)\n'))
if resposta2 == 'Lógicas' or resposta2== 'lógicas' or resposta2== 'Logicas' or resposta2 =='logicas':
    t = True
elif resposta2 == 'Físicas'  or resposta2== 'físicas' or resposta2== 'Fisicas'  or resposta2== 'fisicas':
    t= False
else:
    print(r)
    
print('Quantidade de CPUS',resposta2,':' ,psutil.cpu_count(logical=t))

resposta3 = int(input('Pergunta 3. Quantas vezes solicita ver os segundos que a CPU gastou em cada modo?\n'))

while i2 <= resposta3:
    print(psutil.cpu_times())
    i2 = i2+1
