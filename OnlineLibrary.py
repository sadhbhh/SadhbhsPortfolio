borrowed = ["book15", "book234"]                 #these are the lists i'll be using
sci_fi = ["book43", "book19", "book7"]
comedybooks = ["book93", "book6", "book102"]
dramabooks = ["book40", "book3", "book87"]
non_fiction = ["book9","book208","book54"]
kidsbooks = ["book12", "book214", "book192"]
genrechoice2 = ["action", "crime", "teen fiction", "educational"]

print("Welcome to the online library!")

print("You are currently borrowing these books")

print (borrowed)                            

while True:                             
    print("What genre would you like to browse?")
    genrechoice=input("sci-fi, comedy, drama, non-fiction, kids ")       #the client decides which genre to browse

    if genrechoice== "sci-fi":
            print("these are our most popular books in 'sci-fi' at the moment")                
            print (sci_fi)
            break                                   
    elif genrechoice== "comedy":
            print("these are our most popular books in 'comedy' at the moment")
            print (comedybooks)
            break   
    elif genrechoice== "drama":
            print("these are our most popular books in 'drama' at the moment")
            print (dramabooks)
            break 
    elif genrechoice== "non-fiction":
            print("these are our most popular books in 'non-fiction' at the moment")
            print (non_fiction)
            break
    elif genrechoice== "kids":
            print("these are our most popular books in 'kids' at the moment")
            print (kidsbooks)
            break 
    else:
            print("these are our other genres")
            print ("genrechoice2")
            break

while True:   
    whatever=input("would you like to borrow a book?")       #the client decides which book to borrow
    if whatever== "yes":
            print("which one?")
            bookchoice=input("")
            borrowed.append(bookchoice)
            break
    elif whatever== "no":
            print("okay, thank you for browsing!")
            break
    else:
            print("I don't understand")
            break
        
print("You are currently borrowing these books")

print (borrowed)                                 

print("Thank you for your time.")
            
