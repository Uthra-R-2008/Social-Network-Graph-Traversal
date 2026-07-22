# Social-Network-Graph-Traversal

📌 Graph Traversal using DFS and BFS in Python

A simple Python project that demonstrates Depth First Search (DFS) and Breadth First Search (BFS) traversal on a graph using an adjacency list representation.

This project is designed to help beginners understand how graph traversal algorithms work and the difference between DFS and BFS.

🚀 Features
Represents a graph using a Python dictionary (Adjacency List)
Performs Depth First Search (DFS) recursively
Performs Breadth First Search (BFS) using a queue
Displays the traversal order for both algorithms
Beginner-friendly implementation

📂 Project Structure
Graph-Traversal/
│
├── graph_traversal.py
├── README.md
└── output.png

🛠️ Technologies Used
Python 3
Lists
Dictionaries
Recursion
Queue (using Python List)
📖 Graph Used
        A
      /   \
     B     C
    / \     \
   D   E-----F

Adjacency List:

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
▶️ Output
DFS Traversal:
A B D E F C

BFS Traversal:
A B C D E F

🧠 Concepts Covered
Graph Data Structure
Adjacency List Representation
Depth First Search (DFS)
Breadth First Search (BFS)
Recursion
Queue Operations
Traversal Algorithms

📚 Learning Outcomes

Through this project, I learned:

How graphs are represented using dictionaries.
The difference between DFS and BFS traversal.
How recursion is used in DFS.
How queues are used to implement BFS.
How graph traversal is useful in solving real-world problems like route finding, networking, and social media connections.

💡 Future Improvements
Accept graph input from the user
Visualize graph traversal
Implement iterative DFS
Add weighted graph support
Find shortest path using BFS
Implement Dijkstra's Algorithm
