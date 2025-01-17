import os
print("Welcome to the secret auction program. ")

bidders_List = {}






#screen clears then next bidder

#compare all bids to find highest bid and winner
def silent_auction():
    while True:    
        name_bidder = input("What is your name?: ")
        amount_bid = int(input("What is your bid?: "))
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        bidders_List.update({name_bidder:amount_bid})
        if other_bidders == "yes":
            os.system('clear')
            name_bidder = input("What is your name?: ")
            amount_bid = int(input("What is your bid?: "))
            other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
            bidders_List.update({name_bidder:amount_bid})
        elif other_bidders == "no":
            break
        
    max_bid = max(bidders_List, key=bidders_List.get)
    max_value = bidders_List[max_bid]
    print(max_value)   
    
    #print(f"the winner is {} with a bid of ${}. ")
    
silent_auction()