import os 
from pathlib import Path
#all the adress input should be given in raw strings (r'input')

""" working directory adress for this project """
#C:\Users\amite\OneDrive\Desktop\file handler project 


def create_folder(adress,name):
     
    if adress == '':
        workplace = os.getcwd
    else :
        os.chdir(adress)
    if name == '':
        os.mkdir('newfolder')
    else :
        os.mkdir(name)    
    
def read_folder(adress,name):
    if adress == "":
        adress = os.getcwd
    else :
        os.chdir(adress)

    folderpath = Path(name)
    if folderpath.exists():
        content_list = (os.listdir(folderpath))
        print(content_list)
    else :
        print("no such folder exist")



def update_folder(adress,name,newname):
    if adress == "":
        adress = os.getcwd
    else :
        os.chdir(adress)

    if newname == "":
        newname = "nayanaam"
    else :
        newname == newname 

    folderpath = Path(name)
    if folderpath.exists():
        folderpath.rename(newname)
    else :
        print("no such folder exist")

def delete_folder(adress,name):
    if adress == "":
        adress = os.getcwd
    else :
        os.chdir(adress)
    
    folderpath = Path(name)
    if folderpath.exists() :
        os.rmdir(name)
    else :
        print("no folderfound")


def create_file(adress,name):
    if adress == "":
        adress == os.getcwd
    else :
        os.chdir(adress)
    with open (name , 'x') as name :
        print(f'{name} file is created')

def read_file(adress , file_name):
    
    if adress == "":
        adress == os.getcwd
    else :
        os.chdir(adress)

    if Path(file_name).exists():
        with open(file_name,'r') as book:
            print(book.read())
    else :
        print("no file found")
        

def dele_file(adress,file_name):
    if adress == "":
        adress == os.getcwd
    else :
        os.chdir(adress)

    if Path(file_name).exists() :
        os.remove(file_name)
        print("file succesfully removed")
    else :
        print("no such file found")

def update_file(adress , file_name):
    if adress == "":
        adress == os.getcwd
    else :
        os.chdir(adress)

    a = int(input("1 for name uapdate \n 2 for appending text \n 3 for overriding text"))
    if a == 1:
        if Path(file_name).exists():
            Path(file_name).rename(input("newname :: "))
        else :
            print('no such file found ')

    elif a == 2:
        if Path(file_name).exists():
            with open (file_name , 'a') as book:
                book.write(input('type your text'))
        else :
            print("no file found")

    elif a == 3:
        if Path(file_name).exists():
            with open (file_name , 'w') as book:
                book.write(input('type your text'))
        else :
            print("no file found")
    else :
        print("type correct option")


print("1 for folder crud options ")
print("2 for file crud operations")

form = int(input("file or folder :: \n"))

if form == 1:
    print("c :: for creating folder\nr :: for reaing folder\nu :: for updating folder\nd :: for deleting folder ")
    opt = str(input("operaion"))
    adress = input("enter the adress ")
    name = input("folder name")
    if opt == "c":
        
        create_folder(adress,name)

    elif opt == "r":
        read_folder(adress , name)

    elif opt == "u":
        
        update_folder(adress,name,input("new name"))
    
    elif opt == "d":
        delete_folder(adress,name)
    
    else :
        print("chose the correct option")


elif form == 2:
    print("c :: for creating \nr :: for reaing file\nu :: for updating file\nd :: for deleting file ")
    opt = str(input("operaion"))
    adress = input("enter the adress ")
    name = input("folder name")
    if opt == "c":
        
        create_file(adress,name)

    elif opt == "r":
        read_file(adress , name)

    elif opt == "u":
        
        update_file(adress,name)
    
    elif opt == "d":
        dele_file(adress,name)
    
    else :
        print("chose the correct option")