# College Campus Navigation System

A beginner-friendly DAA (Design and Analysis of Algorithms) project demonstrating:
- Dijkstra's Algorithm (shortest path in a weighted graph)
- Breadth-First Search (BFS) (fewest-edges path in an unweighted sense)

This Streamlit app visualizes a sample college campus graph and lets users find routes, compare algorithms, and view performance metrics.

---

## Contents / Files

- `app.py` — Streamlit interface and page navigation.
- `algorithms.py` — Manual implementations of Dijkstra and BFS.
- `campus_graph.py` — Sample campus locations, edges, and weights.
- `visualization.py` — Functions to draw the campus graph and highlight routes.
- `requirements.txt` — Python package requirements.
- `README.md` — This file.
- `.gitignore` — Files/folders to exclude from Git.

---

## Sample Campus Map (illustrative)
Nodes:
- Main Gate, Library, Canteen, Computer Lab, Science Block, Administration Block, Auditorium, Parking Area, Sports Ground, Hostel

Edges have sample distances in meters (the map and distances are illustrative and not actual campus measurements).

---

## Algorithms (short descriptions)

### Dijkstra's Algorithm
- Uses a weighted adjacency list.
- Initializes the source distance to 0 and others to infinity.
- Uses a min-heap (priority queue) to always pick the unvisited node with smallest known distance.
- Updates neighboring distances when a shorter route is found.
- Reconstructs the shortest path using parent pointers.
- Requires non-negative edge weights.

Time complexity (with binary heap): O((V + E) log V)

### Breadth-First Search (BFS)
- Uses a queue and a visited set.
- Explores neighbors level by level.
- Uses parent pointers to reconstruct a path.
- Returns a path with the fewest edges (not necessarily the shortest distance when weights differ).

Time complexity: O(V + E)

---

## How to run locally

1. Clone or create the project folder:
   - Create a new folder `college-campus-navigation` and save the project files there.

2. Create and activate a Python virtual environment (recommended):
   - On macOS / Linux:
     python3 -m venv venv
     source venv/bin/activate
   - On Windows (PowerShell):
     python -m venv venv
     .\venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run app.py

---

## How to use

- Open the app in the browser (Streamlit prints the local URL).
- Use the "Find Route" page to pick a Start and Destination.
- Click "Find shortest route (Dijkstra)" for minimum-distance path.
- Click "Find route (BFS)" for fewest-edge path.
- View the route highlighted on the map and see the route details and timing.
- Reset to clear previous results.

---

## Example output
- Visual map with nodes and edge distances labeled (in meters).
- Highlighted route (red edges and pink nodes) after running an algorithm.
- Route details: node sequence, total distance (for Dijkstra), number of edges (for BFS), execution time.

---

## Screenshots
Add screenshots by saving images and linking or embedding them in this README. Example Markdown:
````markdown
![Map screenshot](screenshots/map.png)
