B = int(input()) # number of tickets Besa wants to buy
T = int(input()) # total number of tickets for the concert
P = int(input()) # number of tickets other people have purchased

avaTck =  T - P
remTck = avaTck - B

if avaTck >= B:
    print(f"Y {remTck}")
else:
    print("N")


        