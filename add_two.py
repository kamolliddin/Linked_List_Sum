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
