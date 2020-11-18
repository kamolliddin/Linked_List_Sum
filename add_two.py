# Node implementation


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked list class implementation


class LinkedList:
    @classmethod
    # Build linked_list from given list of values
    def build_linked_list(self, values_list):
        number = None
        for value in values_list:
            if number == None:
                number = ListNode(value, None)
            else:
                self.get_last(number).next = ListNode(value, None)
        return number

    @classmethod
    # Get last element of linked list
    def get_last(self, ListNode):
        last = ListNode
        while (last.next):
            last = last.next
        return last

    @classmethod
    # Get numbers stored in linked list
    def get_elements(self, ListNode):
        values_list = []
        temp = ListNode
        while(temp):
            values_list.append(temp.val)
            temp = temp.next
        return values_list

# main function to add two linked list values


def addTwoNumbers(l1, l2):
    sum_list = None
    temp1 = l1
    temp2 = l2
    carry = 0
    last1 = None
    last2 = None

    while(temp1 or temp2):

        if temp1 == None:
            temp1 = ListNode(0, None)
        elif temp2 == None:
            temp2 = ListNode(0, None)

        val1 = temp1.val
        val2 = temp2.val
        sum1 = val1 + val2 + carry
        carry = sum1 // 10
        to_add = sum1 % 10

        if sum_list == None:
            sum_list = ListNode(to_add, None)
        else:
            LinkedList.get_last(sum_list).next = ListNode(to_add, None)

        last1 = temp1
        last2 = temp2

        temp1 = temp1.next
        temp2 = temp2.next

    if ((last1.val + last2.val + carry) >= 10) and carry > 0:
        LinkedList.get_last(sum_list).next = ListNode(carry, None)

    return sum_list
