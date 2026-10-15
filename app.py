"""
app.py

Streamlit application for the College Campus Navigation System.
Pages:
- Home
- Find Route
- Campus Map
- Algorithm Analysis

Run:
streamlit run app.py
"""

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from campus_graph import get_sample_campus
from algorithms import dijkstra, bfs
from visualization import draw_campus
import time

# Page layout
st.set_page_config(page_title="College Campus Navigation System", layout="wide")

# Load data
nodes, adjacency, G, pos = get_sample_campus()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Find Route", "Campus Map", "Algorithm Analysis"])

# Initialize session state for results
if "last_path" not in st.session_state:
    st.session_state.last_path = None
if "last_algo" not in st.session_state:
    st.session_state.last_algo = None
if "last_metrics" not in st.session_state:
    st.session_state.last_metrics = {}

# Helper: reset results
def reset_results():
    st.session_state.last_path = None
    st.session_state.last_algo = None
    st.session_state.last_metrics = {}

# Home page
if page == "Home":
    st.title("College Campus Navigation System")
    st.markdown("""
    This project demonstrates two graph algorithms:
    - Dijkstra's Algorithm (shortest distance in a weighted graph)
    - Breadth-First Search (BFS) (fewest edges in an unweighted sense)
    
    Use the 'Find Route' page to select start and destination, run algorithms, and visualize routes.
    """)
    st.info("Note: The campus map and distances are illustrative and not actual campus measurements.")

# Find Route page
elif page == "Find Route":
    st.title("Find Route")
    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.subheader("Select locations")
        start = st.selectbox("Start", nodes, index=0)
        dest = st.selectbox("Destination", nodes, index=1)

        st.write("")  # spacing
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Find shortest route (Dijkstra)"):
                if start == dest:
                    st.warning("Start and destination are the same. Choose two different locations or use Reset.")
                else:
                    path, total_dist, elapsed = dijkstra(adjacency, start, dest)
                    if path is None:
                        st.error(f"No route found between {start} and {dest}.")
                        reset_results()
                    else:
                        st.success("Dijkstra route found.")
                        st.session_state.last_path = path
                        st.session_state.last_algo = "Dijkstra"
                        st.session_state.last_metrics = {
                            "distance_m": total_dist,
                            "time_s": elapsed,
                            "edges": len(path)-1
                        }
        with c2:
            if st.button("Find route (BFS)"):
                if start == dest:
                    st.warning("Start and destination are the same. Choose two different locations or use Reset.")
                else:
                    path, edge_count, elapsed = bfs(adjacency, start, dest)
                    if path is None:
                        st.error(f"No route found between {start} and {dest}.")
                        reset_results()
                    else:
                        st.success("BFS route found.")
                        st.session_state.last_path = path
                        st.session_state.last_algo = "BFS"
                        st.session_state.last_metrics = {
                            "distance_m": None,
                            "time_s": elapsed,
                            "edges": edge_count
                        }

        st.write("")  # spacing
        if st.button("Reset"):
            reset_results()
            st.experimental_rerun()

        st.markdown("---")
        st.subheader("Algorithm info")
        if st.session_state.last_algo == "Dijkstra":
            st.markdown("**Dijkstra's Algorithm**: Finds the path with the smallest total distance (weights). Uses a priority queue.")
        elif st.session_state.last_algo == "BFS":
            st.markdown("**Breadth-First Search (BFS)**: Finds a path with the fewest edges (weights ignored). Not always the shortest distance.")

    with col_right:
        st.subheader("Campus Map (visual)")
        if st.session_state.last_path is not None:
            fig = draw_campus(G, pos, path=st.session_state.last_path, title=f"Route highlighted ({st.session_state.last_algo})")
        else:
            fig = draw_campus(G, pos, path=None, title="Campus Map")
        st.pyplot(fig)

        st.subheader("Route details")
        if st.session_state.last_path:
            algo = st.session_state.last_algo
            metrics = st.session_state.last_metrics

            # Show metrics as cards
            m1, m2, m3 = st.columns(3)
            with m1:
                if metrics.get("distance_m") is not None:
                    st.metric("Total distance (m)", f"{metrics['distance_m']:.1f} m")
                else:
                    st.metric("Total distance (m)", "—")
            with m2:
                st.metric("Edges traversed", metrics.get("edges", "—"))
            with m3:
                st.metric("Execution time (s)", f"{metrics.get('time_s', 0):.6f}")

            st.markdown(f"**Algorithm:** {algo}")
            st.markdown(f"**Route:** {' → '.join(st.session_state.last_path)}")
            if algo == "BFS":
                st.info("Note: BFS finds a path with the fewest edges, which may not be the shortest distance when edge weights differ.")
        else:
            st.info("No route selected yet. Use the buttons to run Dijkstra or BFS.")

# Campus Map page
elif page == "Campus Map":
    st.title("Campus Map")
    st.markdown("Visual representation of campus locations and distances (labels show distances in meters).")
    st.pyplot(draw_campus(G, pos, path=None, title="Campus Map"))

    st.markdown("Nodes and edges:")
    st.write("Nodes:", nodes)
    st.write("Edges (node1, node2, distance in meters):")
    edges_list = [(u, v, d["weight"]) for u, v, d in G.edges(data=True)]
    st.write(edges_list)

# Algorithm Analysis page
elif page == "Algorithm Analysis":
    st.title("Algorithm Analysis and Performance")
    st.markdown("""
    This section explains theoretical complexity and measures execution time for the sample campus graph.
    The theoretical complexities used:
    - Dijkstra with binary heap and adjacency list: O((V + E) log V)
    - BFS with adjacency list: O(V + E)
    """)
    # Graph stats
    V = G.number_of_nodes()
    E = G.number_of_edges()
    st.write(f"Number of vertices (V): {V}")
    st.write(f"Number of edges (E): {E}")

    st.subheader("Measured execution times (average of repeated runs)")
    runs = st.slider("Number of runs to average", min_value=5, max_value=200, value=50, step=5)

    # We'll pick two sample nodes for measurement
    sample_start = "Main Gate"
    sample_goal = "Auditorium"

    # Time Dijkstra
    t0 = time.time()
    for _ in range(runs):
        _, _, _ = dijkstra(adjacency, sample_start, sample_goal)
    t1 = time.time()
    avg_dijkstra = (t1 - t0) / runs

    # Time BFS
    t0 = time.time()
    for _ in range(runs):
        _, _, _ = bfs(adjacency, sample_start, sample_goal)
    t1 = time.time()
    avg_bfs = (t1 - t0) / runs

    st.write(f"Average Dijkstra time: {avg_dijkstra:.6f} s")
    st.write(f"Average BFS time: {avg_bfs:.6f} s")

    st.markdown("""
    Notes:
    - On small graphs the absolute timings are illustrative only and do not indicate which algorithm is 'always' faster.
    - Dijkstra optimizes for total path distance (weights), while BFS optimizes for the fewest edges (ignores weights).
    """)

    st.subheader("Complexity summary")
    st.markdown("""
    - Dijkstra (with binary heap): O((V + E) log V)
    - BFS: O(V + E)
    """)
