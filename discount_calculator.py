purchase_amount = float(input("Enter the amount of your purchase."))

if purchase_amount >= 1000:
    discount = 0.1
elif purchase_amount >= 500:
    discount = 0.05
else:
    discount = 0

final_price = purchase_amount*(1-discount)
print(f"The final price after discount is {final_price}")