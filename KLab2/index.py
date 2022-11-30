item = [ {"name": 'Bike', "price":100}, {"name": 'TV', "price":200}, {"name": 'Album', "price":10}, {"name": 'Book', "price":5}, {"name": 'Phone', "price":500}, {"name": 'Computer', "price":1000}, ]

# 1 . Filter and show the product that will be bought when you don't have much money I mean Cheap one

# Step1: is to find expensive product which will help us to get cheapest product
expensive = 0
for prix in item:
    if prix['price']>expensive:
        expensive = prix['price']
    else:
        continue
cheap = expensive
for pri in item:
    if pri['price']<cheap:
        cheap = pri['price']
    else:
        continue
print(f'Cheapest product is:',cheap)


# 2 . Filter and show the product that will be expensive in the array

expensive = 0
for prixe in item:
    if prixe['price']>expensive:
        expensive = prixe['price']
    else:
        continue
print(f'The Expensive product Cost:',expensive)

# 3 . Calculate the full price of all product combined

sum = 0
for index in item:
    sum += index['price']
print(f'Full price of All products combined is:', sum)

# 4 . Calculate the full price of all product combined and remove product that are under the 10 dollar
sum = 0
for x in item:
    if x['price']<10:
        continue
    else:
        sum = sum + x['price']
print(f'Price of all product combined except ones whose price is under 10 USD',sum)