def maxprofit(stock_prices):
    max_profit = 0
    for initial_buy in range(len(stock_prices)-1):
        current = stock_prices[initial_buy]
        profit = 0
        for i in range(initial_buy+1,len(stock_prices)):
            #look for potential buy option if next price is higher
            if current is None:
                try:
                    if stock_prices[i+1] > stock_prices[i]:
                        current = stock_prices[i]
                # try/except handles out of range error when at end of the list
                except:
                    pass

            # sell when high
            elif stock_prices[i]>current:
                profit += stock_prices[i]-current
                current = None
                try:
                    if stock_prices[i+1]>stock_prices[i]:
                        current = stock_prices[i]
                except:
                    pass

        max_profit = max(max_profit,profit)
    return(max_profit)

print(maxprofit([7,1,5,3,6,4]))
print(maxprofit([1,2,3,4,5]))
print(maxprofit([7,6,4,3,1]))
print(maxprofit([0,1,0,1,0,1]))
print(maxprofit([4,7,1,0,1]))