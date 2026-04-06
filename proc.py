tarefa= []

def adicionar_tarefa():
    while True:
        tarefa.append(input("Digite a tarefa: "))
        if tarefa[-1] == "sair":
            break


def listar_tarefas():
    len(tarefa)
    print("Tarefas:", tarefa)

def tarefa_concluida():
    len(tarefa)
    decisao = input("Digite a tarefa concluída: ")
    if decisao in tarefa:
        tarefa.remove(decisao)
    else:
        print(f"A tarefa {decisao} não existe.")
    

    