name =input("May I have your name please ? ")
print("Hello",name, "Welcome to the Airport")

Ticket_price = 25000
Seat = 3
is_available = True

print("Okay! here is your data!")
print(Ticket_price)
print(Seat)
print(is_available)

print(type(Ticket_price))
print(type(Seat))
print(type(is_available))

total = Ticket_price * Seat
print("So, that will get us to...")
print(Ticket_price * Seat)
print("And that will be :", total)
sale_price = Ticket_price - 0.25
print("And after discount, its :", Ticket_price)

price1= 400
price2= 300
print("before", price1, "and", price2)
bucket=price1
price1= price2
price2= bucket
print("after", price1, "and", price2)