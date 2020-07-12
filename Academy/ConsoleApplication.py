import csv
import pandas as pd
import shutil
import os
import platform
class Academy:
    def courseofstudy(self):
            with open('course.txt') as f:
                for line in f:
                    print(line.strip())
    def admission(self,*args):
        input_file = open("studentrecord.csv","r+")
        reader_file = csv.reader(input_file)
        value = len(list(reader_file))
        while(value<1):
            with open("studentrecord.csv",'a',newline='\n') as file:
                writer=csv.writer(file)
                writer.writerow(['name','email','phone','degree','payment','due'])
        with open("studentrecord.csv",'a',newline='\n') as file:
            writer=csv.writer(file)
            writer.writerow([*args])
    def newadmission(self):
        courseofstudy()
    def displaydetails(self):
        file = "studentrecord.csv"
        opened = open(file, "r")
        readed = pd.read_csv(file)
        print(readed)
    def updatedetails(self,email,value,nu):
        filename='studentrecord.csv'
        fieldnames=['name','email','phone','degree','payment','due']
        with open(filename, 'r') as csv_file, open(filename.replace('.csv', '_new.csv'), 'w') as temp_file:
            reader=csv.DictReader(csv_file,fieldnames=fieldnames)
            writer=csv.DictWriter(temp_file,fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if nu==1:
                    if row['email']==email:
                        row['name']=value
                    writer.writerow({
                        'name': row["name"],
                        'email': row["email"],
                        'phone': row["phone"],
                        'degree':row["degree"],
                        'payment':row["payment"],
                        'due':row["due"],
                    })
                elif nu==2:
                    if row['email']==email:
                        row['email']=value
                    writer.writerow({
                        'name': row["name"],
                        'email': row["email"],
                        'phone': row["phone"],
                        'degree':row["degree"],
                        'payment':row["payment"],
                        'due':row["due"],
                    })
                elif nu==3:
                    if row['email']==email:
                        row['phone']=value
                    writer.writerow({
                        'name': row["name"],
                        'email': row["email"],
                        'phone': row["phone"],
                        'degree':row["degree"],
                        'payment':row["payment"],
                        'due':row["due"],
                    })
                elif nu==4:
                    if row['email']==email:
                        row['degree']=value
                    writer.writerow({
                        'name': row["name"],
                        'email': row["email"],
                        'phone': row["phone"],
                        'degree':row["degree"],
                        'payment':row["payment"],
                        'due':row["due"],
                    })
            shutil.move(temp_file.name,filename)
            return True
        return False
    def showindividualdetails(self,email):
        with open('studentrecord.csv', mode='r') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                if row["email"] == email:
                    print("Name: %s\t Email: %s\tPhone: %s\t Degree:%s \t Payment: %s\t Due: %s"%(row["name"],row["email"],row["phone"],row["degree"],row["payment"],row["due"]))
    def deleterecord(self,email):
        lines=list()
        with open('studentrecord.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == email:
                        lines.remove(row)
        with open('studentrecord.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    def graduation(self):
        print("Congratulations!! You have successfully graduated from this academy and your refund amount is 20000")
    def clear_screen(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
while True:
    print("Choose any one from the following")
    print("1. If you want to take admission \n2. If you want to inquire with course of study \n3. If you want to see your details \n4. If you want to see all the details \n5. If you want to change your details \n6. If you want to left the program \n7. If you are graduating from the academy \n8. If you want to exit")
    n=int(input())
    if n==1:
        name=input("Enter your name")
        email=input("Enter your email")
        phone=input("Enter your phone number")
        print("Are you graduated? If yes enter 1, If no enter 2")
        n1=int(input())
        if n1==1:
            degree=input("Enter your graduation degree")
        else:
            degree="Not Graduated"
        print("You can pay whole amount or in two installment\n 1. Whole payment \n 2. In Installment of 10000" )
        n3=int(input())
        global due
        if n3==1:
            payment=20000
            due=0
        else:
            payment=10000
            due=10000
        Academy().admission(name,email,phone,degree,payment,due)
        print("Congratulation! You have been admitted to our Academy")
    elif n==2:
        Academy().courseofstudy()
    elif n==3:
        email=input("Enter your email")
        Academy().showindividualdetails(email)
    elif n==4:
        Academy().displaydetails()
    elif n==5:
        email=input("Enter your email")
        print("Which information do you want to update?")
        print("Choose what you want to update\n 1. Name\n 2. Email\n 3. Phone\n 4. Degree")
        nu=int(input())
        value=input("Enter the value you want to change to")
        Academy().updatedetails(email,value,nu)
    elif n==6:
        email=input("Enter your email")
        Academy().deleterecord(email)
        print("Your record has been deleted")
    elif n==7:
        Academy().clear_screen()
        Academy().graduation()
    elif n==8:
        exit()
    else:
        print("You have choosen wrong number")