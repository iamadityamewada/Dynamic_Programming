capcity = 20
weight_list = [5,10,15,2]
value_list = [200,100,300,500]


def knapsack_fraction(cap,wt_list,val_list):
    data = []
    for i in range(len(wt_list)):
        dic = {
            "weight":wt_list[i],
            "price":val_list[i],
            "unit_price":val_list[i]/wt_list[i]
        }
        data.append(dic)
    
    data.sort(reverse= True, key = lambda x:x["unit_price"])
    total = 0
    for item in data:
        weight = item["weight"]
        price = item["price"]
        if weight <= cap:
            cap-=weight
            total+= price
        else:
            total += cap*item["unit_price"]
    return total
            

print(knapsack_fraction(capcity,weight_list,value_list))