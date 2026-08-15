class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join(f'^{s}$')  
    
        n = len(T)
        P = [0] * n  
        center = 0
        right = 0
        max_len = 0
        max_center = 0
    
        for i in range(1, n - 1):
            mirror = 2 * center - i
            if i < right:
                P[i] = min(right - i, P[mirror])
    
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > right:
                center = i
                right = i + P[i]
            if P[i] > max_len:
                max_len = P[i]
                max_center = i
                
        start = (max_center - max_len) // 2
        return s[start:start + max_len]