cap = 7
n = 5
wt_list = [3,4,6,2,11]
val_list = [100,300,250,400,150]

def knapsack(n,cap,wt_list,val_list):
   dp = {}
   def get_max_value(n,cap):
       if n == 0 or cap == 0:
        return 0
       elif (n,cap) in dp:
          return dp[(n,cap)]
       else:
          curr_wt = wt_list[n-1]
          curr_val = val_list[n-1]
          if curr_wt <= cap:
             c1 = curr_val + get_max_value(n-1,cap-curr_wt)
             c2 = get_max_value(n-1,cap)

             c = max(c1,c2)
          else:
             c = get_max_value(n-1,cap)
          dp[(n,cap)] = c
          return c
   max_profit = get_max_value(n,cap)
   return max_profit
print(knapsack(n,cap,wt_list,val_list))      


arr = [5,6,3,4,1,0,2]
target = 50
0

def subset_sum(arr,target):
   n = len(arr)
   def solve(n,cap):
      if cap == 0:
         return True
      elif n == 0:
         return False
      else:
         curr_num = arr[n-1]
         if curr_num <= target:
            c1 = solve(n-1,cap-curr_num)
            c2 = solve(n-1,cap)

            return c1 or c2
   return solve(n,target)     


print(subset_sum(arr,target))
         
      
# dynamic Programming
# sorting
# Partition
# greedy Algorthim 

# 11
# [6,5,7,12]         
# [300,600,200]

# 0
# 600 + 300

# recursion
# 1. DP  - recusrion + memo
# 2. BT  - recursion + control
# 3. DAC

# fab(2) 





3, 11











