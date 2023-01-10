def noob_check(i,x):
    if i==0:
        if x.lower()=="kathmandu" or x.lower()=="iii":
            return True
        else:
            return False
    if i==1:
        if x=="8849" or x.lower()=="ii":
            return True
        else:
            return False
    if i==2:
        if x=="118" or x.lower()=="iii":
            return True
        else:
            return False
    if i==3:
        if x.lower()=="mercury" or x.lower()=="ii":
            return True
        else:
            return False
    if i==4:
        if x=="1.6" or x.lower()=="1.6":
            return True
        else:
            return False


    
def medium_check(i,x):
    if i==0:
        if x.lower()=="leonardo da vinci" or x.lower()=="ii":
            return True
        else:
            return False
    if i==1:
        if x.lower()=="ernest hemingway" or x.lower()=="ii":
            return True
        else:
            return False
    if i==2:
        if x=="5" or x.lower()=="iii":
            return True
        else:
            return False
    if i==3:
        if x.lower()=="hazelnut" or x.lower()=="i":
            return True
        else:
            return False
    if i==4:
        if x.lower()=="god of war" or x.lower()=="iii":
            return True
        else:
            return False


def pro_check(i,x):
    if i==0:
        if x=="1945" or x.lower()=="i":
            return True
        else:
            return False
    if i==1:
        if x.lower()=="austria" or x.lower()=="ii":
            return True
        else:
            return False
    if i==2:
        if x=="1756" or x.lower()=="iii":
            return True
        else:
            return False
    if i==3:
        if x.lower()=="poland" or x.lower()=="i":
            return True
        else:
            return False
    if i==4:
        if x.lower()=="ottawa" or x.lower()=="iii":
            return True
        else:
            return False
    

def user_input():
    value=input("Choose your level:Noob(n),Medium(m),Pro(p)\n").lower()
    return value[0]

def noob():
    question=["What is the capital city of Nepal?","What is the height of Mt.Everest in meters?","How many elements are there in a periodic table?",
    "What planet is closest to the Sun?","To a single decimal point, how many kilometers in a mile?"]
    c=0
    for i in range(0,5):
        print(f"\n{question[i]}\n")
        
        if i==0:
            print('''i.)New Delhi           ii.)Jhapa

iii.)Kathmandu          iv.)New York\n''')
        
        elif i==1:
            print('''i.)8848         ii.)8849

iii.)12000          iv.)9899\n''')

        elif i==2:
            print('''i.)120          ii.)125

iii.)118         iv.)119\n''')
        
        elif i==3:
            print('''i.)Venus          ii.)Mercury

iii.)Earth          iv.)Uranus\n''')
        elif i==4:
            print('''i.)1.3          ii.)1.9

iii.)1.4          iv.)1.6\n''')


    
        x=input("Please enter your answer: \n")
        y=noob_check(i,x)
        if y==True:
            c=c+1
            continue
        elif y==False:
            break
    return c    


def medium():
    question=["Who painted the Mona Lisa?","Who was the author of The Old Man and the Sea?","How many colors are present in a olympic ring?",
    "What nut is in the middle of Forrero Rocher?","Kratos is the main character of what video game series?"]
    c=0
    for i in range(0,5):
        print(f"\n{question[i]}\n")
        
        if i==0:
            print('''i.)Pablo Picasso           ii.)Leonardo da Vinci

iii.)Salavador Dalí         iv.)Masashi Kishimoto\n''')
        
        elif i==1:
            print('''i.)Franz Kafka         ii.)Ernest Hemingway

iii.)Eiichiro Oda          iv.)William Shakespeare\n''')

        elif i==2:
            print('''i.)7          ii.)6

iii.)5         iv.)8\n''')
        
        elif i==3:
            print('''i.)Hazelnut          ii.)Walnut

iii.)Deez Nuts          iv.)Almonds\n''')
        elif i==4:
            print('''i.)Assassin's Creed         ii.)Sekiro: Shadows Die Twice

iii.)God of War          iv.)Red Dead Redemption\n''')


    
        x=input("Please enter your answer: \n")
        y=medium_check(i,x)
        if y==True:
            c=c+1
            continue
        elif y==False:
            break
    return c    

def pro():
    question=["What year was the United Nations established?","In which country was Adolf Hitler born?","In what year was Wolfgang Amadeus Mozart born?",
    "In which country was Marie Curie born?","What is the capital of Canada?"] #1945,#1756
    c=0
    for i in range(0,5):
        print(f"\n{question[i]}\n")
        
        if i==0:
            print('''i.)1945           ii.)1938

iii.)1949          iv.)1936\n''')
        
        elif i==1:
            print('''i.)Sweden         ii.)Austria

iii.)Germany          iv.)France\n''')

        elif i==2:
            print('''i.)1789          ii.)1889

iii.)1756         iv.)1798\n''')
        
        elif i==3:
            print('''i.)Poland          ii.)France

iii.)England          iv.)Sweden\n''')
        elif i==4:
            print('''i.)Copenhagen          ii.)Toronto

iii.)Ottawa          iv.)Hamilton\n''')


    
        x=input("Please enter your answer: \n")
        y=pro_check(i,x)
        if y==True:
            c=c+1
            continue
        elif y==False:
            break
    return c    

def main():
    a=user_input()
    if a=="n":
        b=noob()
    elif a=="m":
        b=medium()
    elif a=="p":
        b=pro() 
    
    if b==0:
        print(f"You only got {b} points\n")
        print(f"You won $0")
         
    elif b==1:
        print(f"You got {b} points\n")
        print("You won $500")
     
    elif b==2:
        print(f"You got {b} points")
        print("You won $1000")

    elif b==3:
        print(f"You got {b} points")
        print("You won $1500")

    elif b==4:
        print(f"You got {b} points")
        print("You won $2000")

    elif b==5:
        print(f"You got {b} points")
        print("You won $2500")    

ask=input("Do you want to play the quiz?(y/n)").lower()
if ask=="y":
    main()
elif ask=="n":
    print("Get Out!")
else:
    print("Enter a valid option")
    
            
    