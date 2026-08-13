class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        dp=[0]*(n+1)
        if n == 0:
            return 0
        elif n==1:
            return 1
        
        dp[0]=0
        dp[1]=1
            
        idx=2
        while idx <= n:
           dp[idx] = dp[idx - 1] + dp[idx - 2]
           idx+=1
           
        return dp[n]
