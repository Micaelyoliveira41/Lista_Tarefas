# LISTA DE TAREFAS DO DIA

tarefas = []

while True: 
    add_tarefa = input('Digite as tarefa: ')
    print(f'tarefa adicionada')

    if add_tarefa:
        tarefas.append(add_tarefa)
    else:
      break
for tarefa in tarefas:
   print(tarefa)

