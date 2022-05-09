x = range(20)
for y in x:
    if y%3 ==0 and y%2 ==0:
        print(f"{y} is divisible by both 2 and 3")
    elif y%2 ==0:
        print(f"{y} is divisible by 2")
    elif y%3 ==0:
        print(f"{y} is divisible by 3")
  
    else:
        print(f"{y} is not divisible by 2 or 3")