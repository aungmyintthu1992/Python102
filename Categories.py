import customers
import sales
import medicines
import customer_feedback


def owner_Cati():
    print("There are some categories for owner!")
    categories=int(input("Press 1 for Customers/Press 2 for Medicines/Press 3 for Sales/Press 4 for Customer Feedback->"))
    if categories==1:
        customers.customer()
    elif categories==2:
        medicines.medicine()
    elif categories==3:
        sales.sale()
    elif categories==4:
        customer_feedback.feedback()
    else:
        print("Invalid Option!Please try again!")
        owner_Cati()
        
    
    

def User_Cati():
    pass


