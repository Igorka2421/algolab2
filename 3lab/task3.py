class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSumsRec(root, isLeft, summ):
    if root is None:
        return

    if root.left is None and root.right is None and isLeft == True:
        summ[0] += root.value

    branchSumsRec(root.left, 1, summ)
    branchSumsRec(root.right, 0, summ)


def branchSums(root):
    summ = [0]

    branchSumsRec(root, 0, summ)

    return summ[0]
