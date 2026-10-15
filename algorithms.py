"""
algorithms.py

Manual implementations of:
- Dijkstra's algorithm (for weighted shortest-distance path)
- BFS (for fewest-edge path in an unweighted sense)

Each function returns:
- path (list of node names) or None if no path
- additional metrics (distance or edge count)
- execution time in seconds
"""

import heapq
import time
from collections import deque

def dijkstra(adjacency, start, goal):
    """
    adjacency: dict[node] = list of (neighbor, weight)
    start, goal: node names (strings)

    Returns (path, total_distance, elapsed_time)
    - path: list of nodes from start to goal (inclusive) or None if unreachable
    - total_distance: sum of weights along path (float) or None
    - elapsed_time: seconds taken (float)
    """
    t0 = time.time()

    # Validate nodes
    if start not in adjacency or goal not in adjacency:
        return None, None, 0.0

    # Initialize distances and parent pointers
    dist = {node: float("inf") for node in adjacency}
    parent = {node: None for node in adjacency}
    dist[start] = 0

    # Min-heap priority queue: (distance, node)
    heap = [(0, start)]
    visited = set()

    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        # Early exit if we reached the goal
        if node == goal:
            break

        for neighbor, weight in adjacency[node]:
            # Ensure non-negative weights (Dijkstra requirement)
            if weight < 0:
                # Skip negative edges for safety (illustration only)
                continue
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    # Reconstruct path
    if dist[goal] == float("inf"):
        t1 = time.time()
        return None, None, t1 - t0

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    t1 = time.time()
    return path, dist[goal], t1 - t0

def bfs(adjacency, start, goal):
    """
    adjacency: dict[node] = list of (neighbor, weight) -- weights ignored for BFS
    start, goal: node names

    Returns (path, edge_count, elapsed_time)
    - path: list of nodes from start to goal (inclusive) or None if unreachable
    - edge_count: number of edges traversed in the path (int) or None
    - elapsed_time: seconds taken (float)
    """
    t0 = time.time()

    if start not in adjacency or goal not in adjacency:
        return None, None, 0.0

    visited = set([start])
    parent = {start: None}
    q = deque([start])

    found = False
    while q:
        node = q.popleft()
        if node == goal:
            found = True
            break
        for neighbor, _ in adjacency[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                q.append(neighbor)

    if not found:
        t1 = time.time()
        return None, None, t1 - t0

    # Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    edge_count = max(0, len(path) - 1)

    t1 = time.time()
    return path, edge_count, t1 - t0
