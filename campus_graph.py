"""
campus_graph.py

Defines the sample campus graph:
- node list
- weighted edges (distances in meters)
- adjacency list for algorithm use
- NetworkX graph and fixed positions for visualization

The map and distances are illustrative (not actual campus measurements).
"""

import networkx as nx

def get_sample_campus():
    # Node names (at least 10)
    nodes = [
        "Main Gate",
        "Library",
        "Canteen",
        "Computer Lab",
        "Science Block",
        "Administration Block",
        "Auditorium",
        "Parking Area",
        "Sports Ground",
        "Hostel",
    ]

    # Weighted edges (undirected) - sample distances in meters
    # Format: (node1, node2, distance)
    edges = [
        ("Main Gate", "Library", 120),
        ("Main Gate", "Administration Block", 200),
        ("Main Gate", "Parking Area", 80),
        ("Library", "Computer Lab", 60),
        ("Library", "Canteen", 150),
        ("Computer Lab", "Science Block", 100),
        ("Science Block", "Auditorium", 140),
        ("Administration Block", "Auditorium", 120),
        ("Canteen", "Sports Ground", 90),
        ("Parking Area", "Sports Ground", 200),
        ("Hostel", "Canteen", 180),
        ("Hostel", "Parking Area", 160),
        ("Hostel", "Science Block", 220),
        ("Parking Area", "Administration Block", 250),
        ("Sports Ground", "Auditorium", 300),
    ]

    # Build adjacency list for algorithm usage: dict[node] = list of (neighbor, weight)
    adjacency = {node: [] for node in nodes}
    for u, v, w in edges:
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))  # undirected

    # Build NetworkX graph for visualization and verification
    G = nx.Graph()
    G.add_nodes_from(nodes)
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Fixed positions (x, y) for stable visualization layout
    pos = {
        "Main Gate": (0, 0),
        "Library": (1, 1.5),
        "Computer Lab": (2.2, 1.3),
        "Science Block": (3.5, 1.0),
        "Auditorium": (4.8, 0.8),
        "Administration Block": (2.0, -0.8),
        "Canteen": (1.6, 0.0),
        "Parking Area": (-0.8, -0.6),
        "Sports Ground": (3.2, -1.6),
        "Hostel": (0.5, -1.8),
    }

    return nodes, adjacency, G, pos
