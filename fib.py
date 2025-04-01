# top - down 

n = 5
dp = [-1] * (n+1)


def fib(n,dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    
    dp[n] = fib(n-1,dp) + fib(n-2, dp)
    return dp[n]

print("fib :",fib(n,dp))

# bottom up 

f = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    f[i] = f[i-1] + f[i-2]

print("fib :",dp[n])    