import csv
import math
import random



def id_generator():
    with open("D://Python//.vscode//Project//Medicine_Shop//customer.csv","r") as readfile:
        csv_reader=csv.DictReader(readfile)
        index=1
        for i in csv_reader:
            if index==int(i["ID"]):
                index+=1
    return index
def otp_generator():
    number="0123456789"
    OTP_code=""
    for i in range(6):
        OTP_code+=number[math.floor(random.random()*10)]
    return OTP_code

def ph_validation(cu_contact):
    if len(cu_contact) == 11 and int(cu_contact[0]) == 0 and int(cu_contact[1]) == 9:
        if int(cu_contact[2]) == 7:
            print('Atom phone number')
        elif int(cu_contact[2]) == 2:
            print('MPT phone number')
        elif int(cu_contact[2]) == 9:
            print('Ooredoo phone number')
        return True
    else:
        print('Invalid Phone Number')
        return False
def password_validation():
    pass


