import csv
import Categories
import tools

def customer():
    print("➕Press 1 for adding new customer➕")
    print("➕Press 2 for removing/delecting customer➕")
    print("➕Press 3 for searching customer➕")
    print("➕Press 4 for updating customer➕")
    print("➕Press 5 for exit➕")
    user_selected=int(input("Please Enter➡️ "))
    match user_selected:
        case 1:
            add_customer()
        case 2:
            remove_customer()
        case 3:
            search_customer()
        case 4:
            update_customer()
        case 5:
            Categories.owner_Cati()
        case default:
            print("❌Wrong Option!❌")
            customer()
def add_customer():
    with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","r") as readfile:
        csvFile = csv.DictReader(readfile)
        cu_name=input("Enter your name➡️ ")
        cu_dob=input("Enter your date of birth➡️ ")
        cu_address=input("Enter your address➡️ ")
        flag=False
        while flag==False:
            cu_contact=input("Enter your mobile number➡️ ")
            flag=tools.ph_validation(cu_contact)
            if flag:
                for i in csvFile:
                    if cu_name==i["Name"] and cu_dob==i["DOB"]:
                        print("User already exist!")
                        customer()
                with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","a") as writefile:
                    columns=["ID","Name","DOB","Address","Contact"]
                    csv_writer=csv.DictWriter(writefile,fieldnames=columns)
                    cu_id=tools.id_generator()
                    csv_writer.writerow({"ID":cu_id,"Name":cu_name,"DOB":cu_dob,"Address":cu_address,"Contact":cu_contact})
                    print("Customer Added Successfully!!!")
                customer()  
        #for i in csvFile:
            #print(i)    
def remove_customer():
    user_name=input("Enter Name->")
    with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","rb") as readfile:
        csv_reader=csv.DictReader(readfile)
        with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","w") as writefile:
            csv_writer=csv.DictWriter(writefile)
            for row in csv_reader:
                if row["Name"]!=0:
                    csv_writer.writerow(row)
def search_customer():
    username=input("Enter username to search ->")
    with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","r") as readfile:
        csv_reader=csv.DictReader(readfile)
        flag=True
        for i in csv_reader:
            if i["Name"]==username:
                flag=False
                print("➡️", i)
                customer()
        if flag==True:
            print("❌User not found!❌")
            customer()
def update_customer():
    username=input("Enter username to update ->")
    userDOB=input("Enter DOB ->")
    with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","r") as readfile:
        csv_reader=csv.DictReader(readfile)
        with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","w") as writefile:
            updatefile=csv.DictWriter(writefile)
            for i in csv_reader:
                if i["Name"]==username and i["DOB"]==userDOB:
                    to_update=input("Enter what to update Eg:Name/DOB/Address/Contact->")
                    if to_update=="Name":
                        updatefile.writerow({"ID":i["ID"],"Name":to_update,"DOB":i["DOB"],"Address":i["Address"],"Contact":i["Contact"]})
                    elif to_update=="DOB":
                        updatefile.writerow({"ID":i["ID"],"Name":i["Name"],"DOB":i,"Address":i["Address"],"Contact":i["Contact"]})
                    elif to_update=="Address":
                        pass
                    elif to_update=="Contact":
                        pass
                    else:
                        print("Invalid Option")
                        update_customer()
                



add_customer()