import socket
import threading
import json

bind_ip = "192.168.0.152"
bind_port = 8080

print("\nStarted...\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print("[+] Listening on {0} : {1}".format(bind_ip,bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("\n[+] Client: {0}\n".format(request))

    message = ['Mistrz pythona,',b'\n',"BBP"]
    json_string = json.dumps(message[0])
    client_socket.send(json_string.encode())
    client_socket.send(message[1])
    json_string = json.dumps(message[2])
    client_socket.send(json_string.encode())


    print("\ni sent {0}\n".format(json_string.encode()))
    client_socket.close()

while True:
    client,addr = server.accept()
    print("\n[+] Accepting connection from {0} _ {1}\n".format(addr[0],addr[1]))
    print("\n[+] Establishing a connection from {0} _ {1}\n".format(addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

print("\nFinished...\n")

