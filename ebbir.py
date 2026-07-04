class PaymentSystem:
    def __init__(self):
        self.accounts = {
            "Ali": {
                "password": "1234",
                "balance": 500.00
            },
            "Ahmed": {
                "password": "5678",
                "balance": 200.00
            },
            "Ayan": {
                "password": "1111",
                "balance": 800.00
            },
            "Hassan": {
                "password": "2222",
                "balance": 1000.00
            },
            "Fatima": {
                "password": "3333",
                "balance": 350.00
            }
        }

    # Login
    def login(self):
        name = input("Geli magaca account-ka: ")
        password = input("Geli Password-ka: ")

        if name in self.accounts:
            if self.accounts[name]["password"] == password:
                print(f"\nSoo dhawoow {name}")
                return name
            else:
                print("Password khaldan.")
        else:
            print("Account lama helin.")

        return None

    # Hubi Balance
    def show_balance(self, user):
        print(f"Balance-kaagu waa: {self.accounts[user]['balance']} ETB")

    # Dir Lacag
    def send_money(self, sender):
        receiver = input("Geli magaca qofka lacagta loo dirayo: ")

        if receiver not in self.accounts:
            print("Account-ka qofka lama helin.")
            return

        try:
            amount = float(input("Geli lacagta (ETB): "))
        except ValueError:
            print("Fadlan geli lacag sax ah.")
            return

        if amount <= 0:
            print("Lacagtu waa inay ka weyn tahay 0.")
            return

        if self.accounts[sender]["balance"] >= amount:
            self.accounts[sender]["balance"] -= amount
            self.accounts[receiver]["balance"] += amount

            print("\nLacagta waa la diray.")
            print(f"Waxaad dirtay {amount} ETB -> {receiver}")
            print(f"Balance-kaaga cusub: {self.accounts[sender]['balance']} ETB")
        else:
            print("Balance kuma filna.")

    # Lacag Ku Shubo
    def deposit(self, user):
        try:
            amount = float(input("Geli lacagta aad shubaneyso (ETB): "))
        except ValueError:
            print("Fadlan geli lacag sax ah.")
            return

        if amount > 0:
            self.accounts[user]["balance"] += amount
            print("Lacagta waa lagu daray.")
            print(f"Balance-kaaga cusub: {self.accounts[user]['balance']} ETB")
        else:
            print("Lacag khaldan.")

    # Beddel Password
    def change_password(self, user):
        old = input("Geli password-kii hore: ")

        if old == self.accounts[user]["password"]:
            new = input("Geli password cusub: ")
            self.accounts[user]["password"] = new
            print("Password waa la beddelay.")
        else:
            print("Password-kii hore waa khaldan.")


# Samee object
ps = PaymentSystem()

# USSD Code
code = input("Fadlan geli code-ka: ")

if code == "*841#":

    user = ps.login()

    if user:

        while True:

            print("\n===== Ebbir Payment =====")
            print("1. Hubi Balance")
            print("2. Dir Lacag")
            print("3. Lacag Ku Shubo")
            print("4. Beddel Password")
            print("5. Ka Bax")

            choice = input("Dooro: ")

            if choice == "1":
                ps.show_balance(user)

            elif choice == "2":
                ps.send_money(user)

            elif choice == "3":
                ps.deposit(user)

            elif choice == "4":
                ps.change_password(user)

            elif choice == "5":
                print("Mahadsanid. Waad baxday.")
                break

            else:
                print("Doorasho khaldan.")

else:
    print("Code-ka aad gelisay waa khaldan.")