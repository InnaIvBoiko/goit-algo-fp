import heapq
from typing import Dict, Union


def dijkstra_with_heap(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, Union[int, float]]:
    """
    Implementation of Dijkstra's algorithm using binary heap for shortest path calculation.
    
    Args:
        graph: Dictionary representing weighted graph where keys are vertices 
               and values are dictionaries of adjacent vertices with weights
        start: Starting vertex for shortest path calculation
    
    Returns:
        Dictionary with shortest distances from start vertex to all other vertices
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    
    visited: set[str] = set()
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
            
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            # Skip if neighbor already visited
            if neighbor in visited:
                continue
                
            new_distance = current_distance + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances


def create_sample_graph() -> Dict[str, Dict[str, int]]:
    """
    Create sample weighted graph for testing Dijkstra's algorithm.
    
    Returns:
        Dictionary representing weighted graph
    """
    return {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }


def test_dijkstra() -> None:
    """Test cases demonstrating Dijkstra's algorithm functionality."""
    
    # Create test graph
    graph = create_sample_graph()
    
    # Test shortest paths from vertex A
    result_a = dijkstra_with_heap(graph, 'A')
    print("\nShortest paths from vertex A:")
    for vertex, distance in result_a.items():
        print(f"  A -> {vertex}: {distance}")
    
    # Test shortest paths from vertex E
    result_e = dijkstra_with_heap(graph, 'E')
    print("\nShortest paths from vertex E:")
    for vertex, distance in result_e.items():
        print(f"  E -> {vertex}: {distance}")


if __name__ == "__main__":
    test_dijkstra()
    print()