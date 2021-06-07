message = input("Message: ")

message = message.encode("ASCII")

message = zip([i//16 for i in message],[i%16 for i in message])

message = [j for i in message for j in i]

message = ' '.join([''.join([k if bool(int(l)) else j for j,k,l in zip("bowl","BOWL",bin(i)[2:].rjust(4, '0'))]) for i in message])

print(message)
