MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def calculate_money(q, d, n, p):
    money_input=(p*0.01)+(n*0.05)+(d*0.1)+(q*0.25)
    return money_input

def transaction(coffee, calculated_money):
    coffee_cost=MENU[coffee]["cost"]
    change=calculated_money-coffee_cost
    if change>0:
        print("Your change is $" + str(change))
        return True
    elif change<0:
        return False
    else:
        print("No exchange needed")
        return True

def check_resources(coffee):
    water=resources["water"]
    milk=resources["milk"]
    coffee_=resources["coffee"]
    req_water=MENU[coffee]["ingredients"]["water"]
    if "milk" in MENU[coffee]["ingredients"]:
        req_milk = MENU[coffee]["ingredients"]["milk"]
    req_coffee=MENU[coffee]["ingredients"]["coffee"]
    if water>=req_water:
        if "milk" in MENU[coffee]["ingredients"]:
            if milk>=req_milk:
                return True
            else:
                return "milk"
        else:
            return True
    else:
        return False

def add_money(coffee):
    resources["money"]+=MENU[coffee]["cost"]
    return True

def subtract_resources(coffee):
    resources["water"]-=MENU[coffee]["ingredients"]["water"]
    if "milk" in MENU[coffee]["ingredients"]:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"]-=MENU[coffee]["ingredients"]["coffee"]

def print_report():
    print(f"Water: {resources['water']}\n"
          f"Milk: {resources['milk']}\n"
          f"Coffee: {resources['coffee']}")

def coffee_machine():
    while True:
        coffee_choice = input("What coffee would you like? espresso/latte/cappuccino or watch a report: ").lower()
        if coffee_choice != "espresso" and coffee_choice != "cappuccino" and coffee_choice != "latte" and coffee_choice != "report":
            print("Incorrect input. Please try again.")
            continue
        if coffee_choice == "report":
            print_report()
            continue
        if check_resources(coffee_choice) == False:
            print("Sorry there is not enough resources")
            continue
        q = int(input("How many quarters? "))
        d = int(input("How many dimes? "))
        n = int(input("How many nickles? "))
        p = int(input("How many pennies? "))
        sum_calculated = calculate_money(q, d, n, p)
        if transaction(coffee_choice, sum_calculated) == False:
            print("Not enough money, money refunded")
            continue
        print(f"This is your {coffee_choice}")
        subtract_resources(coffee_choice)
        add_money(coffee_choice)

coffee_machine()

