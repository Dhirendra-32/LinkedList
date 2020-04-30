# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = n = ListNode(0)
        carr = 0
        while (l1 or l2 or carr):
            totalSum = 0
            if l1:
                totalSum = l1.val
                l1 = l1.next
            if l2:
                totalSum = l2.val
                l2 = l2.next
            totalSum += carr
            carr, rem = divmod(totalSum, 10)
            n.next = ListNode(rem)
            n = n.next
        return root.next


# object creation start from here
print(" start analying from here ")
AddTwo = Solution()

