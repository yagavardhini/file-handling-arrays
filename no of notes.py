amount=int(input("enter the amount:"))
notes=[10,20,50,100,200,500]
notecount=[0,0,0,0,0,0]
print("currency count")
for x,y in zip(notes,notecount):
    if amount >=x:
        y=amount//x
        amount=amount-y*x
        print(x,":",y)
