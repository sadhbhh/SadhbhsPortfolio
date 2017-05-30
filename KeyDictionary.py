from time import sleep
print("Hello, welcome to KeyDictionary. This tool will help you to identify key signatures quickly and efficiently.") #Welcome to the program
sleep(3)
print("First of all, how many sharps/flats does the key signature have?")
 #below is just a function, ignore it for now
def enter():
    print("What are the sharps/flats? If there are more than one, seperate them with a comma, like this:'B flat, E flat' or 'C sharp, G sharp, F sharp'. If you don't use this format the programme will not work efficiently.")
    
number = int(input("")) #user enters the amount of sharps or flats
if number==1:
     enter()
     flatsharps=input("") #the user specifies the sharps or flats
     if flatsharps=="F sharp":
        print("This is the key of G major.") #the user is told what the key is
     elif flatsharps=="B flat":
        print("This is the key of F major.")
        
     else:
        print("This doesn't make sense")
        

elif number==2:
     enter()
     flatsharps=input("")
     if flatsharps == "C sharp, F sharp" or flatsharps == "F sharp, C sharp":
        print("This is the key of D major.")
        
     elif flatsharps=="B flat, E flat" or flatsharps=="E flat, B flat":
        print("This is the key of B flat major.")
        
     else:
        print("This doesn't make sense.")
        
elif number==3:
     enter()
     flatsharps=input("")
     if flatsharps=="C sharp, G sharp, F sharp" or flatsharps=="G sharp, F sharp, C sharp" or flatsharps=="F sharp, G sharp, C sharp"  or flatsharps=="F sharp, C sharp, G sharp" or flatsharps=="G sharp, C sharp, F sharp" or flatsharps=="C sharp, F sharp, G sharp":
        print("This is the key of A major.")
        
     elif flatsharps == "E flat, B flat, A flat" or flatsharps == "B flat, E flat, A flat" or flatsharps == "A flat, B flat, E flat" or flatsharps == "E flat, A flat, B flat" or flatsharps == "B flat, A flat, E flat" or flatsharps == "A flat, E flat, B flat":
        print("This is the key of E flat major")
        
     else:
        print("I don't understand.")
        
elif number==4:
    enter()
    flatsharps=input("")
    if flatsharps == "C sharp, D sharp, F sharp, G sharp" or flatsharps == "D sharp, F sharp, G sharp, C sharp" or flatsharps == "F sharp, G sharp, C sharp, D sharp" or flatsharps == "G sharp, C sharp, D sharp, F sharp" or flatsharps == "C sharp, G sharp, D sharp, F sharp" or flatsharps == "C sharp, D sharp, G sharp, F sharp" or flatsharps == "F sharp, D sharp, G sharp, C sharp" or flatsharps == "G sharp, F sharp, D sharp, C sharp" or flatsharps == "C sharp, F sharp, G sharp, D sharp" or flatsharps == "C sharp, F sharp, D sharp, G sharp" or flatsharps == "D sharp, F sharp, C sharp, G sharp" or flatsharps == "D sharp, C sharp, F sharp, G sharp" or flatsharps == "D sharp, C sharp, G sharp, F sharp" or flatsharps == "D sharp, G sharp, F sharp, C sharp" or flatsharps == "D sharp, G sharp, C sharp, F sharp" or flatsharps == "C sharp, G sharp, F sharp, D sharp" or flatsharps == "F sharp, G sharp, D sharp, C sharp" or flatsharps == "F sharp, D sharp, C sharp, G sharp" or flatsharps == "F sharp, C sharp, G sharp, D sharp" or flatsharps == "F sharp, C sharp, D sharp, G sharp" or flatsharps == "G sharp, C sharp, F sharp, D sharp" or flatsharps == "G sharp, C sharp, F sharp, D sharp" or flatsharps == "G sharp, F sharp, C sharp, D sharp" or flatsharps == "G sharp, D sharp, F sharp, C sharp" or flatsharps == "G sharp, D sharp, C sharp, F sharp":
        print("This is the key of E major.")
    elif flatsharps == "A flat, B flat, D flat, E flat" or flatsharps == "A flat, B flat, E flat, D flat" or flatsharps == "A flat, E flat, D flat, B flat" or flatsharps == " A flat, E flat, B flat, D flat" or flatsharps == "A flat, D flat, E flat, B flat" or flatsharps == "A flat, D flat, B flat, E flat" or flatsharps == "B flat, D flat, E flat, A flat" or flatsharps == "B flat, D flat, A flat, E flat" or flatsharps == "B flat, A flat, D flat, E flat" or flatsharps == "B flat, A flat, E flat, D flat" or flatsharps == "B flat, E flat, A flat, D flat" or flatsharps == "B flat, E flat, D flat, A flat" or flatsharps == "E flat, A flat, D flat, B flat" or flatsharps == "E flat, A flat, B flat, D flat" or flatsharps == "E flat, D flat, B flat, A flat" or flatsharps == "E flat, D flat, A flat, B flat" or flatsharps == "E flat, B flat, D flat, A flat" or flatsharps == "E flat, B flat, A flat, D flat" or flatsharps == "D flat, A flat, B flat, E flat" or flatsharps == "D flat, A flat, E flat, B flat" or flatsharps == "D flat, B flat, A flat, E flat" or flatsharps == "D flat, B flat, E flat, A flat" or flatsharps == "D flat, E flat, A flat, B flat" or flatsharps == "D flat, E flat, B flat, A flat":
        print("This is the key of A flat major.")
    else:
        print("I don't understand.")
      
      #this is where I changed the format to save me from typing so much
elif number==5:
    Bmajor = "A sharp, C sharp, D sharp, F sharp, G sharp" 
    Dflatmajor = "D flat, B flat, C flat, F flat, G flat"
    print("Are the sharps/flats: A) %s or B) %s?" % (Bmajor, Dflatmajor))
    answer=input(" ")
    if answer=="a":
        print("This is the key of B major.")
    elif answer=="b":
        print("This is the key of D flat major.")
    else:
        print("This was not an option.") 
      
elif number==6:
    Fsharpmajor = "A sharp, C sharp, D sharp, E sharp, F sharp, G sharp"
    Gflatmajor = "B flat, C flat, D flat, E flat, F flat, G flat"
    print("Are the sharps/flats: a) %s or b) %s?" % (Fsharpmajor, Gflatmajor))
    answer=input(" ")
    if answer=="a":
        print("This is the key of F sharp major.")
    elif answer=="b":
        print("This is the key of G flat major.")
    else:
        print("This was not an option.")
        
elif number==7:
    Csharpmajor = "A sharp, B sharp, C sharp, D sharp, E sharp, F sharp, G sharp"
    Cflatmajor = "A flat, B flat, C flat, D flat, E flat, F flat, G flat"
    print("Are the sharps/flats: a) %s or b) %s?" % (Csharpmajor, Cflatmajor))
    answer=input(" ")
    if answer=="a":
        print("This is the key of C sharp major.")
    elif answer=="b":
        print("This is the key of C flat major.")
    else:
        print("This was not an option.")
        
elif number > 7:
	   print("There are no key signature with this many sharps or flats.")
	   
elif number==0:
	   print("This is the key of C major.")
	   
elif number < 0:
	   print("This is not possible.")
	   
else:
     print("I don't understand.")
     
sleep(0.5)
print("I hope this was helpful!")


print("")
print(" ___|)______ ")
print("|___/_______      ")
print("|__/|_______  ")
print("|_/(|,\_____  ")
print("|_\_|_/_____         ")
print("    |                        ")
print("  (_|       ")
print("")

"""
Output looks like:
 ___|)_________|___________  
|___/___|______|____         
|__/|___|-.__,-.________     
|_/(|,\_|/___`-'______       
|_\_|_/__________            
    |                        
  (_|      KEYDICTIONARY
           by Sadhbh Eddison 2016
           
"""
