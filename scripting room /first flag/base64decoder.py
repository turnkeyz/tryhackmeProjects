import base64

def encoder():
    message = "stuff"
    msg_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    base64_message = base64_bytes.decode('ascii')
    print('\n',base64_message)


def decoder(amount):
    file = open('b64.txt', 'r').read()
    #print(file,'\n')
    #stuff = 'c3R1ZmY='
    i = 0
    for i in range(amount):
        print(i)
        file = base64.b64decode(file)
    print(file)
#   base64_message = 'ZW5jb2RpbmcgaXMgcHl0aG9uIGlzIGVhc3kh'  
#   base64_bytes = base64_message.encode('ascii')
#   msg_bytes = base64.b64decode(base64_bytes)
#   decoded_message = msg_bytes.decode('ascii')
#   print('\n', decoded_message)



if __name__ == '__main__':
    decoder(int(input()))
