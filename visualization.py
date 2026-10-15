"""
visualization.py

Functions to draw the campus graph and highlight routes using Matplotlib and NetworkX.
"""

import matplotlib.pyplot as plt
import networkx as nx

def draw_campus(G, pos, path=None, title="Campus Map", figsize=(8,6)):
    """
    G: networkx.Graph with 'weight' attributes on edges
    pos: dict of node positions
    path: list of node names (optional)
    Returns a Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title, fontsize=12)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="#87CEEB", ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif", ax=ax)

    # Draw all edges normally
    default_edges = [e for e in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=default_edges, width=1.5, edge_color="#777777", ax=ax)

    # Draw edge weight labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    formatted_labels = {k: f"{v}m" for k,v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_labels, font_color="black", font_size=8, ax=ax)

    # If a path is provided, highlight it
    if path and len(path) >= 2:
        # Build list of edges in path
        path_edges = list(zip(path[:-1], path[1:]))
        # Highlight path edges
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3.5, edge_color="red", ax=ax)
        # Highlight path nodes
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_size=800, node_color="#FFB6C1", ax=ax)

    # Legend (simple)
    ax.plot([], [], color="#FFB6C1", marker='o', linestyle='', label='Selected route nodes')
    ax.plot([], [], color="red", linewidth=3.5, label='Selected route edges')
    ax.plot([], [], color="#87CEEB", marker='o', linestyle='', label='Campus locations')
    ax.legend(loc='upper left', fontsize=8)

    plt.axis('off')
    plt.tight_layout()
    return fig
