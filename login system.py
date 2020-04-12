
import re

flag = 0

while(flag == 0):

    print("\n1.To login")
    print("2.To signup")
    choice = int(input())
    
    if(choice == 1):

        with open('data.txt','r') as f:

            print("Enter the username: ",end = " ")
            username=input()
            print("Enter the password: ",end = " ")
            password = input()
            
            for line in f:
                
                l = line.split()
                
                if( username == l[0] ):

                    decrypt_pass=""
                    
                    for i in l[1]:
                        decrypt_pass += chr(ord(i)+1)

                    if(decrypt_pass == password):    
                        print( "Successfully loged in" )
                        flag = 1

                    else:
                        print( "Wrong Password" )
                        flag = 0  
                                            
                else:                    
                    print( "Wrong username" )
                    flag = 0               
            
    elif(choice == 2):
        
        flag = 1
        print("Enter the username: ",end = " ")
        username=input()
        print("Enter the password: ",end = " ")
        password=input()

        while(len(password) <= 8 or len(password) >= 32 ):
            print("Enter password of length between 8-32 characters")
            print("Enter the password again: ",end=" ")
            password=input()

        print("Enter the password again: ",end=" ")
        re_pass = input()
        
        while(re_pass != password):

            print("Password doesn't match.")
            print("Enter the password again:,end=" "")
            re_pass = input()

        encripted_pass = ""
        
        for i in password:
            
            encripted_pass+=chr(ord(i)-1)
                        
        with open('data.txt','a') as f:

            f.write( username + " " + encripted_pass )
            
    else:
        print("Enter a valid input")
