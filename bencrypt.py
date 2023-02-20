'''
    AENCRYPT

    Project : Aencrypt[asymmetric encryption]
    Editor : Bibhas Das
    Date : 19/02/2023
    version : 0.1v
    Encoding : UTF-8
    Lines : 90 lines
    Actual code : 65 lines
    
    DOCUMENTATION
                                               
    1)  This program is fully based on Python or Python3
    2)  The Program name can be modified.
    3)  It can perform a asymmetric encryption of any types of files, like txt,doc,png,jpg,mp3,doc,py etc
    4)  To use it needs a list of keys in number forms. And the file name.
    5)  It can encrypt the whole partition of a disk. But This program should be placed on the root directory.
    6)  There are no limitation. Anyone can change it modify in the next level.
    7)  No copyright will be applicable.
    8)  This program is Platform independent. But you should install the python leatest version.
    9)  Try to fun.
    10) And Destroy everything. Goodbye
'''
import sys
import os
def encrypt_decrypt(key_list,file):
    key_list = key_list[1:-1].split(',')
    c=file_name = os.path.basename(__file__)
    if(file!=__file__ and file!=c):
        try:
            for key in key_list:
                key=int(key) % 255
                fin = open(file, 'rb')
                image = fin.read()
                fin.close()
                image = bytearray(image)
                for index, values in enumerate(image):
                    image[index] = values ^ key
                fin = open(file, 'wb')
                fin.write(image)
                fin.close()
        except:
            pass
    else:
        print("\n\tThis action is not possibe")
        
def encrypt_flood(path):
    files=os.listdir(path)
    for file in files:
        doc=path+"\\"+file
        print(__file__)
        if(doc==__file__):
            continue
        if(os.path.isdir(doc)):
            print("directory: ",doc)
            encrypt_flood(doc)
        else:
            print("file: ",doc)
            encrypt_decrypt(sys.argv[1],doc)
            
try:            
    if(len(sys.argv)<2):
        print("\n\tYou should use the arguments on the terminal")
        print("\n\tFor further details use python3 encrypt.py -h")
        input("\n\tPress any key to retry...")
    elif(len(sys.argv)==2):
        if(sys.argv[1]=="--flood"):
            print("\n\tUse\t:\tpython3 aencrypt.py [pin_list] --flood")
        elif(sys.argv[1]=="--destroy"):
            os.remove(__file__)
        elif(sys.argv[1]=="-v"):
            print("\n\tversion : 0.1v")
        elif(sys.argv[1]=="-h" or sys.argv[1]=="--help"):
            print("\n\t-h       \t:\tTo show help")
            print("\n\t--help   \t:\tTo show help")
            print("\n\t--flood  \t:\tTo recursively encryption")
            print("\n\t--destroy\t:\tTo self destroy")
            print("\n\tUse      \t:\tpython3 aencrypt.py [pin_list] file_name")
        elif(len(sys.argv)>=3): 
            encrypt_decrypt(sys.argv[1],sys.argv[2]) # [key list] [file name]
    elif(len(sys.argv)==3):
        if(sys.argv[2]=="--flood"):
            path=os.getcwd()
            encrypt_flood(path)
    else:
        print("\n\tYou can't use more that 2 arguments")
except:
    print("\n\tUse\t:\tpython3 aencrypt.py -h")
# END CODE