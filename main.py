import owner_login
import user_login
def phyu_sin_medical():
    print("*"*100)
    print("💊💊💊 Welcome to PHYU SIN MEDICAL SHOP 💊💊💊")
    user_input=int(input("Press 1 for Owner and 2 for User->"))
    if user_input==1:
        owner_login.login()
    elif user_input==2:
        user_login.login()
    else:
        print("❌Invalid Option!Try Again!❌")
        phyu_sin_medical()
        
        
if __name__=="__main__":
    phyu_sin_medical()    