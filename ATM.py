
balance = 1000  
transactions = []  

def display_balance():
    print(f"\nYour current balance is: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ₹{amount}")
        print("Deposit successful!")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: ₹{amount}")
        print("Withdrawal successful!")

def show_statement():
    print("\n--- Transaction Statement ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)
    print("-----------------------------")

def atm_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

atm_menu()