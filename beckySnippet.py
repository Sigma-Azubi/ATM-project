GST = 0.05
HST = 0.13
PST = 0.06


country = input("What country do you come from? : ").upper()

ordertotal = float(input("What is your order tottal amount? : "))

orderwithtaxes = 0.0


if country == "KENYA":
    province = input("Which province do you come from? : ").upper()
    if country == "NAKURU":
        orderwithtaxes = GST * ordertotal + (ordertotal)
        print(orderwithtaxes)
    elif country == "NAIROBI" or "KISUMU" or "TURKANA":
        orderwithtaxes = HST* ordertotal + (ordertotal)
        print(f"The order total with taxes is : {orderwithtaxes}")
    else:
        orderwithtaxes = (PST + GST) * ordertotal + (ordertotal)
        print(orderwithtaxes)
else:
    orderwithtaxes = ordertotal
    print(orderwithtaxes)