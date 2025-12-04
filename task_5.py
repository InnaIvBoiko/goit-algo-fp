from typing import Optional, List, Deque
from collections import deque

import matplotlib.pyplot as plt

from task_4 import Node, draw_tree


def generate_color_gradient(
    total_nodes: int, 
    start_hex: str = "#0036A0", 
    end_hex: str = "#AADDFF"
) -> List[str]:
    """
    Generate a list of colors from dark to light shades using linear interpolation.
    
    Parameters
    ----------
    total_nodes : int
        Number of nodes for which colors need to be generated.
    start_hex : str
        Starting color in hex RGB format (dark), e.g. "#001133".
    end_hex : str
        Ending color in hex RGB format (light), e.g. "#AADDFF".
        
    Returns
    -------
    List[str]
        List of hexadecimal color codes from dark to light.
    """
    if total_nodes <= 0:
        return []
    
    # Convert hex to RGB
    start_hex = start_hex.lstrip("#")
    end_hex = end_hex.lstrip("#")
    
    start_r = int(start_hex[0:2], 16)
    start_g = int(start_hex[2:4], 16) 
    start_b = int(start_hex[4:6], 16)
    
    end_r = int(end_hex[0:2], 16)
    end_g = int(end_hex[2:4], 16)
    end_b = int(end_hex[4:6], 16)
    
    colors = []
    for i in range(total_nodes):
        # Linear interpolation factor from 0 (dark) to 1 (light)
        t = i / max(total_nodes - 1, 1)
        
        r = int(start_r + (end_r - start_r) * t)
        g = int(start_g + (end_g - start_g) * t)
        b = int(start_b + (end_b - start_b) * t)
        
        color = f"#{r:02X}{g:02X}{b:02X}"
        colors.append(color)
    
    return colors


def dfs_traversal(root: Optional[Node]) -> List[Node]:
    """
    Perform depth-first search traversal using a stack.
    
    Parameters
    ----------
    root : Node
        Root node of the binary tree.
        
    Returns
    -------
    List[Node]
        List of nodes in DFS order.
    """
    if not root:
        return []
    
    visited = []
    stack = [root]
    
    while stack:
        current = stack.pop()  # Remove from the end (stack behavior)
        visited.append(current)
        
        # Add children to stack (right first, then left)
        # This ensures left child is processed first when popped
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return visited


def bfs_traversal(root: Optional[Node]) -> List[Node]:
    """
    Perform breadth-first search traversal using a queue.
    
    Parameters
    ----------
    root : Node
        Root node of the binary tree.
        
    Returns
    -------
    List[Node]
        List of nodes in BFS order.
    """
    if not root:
        return []
    
    visited = []
    queue: Deque[Node] = deque([root])
    
    while queue:
        current = queue.popleft()  # Remove from the front (queue behavior)
        visited.append(current)
        
        # Add children to queue (left first, then right)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return visited


def visualize_dfs(root: Node) -> None:
    """
    Visualize depth-first search traversal with color gradient.
    
    Parameters
    ----------
    root : Node
        Root node of the binary tree.
    """
    # Get DFS traversal order
    dfs_order = dfs_traversal(root)
    
    # Generate color gradient
    colors = generate_color_gradient(len(dfs_order))
    
    # Assign colors to nodes based on DFS order
    for i, node in enumerate(dfs_order):
        node.color = colors[i]
    
    # Draw the tree with DFS colors
    draw_tree(root, "Depth-First Search (DFS) Traversal")


def visualize_bfs(root: Node) -> None:
    """
    Visualize breadth-first search traversal with color gradient.
    
    Parameters
    ----------
    root : Node
        Root node of the binary tree.
    """
    # Get BFS traversal order
    bfs_order = bfs_traversal(root)
    
    # Generate color gradient
    colors = generate_color_gradient(len(bfs_order))
    
    # Assign colors to nodes based on BFS order
    for i, node in enumerate(bfs_order):
        node.color = colors[i]
    
    # Draw the tree with BFS colors
    draw_tree(root, "Breadth-First Search (BFS) Traversal")


def create_sample_tree() -> Node:
    """
    Create a sample binary tree for demonstration.
    
    Returns
    -------
    Node
        Root node of the created binary tree.
    """
    # Create nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    return root


def reset_node_colors(root: Node, default_color: str = "skyblue") -> None:
    """
    Reset all node colors to default color.
    
    Parameters
    ----------
    root : Node
        Root node of the binary tree.
    default_color : str
        Default color to set for all nodes.
    """
    if not root:
        return
    
    stack = [root]
    while stack:
        current = stack.pop()
        current.color = default_color
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


if __name__ == "__main__":
    # Create a sample binary tree
    tree_root = create_sample_tree()
    
    # Visualize DFS traversal
    print("Visualizing DFS and BFS traversal...")
    
    visualize_dfs(tree_root)
    reset_node_colors(tree_root)
    visualize_bfs(tree_root)
    
    # Print traversal orders for verification
    reset_node_colors(tree_root)
    dfs_nodes = dfs_traversal(tree_root)
    bfs_nodes = bfs_traversal(tree_root)
    
    print(f"\nDFS order: {[node.val for node in dfs_nodes]}")
    print(f"BFS order: {[node.val for node in bfs_nodes]}")
    print()
