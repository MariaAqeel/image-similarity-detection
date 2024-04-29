
def insert(root, filename, point, depth=0):
    if root is None:
        return {'filename': filename, 'point': point, 'left': None, 'right': None}
    
    k = len(point)
    axis = depth % k
    
    if point[axis] < root['point'][axis]:
        root['left'] = insert(root['left'], filename, point, depth + 1)
    else:
        root['right'] = insert(root['right'], filename, point, depth + 1)
    
    return root




# Find the inorder successor
def minValueNode(node):
    current = node
    
    while current['left'] is not None:
        current = current['left']
    
    return current


# Deleting a node
def deleteNode(root, point, depth=0):
    if root is None:
        return root

    k = len(point)
    axis = depth % k

    if point[axis] < root['point'][axis]:
        root['left'] = deleteNode(root['left'], point, depth + 1)
    elif point[axis] > root['point'][axis]:
        root['right'] = deleteNode(root['right'], point, depth + 1)
    else:
        if root['left'] is None and root['right'] is None:
            return None
        if root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        else:
            temp = minValueNode(root['right'])
            root['point'] = temp['point']
            root['filename'] = temp['filename']
            root['right'] = deleteNode(root['right'], temp['point'], depth + 1)

    return root




# def write_kd_tree_to_file(kd_tree, file_path):
#     with open(file_path, 'w') as f:
#         # Use a recursive function to write the kd-tree structure
#         def write_node(root, indent=0):
#             if root is None:
#                 return
            
#             # Write current root's data (point and filename)
#             f.write(' ' * indent + f"point: {root['point']}, filename: '{root['filename']}'\n")
            
#             # Recursively write left and right subtrees
#             write_node(root['left'], indent + 2)
#             write_node(root['right'], indent + 2)
        
#         # Start writing from the root root
#         write_node(kd_tree)

# # Example usage to write the kd-tree to a text file
# kd_tree = {...}  # Your kd-tree dictionary
# file_path = 'kd_tree.txt'
# write_kd_tree_to_file(kd_tree, file_path)


