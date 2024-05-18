import Categories

def login():
    Owner= ["U Aung","1234@Aung"]
    username=input("Username->")
    password=input("Password->")
    if username!=Owner[0]:
        print("Wrong Username!Try again!")
        login()
    elif password!=Owner[1]:
        print("Wrong Password!Try again!")
        login()
    else:
        print("Owner login Successful!")
        Categories.owner_Cati()
    
        


        
