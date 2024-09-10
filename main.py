MENU={
    "boost":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "whey":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5
    },
    "mass_gainer":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":30,
        },
        "cost":3,
    }

}
profit=0

resources={
    "water":300,
    "milk":200,
    "coffee":100,
}
def is_resources_enough(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}")
            is_enough=False
        return is_enough
def process_coins():
    print("plese insert coins.")
    total=int(input('how many quarters:'))*0.25
    total+=int(input('how many dines:'))*0.1
    total+=int(input('how many nickles:'))*0.05
    total+=int(input('how many pennis:'))*0.01
    return total
def is_transaction_sucess(money_recived,drink_cost):
    if money_recived>=drink_cost:
        global profit
        profit+=drink_cost
        change=round(money_recived-drink_cost,2)
        print(f"here is ur ${change} change")
        return True
    else:
        print("sorry money is not suffecient .Money refunded ")
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f'here is your {drink_name}')
is_on=True
while is_on:
    choise=input("what would you like?(boost/whey/mass_gainer):")
    if choise=="off":
        is_on=False
    elif choise=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink=MENU[choise]
        if is_resources_enough(drink['ingredients']):
            payment=process_coins()
            if is_transaction_sucess(payment,drink['cost']):
                make_coffee(choise,drink['ingredients'])





