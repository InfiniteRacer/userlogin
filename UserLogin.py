#Username - scs
#Password - python

global username

username = 'scs'

def userarea():

    usernameinput=input("What's your user name? ")

    if usernameinput == username:
        
        print("")
        password()
        
    else:
        
        print("")
        print("Wrong, try again.")
        print("")
        userarea()
        
def password():
    
    password = 'python'
    
    passwordinput=input("What's the password? ")

    if passwordinput == password:
        
        print("")
        finish()
        
    else:
        
        print("")
        print("Wrong, try again. 1 out of 3 attempts.")
        print("")
        
        passwordinput=input("What's the password? ")
        
        if passwordinput == password:
            
            print("")
            finish()
            
        else:
            
            print("Wrong, try again. 2 out of 3 attempts.")
            print("")
            
            passwordinput=input("What's the password? ")
            
            if passwordinput == password:
                
                print("")
                finish()
                
            else:
                
                print("Wrong. 3 out of 3 attempts used.")
                exit()
            
        
def finish():
    
    print("Logged in.")
    
userarea()