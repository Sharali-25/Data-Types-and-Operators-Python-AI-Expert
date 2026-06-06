snack_name = "Imarti"
price = 5.25
quantitiy = 25
is_avaliable = True

print(snack_name)
print(price)
print(quantitiy)
print(is_avaliable)

print(type(is_avaliable))
print(type(snack_name))
print(type(quantitiy))
print(type(price))

total= quantitiy * price
print(quantitiy * price)
print("The total is :", total)
sale_price = price - 0.25
print("After discount it's :", sale_price)

print("is price under $2 ?", price<2)
print("If the quantity more than five ?", quantitiy>5)
print("Is price exactly $1.50 ?", price== 1.50)

shop_name = "mota" + "  " +  "lala"
print("shop name =",shop_name)
print(len(snack_name))
print("first Letter", snack_name[0])

price1=50
price2=60
print("before", price1, "and", price2)
bucket=price1 
price1=price2
price2=bucket
print("after", price1, "and", price2)
