class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def sum_tree_values(root):
    if root is None:
        return 0

    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)


def build_tree(values):
    if not values:
        return None

    root = Node(values[0])

    for value in values[1:]:
        root = insert(root, value)

    return root


def run_tests():
    root = build_tree([10, 5, 15, 2, 7, 20])
    assert sum_tree_values(root) == 59

    root = build_tree([5])
    assert sum_tree_values(root) == 5

    root = build_tree([])
    assert sum_tree_values(root) == 0

    root = build_tree([1, 2, 3, 4])
    assert sum_tree_values(root) == 10


if __name__ == "__main__":
    run_tests()

    root = build_tree([10, 5, 15, 2, 7, 20])

    print("Task 2")
    print("Sum of all values:", sum_tree_values(root))
