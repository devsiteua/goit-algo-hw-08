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


def find_min_value(root):
    if root is None:
        return None

    current = root

    while current.left is not None:
        current = current.left

    return current.val


def build_tree(values):
    if not values:
        return None

    root = Node(values[0])

    for value in values[1:]:
        root = insert(root, value)

    return root


def run_tests():
    root = build_tree([10, 5, 15, 2, 7, 20])
    assert find_min_value(root) == 2

    root = build_tree([5])
    assert find_min_value(root) == 5

    root = build_tree([10, 8, 6, 4, 2])
    assert find_min_value(root) == 2

    root = build_tree([])
    assert find_min_value(root) is None


if __name__ == "__main__":
    run_tests()

    root = build_tree([10, 5, 15, 2, 7, 20])

    print("Task 1")
    print("Minimum value:", find_min_value(root))
