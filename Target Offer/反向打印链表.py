'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        result =[]
        if listNode == None:
            return result
        head = listNode
        while head:
            result.insert(0,head.val)
            head = head.next
        return result

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
