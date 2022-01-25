# Name: Zaria Burton  Date: 01/24/2022  Section: 2
# Assignment: 3  Due Date: 01/26/2022
# About this project: This program solves mazes using random, Greedy, and A* algorithms
# Assumptions: every maze has a solution

from __future__ import absolute_import
from maze import Maze
from maze_viz import Visualizer
from dataStructures import PriorityQueue
import random


def RandomSearch(maze):
    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited
    visited_cells = list()

    # Stack of visited cells for backtracking

    path = list()
    # To track path of solution and backtracking cells

    while len(maze.prize_coor_list) >0:
        # While the exit cell has not been encountered

        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices

        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr,col_curr)
        if neighbour_indices is not None:
            # If there are unvisited neighbour cells

            visited_cells.append((row_curr, col_curr))
            # Add current cell to stack

            path.append(((row_curr, col_curr), False))
            # Add coordinates to part of search path
            #false indicates not a back tracker visit

            row_next, col_next = random.choice(neighbour_indices)
            # Choose random neighbour

            maze.grid[row_next][col_next].visited = True
            # Move to that neighbour

            row_curr = row_next
            col_curr = col_next

        elif len(visited_cells) > 0:
            # If there are no unvisited neighbour cells

            path.append(((row_curr, col_curr), True))
            # Add coordinates to part of search path
            #true indicates it is a back tracker visit

            row_curr, col_curr = visited_cells.pop()
            # Pop previous visited cell (backtracking)

        if ((row_curr, col_curr) in maze.prize_coor_list):
           maze.prize_coor_list.remove((row_curr, col_curr))
    path.append(((row_curr, col_curr), False))  # Append final location to path
    print("Expanded ", len(path), " nodes.")
    return path


def Greedy(maze):
    def prizeManhattan(coors):
        #Manhattan distance from current point to prize
        return abs(coors[0][0] - coors[1][0]) + abs(coors[0][1] - coors[1][1])

    def Manhattan(NI):
        sortedPrizes = PriorityQueue('min', prizeManhattan)
        p = maze.prize_coor_list[0]
        for n in NI:
            two_coors = p, n
            sortedPrizes.append(two_coors)
        # coordinate that is closest to a prize
        closest = (sortedPrizes.pop())[1]
        return closest

    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited
    visited_cells = list()

    # Stack of visited cells for backtracking

    path = list()
    # To track path of solution and backtracking cells

    while len(maze.prize_coor_list) > 0:
        # While the exit cell has not been encountered

        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices

        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr,col_curr)
        if neighbour_indices is not None:
            # If there are unvisited neighbour cells

            visited_cells.append((row_curr, col_curr))
            # Add current cell to stack

            path.append(((row_curr, col_curr), False))
            # Add coordinates to part of search path
            #false indicates not a back tracker visit

            #sort neighbours by Manhattan distance from nearest prize coor
            row_next, col_next = Manhattan(neighbour_indices)
            # Choose random neighbour

            maze.grid[row_next][col_next].visited = True
            # Move to that neighbour

            row_curr = row_next
            col_curr = col_next

        elif len(visited_cells) > 0:
            # If there are no unvisited neighbour cells

            path.append(((row_curr, col_curr), True))
            # Add coordinates to part of search path
            #true indicates it is a back tracker visit

            row_curr, col_curr = visited_cells.pop()
            # Pop previous visited cell (backtracking)

        if ((row_curr, col_curr) in maze.prize_coor_list):
           maze.prize_coor_list.remove((row_curr, col_curr))
    path.append(((row_curr, col_curr), False))  # Append final location to path
    print("Expanded ", len(path), " nodes.")
    return path


def AStar(maze):
    row_curr, col_curr = maze.entry_coor  # Where to start searching

    maze.grid[row_curr][col_curr].visited = True
    # Set initial cell to visited

    path = list()
    # To track path of solution and backtracking cells

    exploredNodesPath = list()
    # To track path of solution and backtracking cells

    path.append(((row_curr, col_curr), False))

    # Add coordinates to part of search path
    # false indicates not a back tracker visit

    # Manhattan distance to goal + entry to current node length
    def f(a):
        e = maze.prize_coor_list[0]
        return abs(a[len(a) - 1][0][0] - e[0]) + abs(a[len(a) - 1][0][1] - e[1]) + len(a) - 1

    fringe = PriorityQueue('min', f)  # priority queue based on Manhattan distance
    fringe.append(path)
    explored = set()

    while True:
        currentPath = fringe.pop()
        currentNode = currentPath[len(currentPath) - 1]
        row_curr, col_curr = currentNode[0][0], currentNode[0][1]

        exploredNodesPath.append(((row_curr, col_curr), False))

        maze.grid[row_curr][col_curr].visited = True
        # Move to that neighbour

        if ((row_curr, col_curr) in maze.prize_coor_list):
            maze.prize_coor_list.remove((row_curr, col_curr))

        explored.add((row_curr, col_curr))
        if len(maze.prize_coor_list) == 0:
            break
        neighbour_indices = maze.find_neighbours(row_curr, col_curr)
        # Find neighbour indices
        neighbour_indices = maze.validate_neighbours_solve(neighbour_indices, row_curr, col_curr)
        if neighbour_indices is not None:
            for NI in neighbour_indices:
                if NI not in explored and NI not in currentPath:
                    Path = currentPath.copy()
                    Path.append((NI, False))
                    if not (fringe.__contains__(Path)):
                        fringe.append(Path)
                elif NI in currentPath:
                    if f(NI) < currentPath[NI]:
                        del currentPath[NI]
                        Path = currentPath.copy()
                        Path.append((NI, False))
                        if not (fringe.__contains__(Path)):
                            fringe.append(Path)
    print("Expanded ", len(exploredNodesPath), " nodes.")
    return exploredNodesPath


#Generate Maze
numRows = 10
numCols = 10
theMaze = Maze(numRows, numCols,numPzLocs=5,id=0)

#Show Maze Start
vis = Visualizer(theMaze,cell_size=1,media_filename="")
vis.show_maze()

print("Random Path")

####Random Path
#generate a solution by exploring a random path
theMaze.solution_path = RandomSearch(theMaze)

#Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1,media_filename="")
vis.animate_maze_solution()

print("Greedy")

####Greedy Path
theMaze.ClearSolution()

#generate a solution by exploring a random path
theMaze.solution_path = Greedy(theMaze)

#Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1,media_filename="")
vis.animate_maze_solution()

print("A Star Path")

####AStar Path
theMaze.ClearSolution()

#generate a solution by exploring a random path
theMaze.solution_path = AStar(theMaze)

#Show what points were explored to find the solution
vis = Visualizer(theMaze, cell_size=1,media_filename="")
vis.animate_maze_solution()
