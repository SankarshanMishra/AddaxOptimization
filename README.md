# 🐫 Addax Optimization Algorithm (AOA)

This repository implements the **Addax Optimization Algorithm (AOA)** in Python — a nature-inspired metaheuristic technique used for solving numerical optimization problems. The algorithm mimics the foraging and digging behavior of the endangered Addax antelope.

## 🚀 Features

- Implementation of both **exploration (foraging)** and **exploitation (digging)** phases.
- Configurable population size, dimension, and search space bounds.
- Demonstrated using the **Sphere function** as the objective.
- Simple and modular code structure.

## 📌 Objective Function

The default objective is the **Sphere function**:

```python
f(x) = sum(x_i² for i in range(dimension))
A classic test function for evaluating optimization algorithms — the goal is to minimize it.

🧠 How AOA Works
Initialization: Randomly generate an initial population of solutions.

Foraging Phase: Explore the search space by moving towards the best solution so far.

Digging Phase: Exploit the search space by introducing fine variations.

Selection: Replace existing solutions with better ones.

Update Best: Track the best solution found over time.
 Requirements
Python 3.x

NumPy

Install dependencies (if needed):

bash
Copy
Edit
pip install numpy
Output
The script returns:

Best solution vector (array)

Best fitness value (scalar)

These values represent the most optimal point found during the search process.

📜 License
This project is open-source and available under the MIT License.

💡 Future Work
Add benchmarking against other algorithms (GA, PSO, etc.)

Visualize convergence over iterations

Create a GUI interface or web dashboard

🙌 Contributions
Feel free to fork, open issues, or submit pull requests!

🐪 Inspired by Nature — Powered by Code.
yaml
Copy
Edit
