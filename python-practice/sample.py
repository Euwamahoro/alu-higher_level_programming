#!/usr/bin/python3
def calculate_carbon_emissions(activity):
    # Function to calculate carbon emissions based on the activity
    if activity == "1":
        return 2.5  # Sample carbon emissions for activity 1
    elif activity == "2":
        return 1.8  # Sample carbon emissions for activity 2
    elif activity == "3":
        return 0.5  # Sample carbon emissions for activity 3
    else:
        return 0.0  # Default value for invalid activity


def print_menu():
    # Function to print the menu options
    print("Menu:")
    print("1. Calculate carbon emissions for Activity 1")
    print("2. Calculate carbon emissions for Activity 2")
    print("3. Calculate carbon emissions for Activity 3")
    print("4. Quit")


# Main program
while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1" or choice == "2" or choice == "3":
        emissions = calculate_carbon_emissions(choice)
        print("Carbon emissions:", emissions, "tons")
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

