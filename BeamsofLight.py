N = input() # number of parking spots
L = input() # number of lights
Q = input() # number of parking spots you will be questioned about
Pi, Si = int(input().split(" "))


for Q in Pi:
    if Q in Pi + Si:
        print("Y")
    elif Q in Pi - Si:
        print("Y")
    else:
        print("N")
    