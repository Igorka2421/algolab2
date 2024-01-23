import unittest

from task3 import BinaryTree, branchSums


class TestBinaryTree(unittest.TestCase):

    def test_branchSums(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        result = branchSums(root)
        self.assertEqual(result, 24, "Expected 24 but got {0}".format(result))


if __name__ == "__main__":
    unittest.main()
