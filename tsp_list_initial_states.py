"""
Requirements:
    Objective: Minimize the total distance traveled.
    Constraint: Each city must be visited exactly once.
"""
# TODO: Import any required packages.


# TODO: Initialize the nonlinear model called model.


# TODO: Create the distance array by using numpy and name it distance_matrix.
# Hint: Import the required package and abbreviate it as np.
'''
 Below is the distance matrix needed:
[
[0, 5, 7, 14, 3, 2],
[5, 0, 10, 12, 8, 1],
[7, 10, 0, 6, 11, 7],
[14, 12, 6, 0, 9, 3],
[3, 8, 11, 9, 0, 2],
[2, 1, 7, 3, 2, 0]
]
'''


# TODO: Add the constant to the model object.
# Hint: Add the constant distance_matrix to the model object and name it D.


# TODO: Define the list variable and store it in route.
# Hint: Set the total number of visited cities to 6.


# TODO: Set the objective function: Minimize the total distance traveled.
# Hint: The total distance traveled between locations, including the return trip to the origin.


# Process and print solution.
print("\nTest the initial states of the Traveling Salesperson problem using list variable: \n")
"""Read in the initial states returned and display the solutions."""

# TODO: Lock the model using a context manager.


    # TODO: Define the number of states (test two different states).
    

    # TODO: Provide the following initial states: [0, 2, 4, 3, 5, 1] and [0, 3, 1, 4, 2, 5], and assign them the indexes 0 and 1, respectively.
    

    # TODO: Return the initial state [0, 2, 4, 3, 5, 1] for the list variable symbol and store it in route_state0.
    

    # TODO: Return the objective value of the initial state [0, 2, 4, 3, 5, 1] and store it in objective_value0.
    

    # Print initial state 0 and its objective value.
    print(f"For state 0, route={route_state0} results in objective {objective_value0}")

    # TODO: Return the initial state [0, 3, 1, 4, 2, 5] for the list variable symbol and store it in route_state1.
    

    # TODO: Return the objective value of the initial state [0, 3, 1, 4, 2, 5] and store it in objective_value1.
    

    # Print initial state 1 and its objective value.
    print(f"For state 1, route={route_state1} results in objective {objective_value1}")