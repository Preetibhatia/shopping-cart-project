#shopping_cart.py

import datetime
import statistics
time = datetime.datetime.now()

#TODO covert to CSV
#send receipt via email

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


#create a list to input items from user till they enter Done

id_input=None
price=None
no_items=0
total_list=len(products)
price=[]
customer_list =[]
Tax=[]


while(str(id_input)!='DONE'):
    id_input=input("Please enter the product id: ")
    i=0
    found=False

    while(i<total_list):

        if (id_input)==str(products[i]['id']):
            found=True
            customer_list.append(products[i])
            break
        i=i+1
    if str(id_input)=='DONE':
        break
    elif found==False:
        print("Hey, are you sure that product identifier is correct? Please try again!")

#print the reciept
customer_product_count = len(customer_list)

print ("---------------------------------------------")
print ("PREETI'S GROCERY STORE")
print ("WWW.PREETIGROCERYSTORE.COM")
print ("---------------------------------------------")
print ("CHECKOUT AT:"+ str(time))
print ("---------------------------------------------")
print("You selected " +str(customer_product_count) +" PRODUCTS:")

for p in customer_list:
   price_usd = "(${0:.2f})".format(p["price"])
   print ("....... " + p["name"] + " " + price_usd )
print ("---------------------------------------------")

for p in customer_list:
    price.append(p['price'])
    Tax.append(p['price']*0.0875)
Total_price = "${0:.2f}".format(sum(price))
Total_Tax =  "${0:.2f}".format(sum(Tax))
#Total =  "${0:.2f}".format(sum(int (Total_price), int(Total_Tax)))
Total = "${0:.2f}".format(sum(price) + sum(Tax))

print("SUBTOTAL: ", Total_price) 
print("TAX: ", Total_Tax) 
print("Total: ", Total) 

print ("---------------------------------------------")
print ("THANKS, SEE YOU AGAIN SOON!")
print ("---------------------------------------------")
