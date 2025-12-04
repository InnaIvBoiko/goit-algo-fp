import uuid
from typing import Optional, Dict, Tuple, List, Any, Union

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key: Any, color: str = "skyblue") -> None:
        """Binary tree node used for visualization."""
        self.left: Optional["Node"] = None  # Can be Node or None
        self.right: Optional["Node"] = None  # Can be Node or None
        self.val = key
        self.color = color  # Additional argument to store the node's color
        self.id = str(uuid.uuid4())  # Unique identifier for each node


def add_edges(
    graph: nx.DiGraph, 
    node: Optional[Node], 
    pos: Dict[str, Tuple[float, float]], 
    x: float = 0, 
    y: float = 0, 
    layer: int = 1
) -> nx.DiGraph:
    """
    Recursively add nodes and edges of the binary tree to the graph.

    Parameters
    ----------
    graph : nx.DiGraph
        Graph to which nodes and edges are added.
    node : Node
        Current node of the binary tree.
    pos : dict
        Dictionary with positions of nodes for drawing.
    x, y : float
        Coordinates of the current node.
    layer : int
        Current depth in the tree, used to spread nodes horizontally.
    """
    if node is None:
        return graph
        
    graph.add_node(node.id, color=node.color, label=node.val)
    pos[node.id] = (x, y)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        left_x = x - 1 / 2 ** layer
        pos[node.left.id] = (left_x, y - 1)
        add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / 2 ** layer
        pos[node.right.id] = (right_x, y - 1)
        add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root: Node, title: str ) -> None:
    """
    Draw a binary tree starting from the given root node.

    Parameters
    ----------
    tree_root : Node
        Root node of the binary tree.
    title : str
        Title for the visualization plot.
    """
    tree = nx.DiGraph()
    pos: Dict[str, Tuple[float, float]] = {tree_root.id: (0.0, 0.0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    plt.title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def sift_down(array: List[Any], index: int, size: int) -> None:
    """
    Helper function to restore min-heap property by sifting a value down.

    Parameters
    ----------
    array : list
        List representation of a heap.
    index : int
        Current index to sift down from.
    size : int
        Number of elements in the heap.
    """
    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and array[left] < array[smallest]:
            smallest = left
        if right < size and array[right] < array[smallest]:
            smallest = right

        if smallest == index:
            break

        array[index], array[smallest] = array[smallest], array[index]
        index = smallest


def heapify_min(array: List[Any]) -> None:
    """
    Transform a list into a min-heap in-place.

    Parameters
    ----------
    array : list
        List to be transformed into a min-heap.
    """
    size = len(array)
    # Start from the last non-leaf node and sift down to the root
    for index in range(size // 2 - 1, -1, -1):
        sift_down(array, index, size)


def visualize_binary_heap(heap: List[Any], title: str = "Binary Heap Visualization") -> None:
    """
    Build a binary tree from a binary heap and visualize it.

    The input list is first transformed into a min-heap (heapify),
    then converted into a binary tree structure for visualization.

    For index i in the heap array:
        left child index = 2 * i + 1
        right child index = 2 * i + 2

    Parameters
    ----------
    heap : list
        List representation of a binary heap (not necessarily valid yet).
    title : str
        Title for the visualization plot.
    """
    if not heap:
        return

    # Work on a copy so the original list is not modified
    heap_array = list(heap)
    heapify_min(heap_array)

    # Create Node instances for each heap element
    nodes = [Node(value) for value in heap_array]

    # Link nodes according to binary heap array relationships
    for index, node in enumerate(nodes):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    # The root of the heap is the first element after heapify
    root = nodes[0]
    draw_tree(root, title=title)

    
if __name__ == "__main__":
    arr1 = [4, 10, 3, 5, 1]
    visualize_binary_heap(arr1, "Example 1: Simple Array [4, 10, 3, 5, 1]")

    arr2 = [1, 3, 6, 5, 2, 4, 8, 7]
    visualize_binary_heap(arr2, "Example 2: Larger Array [1, 3, 6, 5, 2, 4, 8, 7]")

    arr3 = [1, 2, 3, 4, 5, 6, 7]
    visualize_binary_heap(arr3, "Example 3: Already Sorted Array [1, 2, 3, 4, 5, 6, 7]")
