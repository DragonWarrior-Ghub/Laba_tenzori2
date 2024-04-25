import random
class TreeNode:
    def __init__(self, value, num_children=0):
        self.value = value
        self.children = []
        self.num_children = num_children

    def equals(self, other):
        if other is None:
            return False
        flag = True
        if len(self.children) == len(other.children):
            for i in range(len(self.children)):
                equals = self.children[i].equals(other.children[i])
                if not equals:
                    flag = False
        else:
            flag = False
        return flag


def generate_tree_from_file(filename):
    with open(filename, 'r') as file:
        structure = [int(num) for num in file.read().split()]

    if not structure:
        return None

    nodes = {0: TreeNode(0)}
    next_value = 1
    parent_value = 0

    for num_children in structure:
        nodes[parent_value].num_children = num_children
        for _ in range(num_children):
            nodes[next_value] = TreeNode(next_value)
            nodes[parent_value].children.append(nodes[next_value])
            next_value += 1
        parent_value += 1

    return nodes[0]


def find_subtrees(root, subtree_structure_root):
        def dfs(node: TreeNode):
            if node is None:
                return []
            result = []
            if node.equals(subtree_structure_root):
                result.append(node)
            for child in node.children:
                result.extend(dfs(child))
            return result

        return dfs(root)


def print_tree_vertical(root, prefix='', is_last=True):
    print(prefix + ("└── " if is_last else "├── ") + str(root.value))
    children_count = len(root.children)
    for i, child in enumerate(root.children):
        is_last_child = i == children_count - 1
        print_tree_vertical(child, prefix + ("    " if is_last else "│   "), is_last_child)

def generate_tree_structure():
    n = int(input('Введите кол-во узлов в дереве: '))
    if n <= 0:
        return []

    # Используем случайные числа для определения количества дочерних узлов каждого узла
    tree_structure = [random.randint(0, min(n - 1, 5)) for _ in range(n)]

    # Записываем массив tree_structure в файл
    with open("tree_structure.txt", "w") as file:
        file.write(" ".join(map(str, tree_structure)))

    return tree_structure


if int(input('Введите 1, если нужно сгенерировать новое дерево: ')) == 1:
    generate_tree_structure()
    tree = generate_tree_from_file('tree_structure.txt')
else:
    tree = generate_tree_from_file('tree_structure.txt')

print("Изначальнео деерво")
print_tree_vertical(tree)


print("Структура поиска")
subtree = generate_tree_from_file('subtree_structure.txt')
print_tree_vertical(subtree)


print("Найденные поддеревья")
for stree in find_subtrees(tree, subtree):
    print_tree_vertical(stree)
