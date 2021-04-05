class Banking:
    def __init__(user):
        uname = str(input("Please Enter your Username: "))
        user.balance = 0
        print(f"Welcome {uname} to Banking Application")

    def deposit(user):
        amount = float(input("Enter amount to be Deposited: "))
        user.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(user):
        amount = float(input("Enter amount to be Withdrawn: "))
        if user.balance >= amount:
            user.balance -= amount
            print("\n You Withdrew: ", amount)
        else:
            print("\n Insufficient balance")

    def display(user):
        print("\n Net Available Balance = ", user.balance)


account = Banking()
account.deposit()
account.withdraw()
account.display()
