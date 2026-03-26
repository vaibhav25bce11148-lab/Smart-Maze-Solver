# Smart Maze Solver: An Exploration of Uninformed Search
**Course:** Fundamentals of AIML (Vityarthi)  
**Project Type:** Bring Your Own Project (BYOP)  
**Language:** Python  

## 📌 Project Overview
This project is a terminal-based maze solver that demonstrates how an artificial intelligence agent navigates a constrained environment to find an exit. Instead of relying on random guessing or trial-and-error, the system uses a systematic, logic-based search algorithm to guarantee that it will find the absolute shortest path from the start point (`S`) to the end point (`E`).

## 🧠 The AIML Concept: Breadth-First Search (BFS)
For this Fundamentals of AIML project, I chose to implement **Breadth-First Search (BFS)**. This is a classic "uninformed" or "blind" state-space search algorithm. 

I selected BFS over other algorithms like Depth-First Search (DFS) because of its mathematical properties. BFS explores the maze by expanding outwards in all possible directions simultaneously (like a ripple in water). Because it checks all paths that are 1 step away, then all paths that are 2 steps away, and so on, it mathematically guarantees that the first path it finds to the exit is the shortest possible route.

### How the Agent "Thinks"
The AI relies on three main data structures to solve the puzzle without getting stuck in infinite loops:
1. **The Grid (Environment):** The maze is represented as a 2D array (list of lists) where `#` acts as a wall and `.` is an open path.
2. **The Queue (Frontier):** The AI uses a double-ended queue (`collections.deque`) to keep track of which coordinates to explore next. It operates on a First-In-First-Out (FIFO) basis.
3. **The Visited Set (Memory):** To prevent the AI from pacing back and forth between the same two empty squares forever, it logs every coordinate it steps on into a Python `set`. Before making a move, it checks this memory bank.

## 🚀 How to Run the Project
This project relies entirely on standard Python data structures and requires no external machine learning libraries.

1. Ensure Python 3.x is installed on your machine.
2. Download or clone the `maze_solver.py` file.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the file and run the following command:
   ```bash
   python Vityarthi project.py
5. The terminal will print the unsolved maze, process the BFS algorithm, and then print the solved maze with the optimal path     marked by * characters.

## 🔮 Future Improvements
If I were to expand on this project, the next logical step would be to upgrade the uninformed BFS algorithm to an informed search algorithm like A (A-Star)*. By adding a heuristic (like calculating the Manhattan distance to the exit), the AI could prioritize moving toward the exit rather than exploring dead-end paths in the opposite direction, making it much more computationally efficient on massive mazes.