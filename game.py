# Enter the code here
# Aaryan Batra
def select_options():
    # List of 10 options of fighters that the user can pick from
    options = ["Fighter 1", "Fighter 2", "Fighter 3", "Fighter 4", "Fighter 5", 
               "Fighter 6", "Fighter 7", "Fighter 8", "Fighter 9", "Fighter 10"]
    
    print("Select 5 options from the list:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    selected = []
    selection = False
    
    while not selection:
        print("\nEnter 5 numbers between 1-10, separated by spaces:")
        user_input = input("> ")
        choices = user_input.split()
        
        # Makes sure that there are only 5 options selected
        if len(choices) != 5:
            print(f"Please select exactly 5 options. You entered {len(choices)}.")
            continue
        
        # Try to convert all inputs to integers
        valid_numbers = True
        numbers = []
        for choice in choices:
            if not choice.isdigit():
                valid_numbers = False
                break
            numbers.append(int(choice))
        
        if not valid_numbers:
            print("Please enter only numbers.")
            continue
        
        # Double check to make sure the user entered numbers within the range
        if any(num < 1 or num > 10 for num in numbers):
            print("All numbers must be between 1 and 10.")
            continue
        
        # Check to see if the user selected any duplicates 
        if len(set(numbers)) != 5:
            print("Please select 5 different options (no duplicates).")
            continue
        
        # All validation passed, get the selected options
        selected = [options[num-1] for num in numbers]
        selection = True
    
    print("\nYour selections:")
    for option in selected:
        print(f"- {option}")
    
    return selected

if __name__ == "__main__":
    select_options()
# Adithya Menon
# Mehret Berihun
# Joshua Koroma
