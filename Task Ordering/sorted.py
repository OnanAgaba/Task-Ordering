
from collections import defaultdict

def sorted_steps(dependencies):
    """
    Orders tasks respecting prerequisites with alphabetical prioritization.
    The parameter dependencies lists two-item where each [X, Y] means X must come before Y.
    """
    # Build the graph and track in-degrees
    graph = defaultdict(list)  # Adjacent list for the graph
    in_degree = {}  # Dictionary to track the number of prerequisites for each task

    # Initialize the graph and in-degree dictionary
    for prereq, task in dependencies:
        if prereq not in graph:
            graph[prereq] = []
        if task not in graph:
            graph[task] = []
        graph[prereq].append(task)
        in_degree[task] = in_degree.get(task, 0) + 1
        if prereq not in in_degree:
            in_degree[prereq] = 0

    # Find all tasks with no prerequisites (in-degree == 0)
    available_tasks = [task for task in in_degree if in_degree[task] == 0]
    available_tasks.sort()  # Sort alphabetically to maintain order

    # Process tasks one by one
    result = []  # List to store the final order of tasks
    while available_tasks:
        # Pick the alphabetically first task
        current_task = available_tasks.pop(0)
        result.append(current_task)

        # Reduce the in-degree of its neighbors
        for neighbor in graph[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # add to available tasks
                available_tasks.append(neighbor)
                available_tasks.sort()  # Re-sort to ensure alphabetical order

    # Return the result as a string
    return ''.join(result)
