class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ret = ListNode(-1)
        temp = ret
        while l1 or l2 or carry:
            cur = carry
            if l1:
                cur += l1.val
            if l2:
                cur += l2.val
            if cur >= 10:
                carry = 1
                cur %= 10
            else:
                carry = 0
            temp.next = ListNode(cur)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ret.next
