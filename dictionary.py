print("Welcome to the secret auction program.")
import art
print(art.logo)
def result(bidding):
    winning_bid = 0 
    winner = {}
    for bid in bidding:
        bid_amount = int(bidding[bid])
        if(bid_amount > winning_bid):
            winning_bid = bid_amount
            winner = bid

    print(f"The winner is {winner} with bid amount of {winning_bid}.")    
dictionary = {}
while True:
    name = input("What is your name?\n")
    bid = input("What's is the bid?\n")
    dictionary[name] = bid
    verify = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if(verify == 'yes'):
        continue
    else:
        result(dictionary)
        break



