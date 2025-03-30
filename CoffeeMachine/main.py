from menu import MENU

#initial resources
water = 300
milk = 200
coffee = 100
money = 0

# coins
quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01


def report():
    """Return current resource values."""
    print(f"Water: {water}ml "
          f"\nMilk: {milk}ml"
          f"\nCoffee: {coffee}g"
          f"\nMoney: ${money}")


def pour(user_input):
    """Reduce resources based on the selected drink."""
    global water, milk, coffee

    ingredients = MENU[user_input]["ingredients"]
    water -= ingredients["water"]
    coffee -= ingredients["coffee"]

    if "milk" in ingredients:
        milk -= ingredients["milk"]


def enough(user_input):
    """checks if resources are enough"""
    global water, milk, coffee
    ingredients = MENU[user_input]["ingredients"]

    if water < ingredients["water"]:
        print("Sorry there is not enough water.")
        return False
    elif coffee < ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif "milk" in ingredients and milk < ingredients["milk"]:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True

def update_coins(user_input):
    """Handles coin input and checks if the payment is sufficient."""
    global money
    print("Kindly, insert coins...")
    quarters_inserted = int(input("How many quarters? "))
    dimes_inserted = int(input("How many dimes? "))
    nickels_inserted = int(input("How many nickels? "))
    pennies_inserted = int(input("How many pennies? "))

    payment = (quarters * quarters_inserted) + (dimes * dimes_inserted) + (nickels * nickels_inserted) + (pennies * pennies_inserted)

    if MENU[user_input]["cost"] > payment:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if payment > MENU[user_input]["cost"]:
        change = payment - MENU[user_input]["cost"]
        rounded_change = round(change, 2)
        print(f"Here is {rounded_change} dollars in change.")

    money += MENU[user_input]["cost"]

    return True


while True:
    prompt = input("What would you like? (latte/espresso/cappuccino): ").lower()

    if prompt == "report":
        report()
    elif prompt in MENU:
        if enough(prompt):
            if update_coins(prompt):
                pour(prompt)
                print(f"Here is your {prompt}. Enjoy!")
    elif prompt == "off":
        print("Turning off the coffee machine.")
        break
    else:
        print("Invalid input. Please choose a valid option.")
















