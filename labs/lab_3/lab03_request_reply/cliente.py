import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")


def enviar(pedido):
    socket.send_string(pedido)
    return socket.recv_string()


def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        tarefa = input("Descricao da tarefa: ")
        resposta = enviar(f"ADICIONAR|{tarefa}")
        print(resposta.split("|", 1)[1])

    elif opcao == "2":
        indice = input("Numero da tarefa a remover: ")
        if indice.isdigit():
            resposta = enviar(f"REMOVER|{indice}")
            print(resposta.split("|", 1)[1])
        else:
            print("Numero invalido.")

    elif opcao == "3":
        resposta = enviar("LISTAR")
        lista = resposta.split("|", 1)[1]
        tarefas = lista.split(";") if lista else []
        if tarefas:
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")
        else:
            print("Nenhuma tarefa cadastrada.")

    elif opcao == "4":
        print("Encerrando cliente.")
        break

    else:
        print("Opcao invalida.")
