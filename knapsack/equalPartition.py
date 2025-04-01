arr = [5,5,10,20,10]
target = 30

def equal_partition(arr,target):
    total = sum(arr)
    arr.sort(reverse = True)
    if total % 2 !=0:
        return False
    else:
        n = len(arr)
        def solve(n,cap):
            if cap ==0:
                return True
            elif n == 0:
                return False
            else:
                num = arr[n-1]
                if num <= cap:
                    c1 = solve(n-1,cap-num)
                    c2 = solve(n-1,cap)
                    return c1 or c2
                else:
                    return False
        return solve(n,target)

print(equal_partition(arr, target))        
