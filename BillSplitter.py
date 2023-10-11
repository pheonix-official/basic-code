def split_bill():
    try:
        total_cost = float(input("Enter the total cost of the bill: "))
        num_people = int(input("Enter the number of people: "))
        
        if total_cost <= 0 or num_people <= 0:
            print("Total cost or number of people must be greater than zero.")
            return
        
        each_share = total_cost / num_people
        
        
        people = []
        for i in range(num_people):
            person_name = input(f"Enter the name of person {i + 1}: ")
            people.append(person_name)
        
        for person in people:
           print(f"{person} need to pay {each_share:.2f}")
           
    except ValueError:
        print("Invalid input. Please enter valid numbers for total cost , number of people, and amounts paid.")

split_bill()
