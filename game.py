import random

x = random.randint(1, 50)
print(x)
for i in range(5):
    y = int(input("請猜一個數字:"))
    if x == y:
        print("猜對了!")
        print(f"這是第{i+1}次猜對")
        break
    else:
        if x > y:
            print("猜高一點!!")
        else:
            print("猜低一點!!")
if x != y:
    print(f"答案為:{x}")
