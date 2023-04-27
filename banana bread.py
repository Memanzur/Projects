# Define a function to handle order requests
def place_order():
    # Request customer information
    name = input("Please enter your name: ")
    contact_info = input("Please enter your phone number or email address: ")
    
    # Request order details
    while True:
        quantity = input("How many banana bread pieces would you like to order? (Enter a number or 'pack of 4'): ")
        if quantity == "pack of 4":
            break
        elif quantity.isdigit():
            break
        else:
            print("Invalid input. Please enter a number or 'pack of 4'.")
    
    if quantity == "pack of 4":
        while True:
            flavor_option = input("Would you like all pieces to be the same flavor? (Enter 'yes' or 'no'): ")
            if flavor_option == "yes" or flavor_option == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if flavor_option == "yes":
            while True:
                flavor_choice = input("Which flavor would you like? (Enter 'plain', 'chocolate chip', 'nut', or 'both'): ")
                if flavor_choice in ['plain', 'chocolate chip', 'nut', 'both']:
                    break
                else:
                    print("Invalid input. Please enter 'plain', 'chocolate chip', 'nut', or 'both'.")
            order_details = {"pack of 4": {"flavor": flavor_choice}}
        else:
            order_details = {"pack of 4": {"flavors": []}}
            for i in range(4):
                while True:
                    flavor_choice = input("Which flavor would you like for piece {}? (Enter 'plain', 'chocolate chip', 'nut', or 'both'): ".format(i+1))
                    if flavor_choice in ['plain', 'chocolate chip', 'nut', 'both']:
                        break
                    else:
                        print("Invalid input. Please enter 'plain', 'chocolate chip', 'nut', or 'both'.")
                order_details["pack of 4"]["flavors"].append(flavor_choice)
    else:
        order_details = {"individual pieces": []}
        for i in range(int(quantity)):
            while True:
                flavor_choice = input("Which flavor would you like for piece {}? (Enter 'plain', 'chocolate chip', 'nut', or 'both'): ".format(i+1))
                if flavor_choice in ['plain', 'chocolate chip', 'nut', 'both']:
                    break
                else:
                    print("Invalid input. Please enter 'plain', 'chocolate chip', 'nut', or 'both'.")
            order_details["individual pieces"].append({"number": i+1, "flavor": flavor_choice})
    
    # Calculate total cost of order
    # Assuming base cost of $2.79 per mix, $4.79 per cup of chocolate chips, and $0.69 per banana
    total_cost = 0
   
