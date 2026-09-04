import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

todos = []

# 1 -> adicionar
# 2 -> listar
# 3 - remover
while True:
    message = socket.recv()
    print(f"Mensagem recebida: {message}", flush=True)
    print(type(message.decode("utf-8")))
    for c in message.decode('utf 8'):
        print(c)
    socket.send_string("World")

