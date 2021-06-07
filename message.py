bowl = input("Bowl: ")

bowl = bowl.replace(' ', '')

length = len(bowl)//8

bowl = [i.isupper() for i in bowl]

bowl = sum([b*2**i for i, b in enumerate(bowl[::-1])])

bowl = bowl.to_bytes(length, 'big').decode("ASCII")

print(bowl)
