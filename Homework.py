def calculate(cost, paid):
    change = paid - cost
    return change

howmuch = float(input("How much was item: "))
howmuchpay = float(input("How much did you pay: "))

if howmuchpay < howmuch:
    print("You did not pay enough")
else:
    changeleft = calculate(howmuch, howmuchpay)
    print("the change they have to give you back is", changeleft)
