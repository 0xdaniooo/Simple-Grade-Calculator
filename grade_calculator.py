from os import system, name
from grade import Grade
from module import Module

"""
    Written by Daniel Kasprzyk
"""

# function to elear screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')
  

if __name__ == '__main__':
    clear()

    print("-----------------------------------------------------")
    print("Simple Grade Calculator - Written by Daniel Kasprzyk")
    print("-----------------------------------------------------\n")

    # create module
    module_name = input("Enter your module name: ")
    module = Module(module_name)

    total_percentage = 100
    valid_input = False

    # input grades until 100% used up
    while total_percentage > 0:
        clear()
        print("Module: " + module.name)
        print("Total percentage for this module remaining: " + str(total_percentage) + "%\n")

        # name the grade
        grade_name = input("Name of grade: ")
        clear()

        # input weight of grade on module
        valid_input = False
        while valid_input == False:
            print("Module: " + module.name)
            print("Total percentage for this module remaining: " + str(total_percentage) + "%\n")

            percentage_weight = input(f"What is overall weight of '{grade_name}' on the module (percentage wise)?: ")
            try:
                percentage_weight = int(percentage_weight.replace("%", ""))
                int(percentage_weight)
                if percentage_weight > 100:
                    clear()
                    print("Value cannot exceed 100\n")
                    continue
                elif percentage_weight > total_percentage:
                    clear()
                    print("Invalid input. Value is exceeding total of 100%\n")
                    continue
                valid_input = True
            except ValueError:
                clear()
                print("Invalid input. Please try again.\n")

        clear()

        # input what you scored for the grade
        valid_input = False
        while valid_input == False:
            print("Module: " + module.name)
            print("Total percentage for this module remaining: " + str(total_percentage) + "%\n")
            actual_percentage = input(f"What did you score for '{grade_name}' (percentage wise)?: ")
            try:
                actual_percentage = int(actual_percentage.replace("%", ""))
                int(actual_percentage)
                if actual_percentage > 100:
                    clear()
                    print("Value cannot exceed 100\n")
                    continue
                valid_input = True
            except ValueError:
                clear()
                print("Invalid input. Please try again.")

        module.grades.append(Grade(grade_name, percentage_weight, actual_percentage))
        total_percentage -= percentage_weight

    clear()
    total = 0

    # calculate total grade
    for grade in module.grades:
        total += (grade.percentage_weight / 100) * grade.actual_percentage

    # print out data
    print("-----------------------------------------------------------------------------------")
    print("You have achieved " + str(total) + "% for " + module.name)
    print("-----------------------------------------------------------------------------------")

    for grade in module.grades:
        print(f"{grade.grade_name}: Scored - {grade.actual_percentage}% | Weight on module - {grade.percentage_weight}%")

    print("-----------------------------------------------------------------------------------")
    exit = input("Press any key to exit...")
    
