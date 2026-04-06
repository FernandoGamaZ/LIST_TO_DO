import proc

while True:
    opcao = int(input("Digite a opção desejada: \n1 - Adicionar tarefa \n2 - Listar tarefa \n3 - Concluir tarefa \n4 - Encerrar programa: "))
    match opcao:
        case 1:
            proc.adicionar_tarefa()
        case 2:
            proc.listar_tarefas()
        case 3:
            proc.tarefa_concluida()
        case 4:
            print("Programa encerrado.")
            break