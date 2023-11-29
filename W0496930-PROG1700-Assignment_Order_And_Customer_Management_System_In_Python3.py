#Author: William Taylor      
#Student ID: W0496930      
#Course: PROG1700
#Date: 11/29/23
#Project: W0496930-PROG1700-Assignment_Order_And_Customer_Management_System_In_Python3
#Repository:https://github.com/W0496930/PROG1700-Algorithms
#Programming language: Python 3

#Setup the data for the program
customers = {'name': 'Will', 
            'contact': '19025550000', 
            'orders': [{'order_id': 1, 
            'product_name': 'Bananas', 
            'quantity': 2, 
            'total_cost': 10.0}, 
            {'order_id': 2, 
            'product_name': 'Apples', 
            'quantity': 2, 
            'total_cost': 2.0}]}

#Define the function to add a new customer
def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter contact number: ")
    customer_id = len(customers) + 1
    orders = []
    customer_data = {'name': name, 'contact': contact, 'orders': orders}
    customers[customer_id] = customer_data
    print(f"Customer {name} added successfully with ID {customer_id}")

#Define the function to place an order within the program
def place_order(customer_id, product_name, quantity, unit_price):
    #Validate input
    if customer_id not in customers:
        print("Error: Customer not found.")
        return

    #Generate the order id
    order_id = len(customers[customer_id]['orders']) + 1

    #Calculate the cost
    total_cost = quantity * unit_price

    #Create an order dictionary
    order_data = {
        'order_id': order_id,
        'product_name': product_name,
        'quantity': quantity,
        'total_cost': total_cost
    }

    #Add the order to the customer's orders list and print a message if the order is placed succesfully
    customers[customer_id]['orders'].append(order_data)
    print(f"Order placed successfully for customer {customer_id}, order ID: {order_id}")

#Function to create the customer report
def generate_customer_report(customer_id):
    #Validate input
    if customer_id not in customers:
        print("Error: Customer not found.")
        return
    
    customer_data = customers[customer_id]

    #Display all of the customer contact details
    print("\nCustomer Report:")
    print(f"Customer ID: {customer_id}")
    print(f"Name: {customer_data['name']}")
    print(f"Contact: {customer_data['contact']}")

    #Calculate the cost of the order
    total_spending = sum(order['total_cost'] for order in customer_data['orders'])
    print(f"Total Spending: ${total_spending:.2f}")

    #Display orders
    if customer_data['orders']:
        print("\nOrders:")
        for order in customer_data['orders']:
            print(f"Order ID: {order['order_id']} | Product: {order['product_name']} | Quantity: {order['quantity']} | Total Cost: ${order['total_cost']:.2f}")
    else:
        print("No orders for this customer.")
    print("End of Customer Report")

#Function to generate all of the reports
def generate_all_reports():
    #Validate Input
    if not customers:
        print("No customers to generate reports for.")
        return
    #Display all of the reports
    print("\nGenerating Reports for All Customers:")    
    for customer_id, customer_data in customers.items():
        generate_customer_report(customer_id)    
    print("End of All Customer Reports")

#Menu
def display_menu():
    print("\nOrder and Customer Management System Menu:")
    print("1. Add Customer")
    print("2. Place Order")
    print("3. Generate Customer Report")
    print("4. Generate All Customer Reports")
    print("5. Exit")

#Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_customer()
    elif choice == '2':
        customer_id = int(input("Enter Customer ID: "))
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        unit_price = float(input("Enter Unit Price: "))
        place_order(customer_id, product_name, quantity, unit_price)
    elif choice == '3':
        customer_id = int(input("Enter Customer ID: "))
        generate_customer_report(customer_id)
    elif choice == '4':
        generate_all_reports()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
