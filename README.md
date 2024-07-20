# Percolation-Simulation

## Overview

This project provides a simulation of the Percolation Problem, where we determine the percentage of open squares required to achieve connectivity from the top to the bottom of a grid. This simulation uses a union-find data structure to manage connectivity and a custom bit array to track open/closed squares.

## Installation

Ensure you have Python and NumPy installed. If you don't have NumPy, you can install it using pip:

```bash
pip install numpy
```

## Files

- `percolation.py`: Contains the main code for the percolation simulation.
- `UnionFind.py`: Contains the union-find (disjoint-set) data structure implementation.
- `btds_bitarray.py`: Contains the custom bit array implementation.

## Usage

### Running the Simulation

1. Run the `percolation.py` script.
2. You will be prompted to enter the size of the board (n x n).
3. The script will simulate the percolation process, opening squares randomly until the top of the grid is connected to the bottom.
4. The script will output the percentage of squares opened to achieve percolation and the time taken for the simulation.

```bash
python percolation.py
```

### Example

```bash
size of board: 5
percentage of sq opened to get a connectivity from top to bottom:  52.0 time:  0.0026314258575439453
```

## Code Structure

### Board Class

The `Board` class manages the percolation grid and connectivity operations.

- **Attributes**:
  - `size`: The size of the grid.
  - `NoOfSqOpened`: The number of open squares.
  - `openclose`: A `btds_bitarray` instance to track open/closed squares.
  - `store`: A `UnionFind` instance to manage connectivity.

- **Methods**:
  - `__init__(self, n)`: Initializes the board with a given size.
  - `connect(self, p, q)`: Connects two squares if both are open.
  - `connected(self)`: Checks if the virtual top node is connected to the virtual bottom node.
  - `OpenOneSq(self, p)`: Opens a square and connects it to its adjacent open squares.

### Main Simulation Loop

The main simulation loop in `percolation.py` initializes the board and repeatedly opens random squares until the grid percolates (i.e., there is a connected path from the top to the bottom). It then prints the results.

## Dependencies

- `numpy`: Used for efficient array manipulations.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.

---

This README provides an overview of the percolation simulation project, including instructions for installation, usage examples, a description of the code structure, dependencies, and guidelines for contributing.
