# Name: Zaria Burton  Date: 01/15/2022  Section: 2
# Assignment: 1  Due Date: 01/16/2022
# About this project: This program solves mazes using random, depth first, and breadth first algorithms
# Assumptions: every maze has a solution

from __future__ import absolute_import
from maze import Maze
from maze_viz import Visualizer
from dataStructures import *

def RandomSearch(maze):
    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited

    path = list()
    # To track path of solution and backtracking cells

    exploredNodesPath = list()
    # To track path of solution and backtracking cells

    path.append(((row_curr, col_curr), False))
    exploredNodesPath.append(((row_curr, col_curr), False))

    # Add coordinates to part of search path
    # false indicates not a back tracker visit

    fringe = Queue()  # queue
    fringe.push(path)
    explored = set()

    NumNodesExpanded = 0

    while not(fringe.isEmpty()):
        NumNodesExpanded+=1
        currentPath = fringe.randomPop()
        currentNode = currentPath[len(currentPath)-1]
        row_curr, col_curr = currentNode[0][0],currentNode[0][1]

        exploredNodesPath.append(((row_curr, col_curr), False))

        maze.grid[row_curr][col_curr].visited = True
        # Move to that neighbour

        if ((row_curr, col_curr)==maze.exit_coor):
            print("Expanded ",NumNodesExpanded," nodes.")
            return exploredNodesPath,currentPath

        explored.add((row_curr, col_curr))

        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices
        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr, col_curr)
        if neighbour_indices is not None:
            for NI in neighbour_indices:
                if NI not in explored:
                    Path = currentPath.copy()
                    Path.append((NI, False))
                    if not(fringe.contains(Path)):
                        fringe.push(Path)
    return None,None


def DepthFirstSearch(maze):
    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited

    path = list()
    # To track path of solution and backtracking cells

    exploredNodesPath = list()
    # To track path of solution and backtracking cells

    path.append(((row_curr, col_curr), False))
    exploredNodesPath.append(((row_curr, col_curr), False))

    # Add coordinates to part of search path
    # false indicates not a back tracker visit

    fringe = Stack()  # LIFO
    fringe.push(path)
    explored = set()

    NumNodesExpanded = 0

    while not (fringe.isEmpty()):
        NumNodesExpanded += 1
        currentPath = fringe.pop()
        currentNode = currentPath[len(currentPath) - 1]
        row_curr, col_curr = currentNode[0][0], currentNode[0][1]

        exploredNodesPath.append(((row_curr, col_curr), False))

        maze.grid[row_curr][col_curr].visited = True
        # Move to that neighbour
        if ((row_curr, col_curr)==maze.exit_coor):
            print("Expanded ",NumNodesExpanded," nodes.")
            return exploredNodesPath,currentPath

        explored.add((row_curr, col_curr))

        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices
        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr, col_curr)
        if neighbour_indices is not None:
            for NI in neighbour_indices:
                if NI not in explored:
                    Path = currentPath.copy()
                    Path.append((NI, False))
                    fringe.push(Path)

    return None, None


def BreadthFirstSearch(maze):
    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited

    path = list()
    # To track path of solution and backtracking cells

    exploredNodesPath = list()
    # To track path of solution and backtracking cells

    path.append(((row_curr, col_curr), False))
    exploredNodesPath.append(((row_curr, col_curr), False))

    # Add coordinates to part of search path
    # false indicates not a back tracker visit

    fringe = Queue()  #LIFO
    fringe.push(path)
    explored = set()

    NumNodesExpanded = 0

    while not (fringe.isEmpty()):
        NumNodesExpanded += 1
        currentPath = fringe.pop()
        currentNode = currentPath[len(currentPath) - 1]
        row_curr, col_curr = currentNode[0][0], currentNode[0][1]

        exploredNodesPath.append(((row_curr, col_curr), False))

        maze.grid[row_curr][col_curr].visited = True
        # Move to that neighbour

        if ((row_curr, col_curr) == maze.exit_coor):
            print("Expanded ", NumNodesExpanded, " nodes.")
            return exploredNodesPath, currentPath

        explored.add((row_curr, col_curr))

        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices
        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr, col_curr)
        if neighbour_indices is not None:
            for NI in neighbour_indices:
                if NI not in explored:
                    Path = currentPath.copy()
                    Path.append((NI, False))
                    fringe.push(Path)

    return None, None


# Generate Maze
numRows = 10
numCols = 10
theMaze = Maze(numRows, numCols, id=0)


print("Random Path")
####Random Path
# generate a solution by exploring a random path
exploredNodesPath,solutionPath = RandomSearch(theMaze)

theMaze.solution_path = exploredNodesPath
# Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.animate_maze_solution()

theMaze.solution_path = solutionPath
# Show Solution Path
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.show_maze_solution()

############################
print("DepthFirstSearch")
####DepthFirstSearch
# generate a solution by exploring a random path
theMaze.ClearSolution()
exploredNodesPath,solutionPath = DepthFirstSearch(theMaze)

theMaze.solution_path = exploredNodesPath
# Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.animate_maze_solution()

theMaze.solution_path = solutionPath
# Show Solution Path
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.show_maze_solution()

############################
print("BreadthFirstSearch")
####BreadthFirstSearch
# generate a solution by exploring a random path
theMaze.ClearSolution()
exploredNodesPath,solutionPath = BreadthFirstSearch(theMaze)

theMaze.solution_path = exploredNodesPath
# Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.animate_maze_solution()

theMaze.solution_path = solutionPath
# Show Solution Path
vis = Visualizer(theMaze, cell_size=1, media_filename="")
vis.show_maze_solution()

