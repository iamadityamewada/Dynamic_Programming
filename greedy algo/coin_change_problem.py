coins = [1,2,5,10,20,50,100,500,2000]
amount = 10000

def coin_change(coin,amount):
    coin.sort(reverse = True)
    result = []
    for coin in coins:
        while coin <= amount:
            amount-=coin
            result.append(coin)
        if amount ==0:
            break
    return result, len(result)

print(coin_change(coins,amount))        