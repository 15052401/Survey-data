__author__ = 'Edward'


def read_data():
    """Creates a list of the data

    it makes a master list with sublist for each line with the scores stored as a sublist of that"""
    data = []
    x = 0
    for eachline in raw_data:
        eachline = eachline.split()
        data.append([eachline[0]])
        data[x].append(eachline[1:4])
        x += 1
    return(data)#This returns the generated list of data



def menu():
    """This prints out the menu choices that are availble to the user"""
    print("""Main menu
    0. Quit
    1. Display the menu
    2. Display all the survey information
    3. Given a department inputted by the user display the number of customers that have answered the survey and the average result for that department
    4. Display the department(s) with the highest average of customer satisfaction
    5. Display the department(s) with the lowest average customer satisfaction
    6. Display the departments for which 50% or more of the customers voted fair or poor.
    7. Display the departments for which 60% or more of the customers voted good.
    8. Display the number of people that have used the customer satisfaction devices and the total average value of their responses.""")



def display_data():
    """This prints out all of the department names each on a new line"""
    for line in data_list:
        print(line)



def calculate_total():
    """this calculates the total number of votes across all departments

    It goes into the first department and then adds them all to total and then moves on to the next department until it has gone through them all and returns the total"""
    x = 0
    total = 0
    lines_in_data = -1
    for departments in data_list:
        lines_in_data += 1
    while x <= lines_in_data:
        for numbers in data_list[x][1]:
            total += int(numbers)
        x += 1
    return(total)#returns the total number of votes in the survey



def calculate_total_by_department(x):
    """This gives the total number of votes for a chosen department

    This function given a department will go through all of the data and find that department and will then calculate the total number of votes in that department"""
    y = 0
    for list in data_list:
        y += 1
        for department in list:
            if x == department:
                return(int(data_list[y-1][1][0]) + int(data_list[y-1][1][1]) + int(data_list[y-1][1][2]))#returns the total number of votes



def calculate_average_by_department(x):
    """given a department this will tell you the average rating

    This function given a department will go through all of the data and find that department and then it will calculate the avrage vote score"""
    y = 0
    for list in data_list:
        y += 1
        for department in list:
            if x == department:
                return((float(data_list[y-1][1][0])*3 + float(data_list[y-1][1][1])*2 + float(data_list[y-1][1][2])*1)/(float(data_list[y-1][1][0]) + float(data_list[y-1][1][1]) + float(data_list[y-1][1][2]))) #returns the average vote score of thedepartment



def display_highest():
    """This shows the department that has the highest average rating

    It goes through all the departments calculateing their average score and if it is larger than the largest score up until that point it reassigns that value as the highest average and stores the name of the department. This continues until it has gone through all the data"""
    y = 0
    x = 0
    for list in data_list:
        y += 1
        for department in list:
            if x < float((float(data_list[y-1][1][0])*3 + float(data_list[y-1][1][1])*2 + float(data_list[y-1][1][2])*1)/(float(data_list[y-1][1][0]) + float(data_list[y-1][1][1]) + float(data_list[y-1][1][2]))):
               x = float((int(data_list[y-1][1][0])*3 + float(data_list[y-1][1][1])*2 + float(data_list[y-1][1][2])*1)/(float(data_list[y-1][1][0]) + float(data_list[y-1][1][1]) + float(data_list[y-1][1][2])))
               dep = data_list[y-1][0]
    return(dep, x)#returns the name of the department and its score



def display_lowest():
    """This shows the department with the lowest average raiting

    It goes through all the departments calculateing their average score and if it is smaller than the smallest score up until that point it reassigns that value as the smallest average and stores the name of the department. This continues until it has gone through all the data"""
    y = 0
    x = 4 #number bigger than the max possible average
    for list in data_list:
        y += 1
        for department in list:
            if x > float((float(data_list[y-1][1][0])*3 + float(data_list[y-1][1][1])*2 + float(data_list[y-1][1][2])*1)/(float(data_list[y-1][1][0]) + float(data_list[y-1][1][1]) + float(data_list[y-1][1][2]))):
               x = float((int(data_list[y-1][1][0])*3 + float(data_list[y-1][1][1])*2 + float(data_list[y-1][1][2])*1)/(float(data_list[y-1][1][0]) + float(data_list[y-1][1][1]) + float(data_list[y-1][1][2])))
               dep = data_list[y-1][0] # this stores the name of the most recent department with the lowest value up to that point
    return(dep, x)#returns the name of the department and its score



def calculate_average():
    """This gives you the average raiting over all of the departments

    It will go through all of the departments and get the first value from each and add them up and then add it to a list then go and do the same for the next 2 and then calculate the average"""
    x = 0
    data = []
    lines_in_data = -1
    for departments in data_list:
        lines_in_data += 1
    while x <= 2:
        y = 0
        total = 0
        while y <= lines_in_data:#This adapts the prgram to go through all the lines in the data no matter what text file is used as long as it has the same format
            total += int(data_list[y][1][x])
            y += 1
        data.append(total)
        x += 1
    average = (float(data[0]) * 3 + float(data[1]) * 2 + float(data[2]) * 1)/calculate_total()
    return(average)#returns the average score of the survey



def display_poor_performence():
    """This shows a list of departments where more than 50% voted fair or poor

    It goes through all of the departments and checks if more than 50% of people voted fair or poor and if they have it adds the name of the department to the list \"poor\" """
    poor = []
    for list in data_list:
        if int(list[1][0]) <= (int(list[1][1])+int(list[1][2])):#This checks if more than%50 of customers voted fair or poor than good
            poor.append(list[0])
    return(poor)#This returns a list of departments that met the criteria



def display_excellent_perforemance():
    """Shows a list of departments where more than %60 voted good

    It goes through the departments and checks if the more than 60% of people voted good and if they have it adds the name of the department to a list"""
    good = []
    for list in data_list:
        if int(list[1][0]) >= (0.6*((int(list[1][1])+int(list[1][2])+int(list[1][0])))):
            good.append(list[0])
    return(good)#returns a list of all departments with a good raiting



raw_data = open("data.txt", "r")
data_list = read_data()

menu()
choice = int(input("------------------------------------------------------------------------------------------------------------------------------------ \nPlease indicate with a number which action you would like to perform. If at anytime you would like to see the options again just enter \"1\" :"))
while choice != 0:
    if choice == 1:
        menu()
        
    elif choice == 2:
        display_data()
        
    elif choice == 3:
        print("The deaprtments available are:")
        for line in data_list:
            print(line[0])
        x = input("Please input the department you would like to see the data from :")#Has to be raw_input when working on my pc and just input on uni pc
        while calculate_total_by_department(x) == None:
            x = input("Department not found! Please check your spelling and that the first letter is capitalized and input the department you would like to see the data from again :")#Has to be raw_input when working on my pc and just input on uni pc
        print("In the" , x , "department, the total number of votes is" , calculate_total_by_department(x), "and the average vote score was" , round(calculate_average_by_department(x),2))
        
    elif choice == 4:
        print(display_highest()[0], "Has the highest level of customer satisfaction of" ,round(display_highest()[1],2) )

    elif choice == 5:
        print(display_lowest()[0] , "Has the lowest level of customer satisfaction of" , round(display_lowest()[1],2))

    elif choice == 6:
        print("The departments " , display_poor_performence()[0:], " had 50% or more of the votes vote fair or poor")

    elif choice == 7:
        if display_excellent_perforemance() == []:
            print("0 Department(s) had 60% or more of the voters vote good")
        else :
            print(display_excellent_perforemance() , "Department(s) had 60% or more of the voters vote good")

    elif choice == 8:
        print(calculate_total(), "people voted in all of the surveys and the average score of all the votes across all departments was :" , round(calculate_average(), 2) )

    elif choice > 8 or choice < 0:
        print("Invalid choice, please select a value from in the range 0-8")

    choice = int(input("------------------------------------------------------------------------------------------------------------------------------------ \nPlease indicate with a number which action you would like to perform. If at anytime you would like to see the options again just enter \"1\" :"))

print("Thank you, goodbye")

