from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True
money: int = 0
while is_on:
    options = menu.get_items()
    users_choice = input(f"What would you like? {options}: ").lower()
    if users_choice == "off":
        is_on = False
    elif users_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(users_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) :
            coffee_maker.make_coffee(drink)