menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):

    print('Calculating bill subtotal...')
    
    ### WRITE SOLUTION HERE
    count = 0
    for item in order:
        count += float(item['price'])
    return round(count,2)      

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE  
    return round((float(subtotal)* 0.15), 2)    

def summarize_order(order):
    names = list()
    total = 0
    for item in order:
        names.append(item['name'])
        total += float(item['price']) + float(item['price'])*0.15

    return names, total

    
    

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------To finish print 'done'")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    while True:
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        if item == 'done':
            return order
        elif not(item.isnumeric()) or int(item) not in range(1,6):
            print("Choose between(1~5)")
            continue
        count += 1
        order.append(menu[int(item)])

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    print('summery:')
    print('---------')
    items, subtotal = summarize_order(order)
    d = dict()
    for name in items:
        if name not in d:
            d[name] = d.get(name, 0) + 1
        else:
            d[name] = d[name]+1
    res = [*set(items)]
    for item in res:
        print(item, f'({d[item]})')
    print('---------')
    print(f"Total: {subtotal}")


if __name__ == "__main__":
    main()
