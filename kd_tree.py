# Function to insert a node into a KD tree
def insert(root, filename, point, depth=0):
    # If the current node is None, create a new node with the given filename and point
    if root is None:
        return {'filename': filename, 'point': point, 'left': None, 'right': None}
    
    # Calculate the dimensionality of the point
    k = len(point)
    # Determine which axis to compare based on the current depth
    axis = depth % k
    
    # If the point's coordinate along the current axis is less than or equal to the current node's coordinate,
    # recursively insert into the left subtree; otherwise, insert into the right subtree
    if point[axis] <= root['point'][axis]:
        root['left'] = insert(root['left'], filename, point, depth + 1)
    else:
        root['right'] = insert(root['right'], filename, point, depth + 1)
    
    # Return the modified root node
    return root


# Function to find the inorder successor (the node with the smallest value in the subtree)
def minValueNode(node):
    current = node
    
    # Traverse to the leftmost node to find the smallest value
    while current['left'] is not None:
        current = current['left']
    
    return current


# Function to delete a node from the KD tree
def deleteNode(root, point, depth=0):
    # If the root is None, return None
    if root is None:
        return root

    # Calculate the dimensionality of the point
    k = len(point)
    # Determine which axis to compare based on the current depth
    axis = depth % k

    # Recursively traverse the tree to find the node to be deleted
    if point[axis] < root['point'][axis]:
        root['left'] = deleteNode(root['left'], point, depth + 1)
    elif point[axis] > root['point'][axis]:
        root['right'] = deleteNode(root['right'], point, depth + 1)
    else:
        # If the node to be deleted has no children, return None
        if root['left'] is None and root['right'] is None:
            return None
        # If the node has only one child, return that child
        if root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        else:
            # If the node has both children, find the inorder successor,
            # replace the node's value with the successor's value, and delete the successor
            if point[0] == root['point'][0] and point[1] == root['point'][1] and point[2] == root['point'][2]:
                temp = minValueNode(root['right'])
                root['point'] = temp['point']
                root['filename'] = temp['filename']
                root['right'] = deleteNode(root['right'], temp['point'], depth + 1)
            else:
                # Otherwise, continue the deletion process recursively
                if point[axis] < root['point'][axis]:
                    root['left'] = deleteNode(root['left'], point, depth + 1)
                elif point[axis] > root['point'][axis]:
                    root['right'] = deleteNode(root['right'], point, depth + 1)

    # Return the modified root node
    return root
