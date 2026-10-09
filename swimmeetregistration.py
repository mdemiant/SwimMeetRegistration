'''With this function we can determinate if the year the user was
born is a leap year or not, by dividing the year and checking if it has residue or not'''

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

'''With this function we can categorize the age of the user'''
'''Add an `else` statement so that the program ends when they are not 11 years old.'''

def category(age):
    if 11 <= age <= 12:
        return "11-12 years old"
    elif 13 <= age <= 14:
        return "13-14 years old"
    elif 15 <= age <= 16:
        return "15-16 years old"
    elif 17 <= age <= 18:
        return "17-18 years old"
    elif age >= 19:
        return "19 and older"
    else:
        return "Not old enough to participate"

'''With this function we charge the base fee of the meet'''
def calculate_base_fee():
    return 1000

'''This function calculates the cost of the extraordinary events'''
def extraordinary(num_events):
    cost = num_events*300
    if num_events>3:
        cost = cost*0.85
    return cost

    '''This function helps organize the program'''
def main():
    '''Lists to save the data of the user'''   
    swimmers = []
    totals = []
    leap_years_status = []
    
    print("\nMEET REGISTRATION 2026\n")
    print("Avaible events:\t 50 free, 100 free, 200 free,400 free, 800 free, 1500 free, 50 fly, 100 fly, 200 fly, 50 back, 100 back,\n200 back, 50 breastroke, 100 breastroke, 200 breastroke.")
    
    '''With this while we can offer the user to add another swimmer'''
    
    seguirregistro = "yes"

    while seguirregistro == "yes":
        name = input("\nInsert name: ")
        '''Use of nested loops following the first while to make sure the user gives a name'''
        while len(name)==0:
            print("Enter a name:")
            name = input("Insert name: ")
            
            '''Use of nested loops following the second while to make sure the user gives a positive number'''
            
        age = int(input("Age: "))
        while age <= 0:
            print("Only positive numbers will be accepted")
            age = int(input("Age: "))

        cat = category(age)
        print("Category:", cat)

        if cat == "Not old enough to participate":
            print("You are not eligible for the competition.")
            
            '''The use of break to end inmediatly the program when the swimmer is 10 years or lower'''

            break
        
            '''With this while we verify that the birth year the user gave is not false,
            using the year of birth of the oldest person alive and the current year'''

        birth_year = int(input("Birth year: "))
        while birth_year <= 1909 or birth_year > 2026:
            print("Please enter a valid birth year.")
            birth_year = int(input("Birth year: "))

        born_leap = is_leap_year(birth_year)
        print("Born in a leap year:", born_leap)
        
        '''With this while after asking the user if they want any extraordinary events,
        we can secure that the number isn't negative causing trouble with the base fee'''

        want_extra = input("\nDo you want to add extraordinary events? (yes/no):")

        if want_extra == "yes":
            extra_count = int(input("Number of extraordinary events: "))
            while extra_count <= 0:
                print("Please enter a number greater than 0.")
                extra_count = int(input("Number of extraordinary events: "))
                
                '''With this list we save the user extraordinary events'''

            selected_events = []
            
            '''With this loop we give the user the chance to choose their events'''

            for x in range(extra_count):
                event_name = input(f"Enter name for extraordinary event {x + 1}:")
                
                '''With this while we secure that they write the events'''
                
                while len(event_name) == 0:
                    print("Event name cannot be empty.")
                    event_name = input(f"Enter name for extraordinary event #{x + 1}:")
                selected_events.append(event_name)
        else:
            extra_count = 0
            
        '''We calculate the cost of all the swimmers registrated'''
        
        base = calculate_base_fee()
        extra_cost = extraordinary(extra_count)
        total_payment = base+extra_cost

        '''With the .append we add to the lists made before, the data the user gives'''
        
        swimmers.append(name)
        totals.append(total_payment)
        leap_years_status.append(born_leap)

        print("\nBase registration fee:", base)
        print("Total price for extraordinary events:", extra_cost)
        print("Total to pay for", name, ":", total_payment)

        seguirregistro = input("\nDo you want to add another swimmer? (yes/no):")

    '''We give the summary of the registration'''
    
    if len(swimmers) > 0:
        print("\nFINAL REGISTRATION SUMMARY")
        

        total_income = 0
        leap_year_count = 0

        '''This loop helps to registrate the data of all the swimmers'''
        
        for x in range(len(swimmers)):
            print(f"\n{x + 1}. {swimmers[x]} - Total Paid: {totals[x]}")
            total_income += totals[x]
            if leap_years_status[x]:
                leap_year_count += 1

        average_income = total_income / len(swimmers)
        
        
        print("\nSwimmers registrated:", len(swimmers))
        print("\nTotal:", total_income, "pesos")
        print("\nAverage payment per swimmer:", average_income, "pesos")
        print("\nSwimmers born in leap years:", leap_year_count)
      


main()
