weight= float(input("How much does your package weigh?"))

#Ground shipping
if weight <= 2:
  cost_ground=(weight*1.50+20)
elif weight <=6:
  cost_ground=(weight*3.00+20)
elif weight <=10:
  cost_ground=(weight*4.00+20)
else:
  cost_ground=(weight*4.75+20)
print("Ground Shipping: $", '%.2f'%cost_ground)

#Premium Ground Shipping
cost_ground_premium = 125.00
print("Premium Ground Shipping: $", '%.2f'%cost_ground_premium)

#Drone Shipping
if weight <= 2:
  drone_cost=(weight*4.50)
elif weight <=6:
  drone_cost=(weight*9.00)
elif weight <=10:
  drone_cost=(weight*12.00)
else:
  drone_cost=(weight*14.25)
print("Drone Shipping: $", '%.2f'%drone_cost)