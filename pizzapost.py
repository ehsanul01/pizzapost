print("Thank you for choosing Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L")
Small=15
Middi=20
Large=25
pepforSmall=2
pepforMid=3
CheeforLarge=1

# What size pizza do you want? S, M, or L


# 🚨 Don't change the code above 👆
# Write your code below this line 👇
size = input("What size pizza do you want? S, M, or L")
if size == "S" or size =="s":
  add_pepperoni = input("Do you want pepperoni? Y or N")
  if add_pepperoni == "Y" or add_pepperoni=="y":
    smal=Small+pepforSmall
    extra_cheese = input("Do you want extra cheese? Y or N")
    if extra_cheese== "N" or extra_cheese=="n":
      print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is:{smal}")
    if extra_cheese== "Y" or extra_cheese=="y":
      k=smal+CheeforLarge
      print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {k}")
      
  else:
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is:{Small}")
    
if size == "M" or size =="m":
  add_pepperoni = input("Do you want pepperoni? Y or N")
  if add_pepperoni == "Y" or add_pepperoni=="y":
    smali=Middi+pepforMid
    extra_cheese = input("Do you want extra cheese? Y or N")
    if extra_cheese== "N" or extra_cheese=="n":
      print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: {smali}")
    if extra_cheese== "Y" or extra_cheese=="y":
      ki=smali+CheeforLarge
      print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {ki}")
      
  else:
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {Middi}")
    
if size == "L" or size =="l":
  add_pepperoni = input("Do you want pepperoni? Y or N")
  if add_pepperoni == "Y" or add_pepperoni=="y":
    sma=Large+pepforMid
    extra_cheese = input("Do you want extra cheese? Y or N")
    if extra_cheese== "N" or extra_cheese=="n":
      print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {sma}")
    if extra_cheese== "Y" or extra_cheese=="y":
      kia=sma+CheeforLarge
      print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {kia}")
      
  else:
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is:{Middi}")  
 
  
  
