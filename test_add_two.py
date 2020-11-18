from add_two import *
import unittest

inputs_for_list1 = [
    [0],
    [2, 4, 3],
    [9, 9, 9, 9, 9, 9, 9],
    [5],
    [2, 4, 3, 1, 3, 5, 6],
    [2, 4, 3]
]
inputs_for_list2 = [
    [0],
    [5, 6, 4],
    [9, 9, 9, 9],
    [5],
    [5, 6, 4],
    [5, 6, 4, 1, 3, 5, 6]
]
expected_outputs = [
    [0],
    [7, 0, 8],
    [8, 9, 9, 9, 0, 0, 0, 1],
    [0, 1],
    [7, 0, 8, 1, 3, 5, 6],
    [7, 0, 8, 1, 3, 5, 6]
]


class TestAddTwo(unittest.TestCase):
    # Test for correct results
    def test_sum(self):
        for i in range(len(inputs_for_list1)):
            l1 = LinkedList.build_linked_list(inputs_for_list1[i])
            l2 = LinkedList.build_linked_list(inputs_for_list2[i])
            expected_sum = LinkedList.build_linked_list(expected_outputs[i])
            self.assertAlmostEqual(LinkedList.get_elements(
                addTwoNumbers(l1, l2)), LinkedList.get_elements(expected_sum))
