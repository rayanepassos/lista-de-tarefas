def lista_tarefas():
    tarefas = []

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Mostrar lista de tarefas")
        print("4. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            tarefa = input("\nDigite uma tarefa: ")
            tarefas.append({"tarefa": tarefa, "concluida": False})
        elif escolha == '2':
            if not tarefas:
                print("Nenhuma tarefa para marcar como concluída.")
                continue
            
            for i, tarefa in enumerate(tarefas):
                status = "Concluída" if tarefa["concluida"] else "Não concluída"
                print(f"{i + 1}. {tarefa['tarefa']} - {status}")
            
            tarefa_num = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            
            if 0 <= tarefa_num < len(tarefas):
                tarefas[tarefa_num]["concluida"] = True
                print(f"Tarefa '{tarefas[tarefa_num]['tarefa']}' marcada como concluída.")
            else:
                print("Número de tarefa inválido.")
        elif escolha == '3':
            if not tarefas:
                print("Nenhuma tarefa na lista.")
            else:
                print("\nLista de Tarefas:")
                for tarefa in tarefas:
                    status = "Concluída" if tarefa["concluida"] else "Não concluída"
                    print(f"- {tarefa['tarefa']} ({status})")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

lista_tarefas()
