import random

list_of_num = [1,2,3,4,5,6,7,8,9]
list_of_Sletters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_of_Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_of_sym = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',':',';','<','>','.','?','/']
all_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',':',';','<','>','.','?','/']

def password_generator():
    total_length = int(input("Enter the total length of the password: "))
    no_of_Cletters = int(input("Enter the no of Capital letter: "))
    no_of_Sletters = int(input("Enter no of Small letters:"))
    no_of_sym = int(input("Enter the no of symbols: "))

    Cletters = []
    Sletters = []
    sym = []

    if no_of_Cletters+no_of_Sletters+no_of_sym > total_length:
        print("Requested character exceeded!!")
        return 0
    
    for i in range(no_of_Cletters):
        Cletters.append(random.choice(list_of_Cletters))
    
    for j in range(no_of_Sletters):
        Sletters.append(random.choice(list_of_Sletters))

    for k in range(no_of_sym):
        sym.append(random.choice(list_of_sym))

    if total_length - (no_of_Cletters+no_of_Sletters+no_of_sym) != 0:
        left_out = total_length - (no_of_Cletters+no_of_Sletters+no_of_sym)
        for l in range(left_out):
            sym.append(random.choice(all_list))

    password = Cletters+Sletters+sym
    random.shuffle(password)
    print(''.join(password))

password_generator()

