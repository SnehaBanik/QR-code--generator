menu={
    "Pizza":50,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffe":80
}
print("Welcome to our resturant")
print("Pizza:Rs 50\n Pasta:Rs 50\n Burger:Rs 60\n Salad:Rs 70\n Coffe:Rs 80")
order_total= 0

item_1=input("Enter the item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Your item {item_1} is not available yet")
another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of the second item= ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
         print(f"Ordered item {item_1} is not available yet")
         
print(f"The total amount of items to pay is {order_total}")