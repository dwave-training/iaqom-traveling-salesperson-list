"""
Requirements:
    Objective: Minimize the total distance traveled.
    Constraint: Each city must be visited exactly once.
"""

# TODO: Import any required packages.


# TODO: Initialize the nonlinear model called `model`.


# TODO: Create the distance array by using numpy and name it `distance_matrix`.
# Hint: Import the required package and alias it as `np`.
"""
 Below is the distance matrix needed:
[
[0, 5, 7, 14, 3, 2],
[5, 0, 10, 12, 8, 1],
[7, 10, 0, 6, 11, 7],
[14, 12, 6, 0, 9, 3],
[3, 8, 11, 9, 0, 2],
[2, 1, 7, 3, 2, 0]
]
"""


# TODO: Add the constant to the model object.
# Hint: Add the constant distance_matrix to the model object and name it `D`.


# TODO: Define the list variable and store it in `route`.
# Hint: Set the total number of visited cities to 6.


# TODO: Set the objective function: Minimize the total distance traveled.
# Hint: The total distance traveled between locations, including the return trip to the origin.


# TODO: Lock the model explicitly to prevent changes.


# TODO: Instantiate the nonlinear sampler and name it `sampler`.


# TODO: Submit the nonlinear model to the Stride hybrid solver. Use the label "TSP_List", which is case-sensitive and uses an underscore.


# Process and print solution.
print("\nSubmit the Traveling Salesperson problem to the Stride hybrid solver using a list variable: \n")
"""Read in the solution returned using .state(0) and display the solutions."""

# TODO: Return the best solution for the list variable and store it in `route_state`.


# TODO: Return the objective value of the best solution and store it in `objective_value`.


# Print the best solution state and its objective value.
print(f"For state 0, route={route_state} results in the objective value {objective_value}")
