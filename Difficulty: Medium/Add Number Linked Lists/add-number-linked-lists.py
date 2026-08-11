class Solution:
    def addTwoLists(self, head1, head2):
        # Reverse both lists to process from least significant digit
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Reverse both input lists
        head1 = reverse(head1)
        head2 = reverse(head2)
        
        # Add digit by digit with carry
        dummy = Node(0)
        curr = dummy
        carry = 0
        
        while head1 or head2 or carry:
            sum_val = carry
            
            if head1:
                sum_val += head1.data
                head1 = head1.next
            if head2:
                sum_val += head2.data
                head2 = head2.next
            
            carry = sum_val // 10
            digit = sum_val % 10
            
            curr.next = Node(digit)
            curr = curr.next
        
        # Reverse the result back to correct order
        result = reverse(dummy.next)
        
        # Remove leading zeros (keep at least one node)
        while result and result.next and result.data == 0:
            result = result.next
        
        return result