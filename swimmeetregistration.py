'''With this function we can categorize the age of the user'''
def category(age):
 if age >=11 and age <=12:
    return("11-12 years old")
 elif age >=13 and age <=14:
    return("13-14 years old")
 elif age >=15 and age <=16:
    return("15-16 years old")
 elif age >=17 and age <=18:
    return("17-18 years old")
 elif age >= 19:
    return("19 and older")
    '''Add an `else` statement so that the program ends when they are not 11 years old.'''
 else:
    return("Not old enough to participate")
'''This function calculates the cost of the extraordinary events'''
def extraordinary(extra):
    if extra>0:
        return(extra*300)
    else:
        return ("No extraordinary events registrated")
'''This function helps organize the program'''
def main():
    '''With this while we can offer the user to add another swimmer'''
    seguirregistro="yes"
    while seguirregistro=="yes":
        print("Avaible events:\t 50 free, 100 free, 200 free,400 free, 800 free, 1500 free, 50 fly, 100 fly, 200 fly, 50 back, 100 back,\n200 back, 50 breastroke, 100 breastroke, 200 breastroke.")
        print("\nTime limits: \n50 free: 30.00\n100 free: 1:02.00\n200 free: 2:04.00\n400 free: 4:20.70\n800 free: 9:54.00\n1500 free: 18:00.40\n50 fly: 32.80\n100 fly: 1:05.30\n200 fly: 2:23.90\n50 back: 32.87\n100 back: 1:07.33\n200 back: 2:24.67\n50 breastroke: 37.87\n100 breastroke: 1:18.78\n200 breastroke: 2:34.98")
        print("\nExtraordinary events cost: 350 pesos")
        print("MEET REGISTRATION 2026\n")
        name=input("\nInsert name:")
        age=int(input("\nAge:"))
        '''Use of nested loops following the first while to make sure the user gives a positive number'''
        while age<=0:
            print("Only positive numbers will be accepted")
            age=int(input("\nAge:"))
            
        cat=category(age)
        print("\nCategory:",cat)
        '''The use of break to end inmediatly the program when the swimmer is 10 years or lower'''  
        if cat=="Not old enough to participate":
            print("You are not eligible for the competition")
            break
        else:
            extra=int(input("\nNumber of extraordinary events:"))
        '''The use of another while to give the user the option to not add any extraordinary events'''   
        while extra<0:
                print("No extraordinary events registrated")
                extra=int(input("\nNumber of extraordinary events:"))
             
        print("\nTotal price for the extraordinary events:",extraordinary(extra))
        
        seguirregistro=input("Do you want to add another swimmer? (yes/no)")
            


main()    


