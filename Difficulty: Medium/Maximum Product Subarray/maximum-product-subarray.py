class Solution:
	def maxProduct(self,arr):
		# code here
# 		n = len(arr)
# 		prod=[1]*n
		
# 		pivot = 0
# 		while pivot < n:
# 		    total_prd = 1
# 		    max_prd = float('-inf')
# 		    for i in range(pivot, n):
# 		        total_prd = total_prd*arr[i]
# 		        max_prd = max(total_prd, max_prd)
# 		    prod[pivot] = max_prd
# 		    pivot += 1
# 		return max(prod)


        if not arr:
            return 0

        n= len(arr)
        
        max_so = arr[0]
        min_end = arr[0]
        max_end = arr[0]
        
        for i in range(1,n):
            old_max = max_end
            
            max_end = max(arr[i], max_end*arr[i], min_end*arr[i])
            min_end = min(arr[i], min_end*arr[i], old_max*arr[i])
            
            max_so = max(max_so, max_end)
            
        return max_so