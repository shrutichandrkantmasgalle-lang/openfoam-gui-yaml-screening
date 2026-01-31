from binary_tree import BinaryTree
from yaml_handler import write_yaml

tree = BinaryTree()
for val in [10, 5, 15, 3, 7]:
    tree.insert(val)

tree_dict = tree.to_dict(tree.root)
write_yaml(tree_dict, "../sample_data/tree_data.yaml")
