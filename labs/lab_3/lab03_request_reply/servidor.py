import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

# armazenamento das tarefas em memoria, usando uma lista simples
tarefas = []

print("Servidor pronto para receber pedidos.", flush=True)

while True:
    pedido = socket.recv_string()
    partes = pedido.split("|")
    acao = partes[0]

    if acao == "ADICIONAR":
        descricao = partes[1]
        tarefas.append(descricao)
        resposta = "OK|Tarefa adicionada."

    elif acao == "REMOVER":
        indice = partes[1]
        if indice.isdigit() and int(indice) < len(tarefas):
            removida = tarefas.pop(int(indice))
            resposta = f"OK|Tarefa removida: {removida}"
        else:
            resposta = "ERRO|Indice invalido."

    elif acao == "LISTAR":
        resposta = "LISTA|" + ";".join(tarefas)

    else:
        resposta = "ERRO|Acao desconhecida."

    print(f"Pedido: {pedido} -> Resposta: {resposta}", flush=True)
    socket.send_string(resposta)
