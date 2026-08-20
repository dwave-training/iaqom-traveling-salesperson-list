[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-traveling-salesperson-list?quickstart=1)
  
# Traveling Salesperson with Stride<sup>TM</sup> Hybrid Solver Using List Variable

For the traveling salesperson problem, convert the mathematical formulation into a model in Python. Use a list variable to represent the decision variable, and formulate the problem so that it is compatible for submission to the Stride hybrid solver.

The objective is to minimize the total distance traveled between locations, including the return trip to the origin. The decision variable represents the order in which each city is visited. There is only one constraint which is that each city must be visited exactly once.

Build the nonlinear model then define the objective function. Remember that the constraint is implicitly enforced by the use of a list to represent the decision variable.

## Exercise 1

In the first exercise, build the traveling salesperson problem so that the total distance traveled is minimized. Create the model object, add the constant to the model, define the decision variable, and set the objective function. Then, provide two different initial states to test the code.

Open `tsp_list_initial_states.py`.

   1. Import any required packages.
   
   2. Create a nonlinear model object called `model`.

   3. Create the distance array by using numpy and name it `distance_matrix`. Import the required package and abbreviate it as `np`.

   4. Add the constant to the model object.
      - Add `distance_matrix` to the model object and name it `D`.
   
   5. Define the list decision variable and store it in `route`. Set the total number of visited cities to 6.

   6. Set the objective function to minimize the total distance traveled between locations, including the return trip to the origin:

   ```math
    min[
        D[route[:-1], route[1:]].sum() + D[route[-1], route[0]]
    ]
   ```

   7. Lock the model using a context manager. Include the following steps in the block:

      a. Define the number of states. In this case, two different states are being tested.
   
      b. Provide the following initial states `[0, 2, 4, 3, 5, 1]` and `[0, 3, 1, 4, 2, 5]`, and assign them the indexes 0 and 1, respectively.

      c. Return the initial state `[0, 2, 4, 3, 5, 1]` for the list variable symbol and store it in `route_state0`.

      d. Return the objective value of the initial state `[0, 2, 4, 3, 5, 1]` and store it in `objective_value0`.

      e. Return the initial state `[0, 3, 1, 4, 2, 5]` for the list variable symbol and store it in `route_state1`.

      f. Return the objective value of the initial state `[0, 3, 1, 4, 2, 5]` and store it in `objective_value1`.

## Exercise 2

For exercise 2, submit the problem to the Stride hybrid solver to obtain the best solution.

Start with the work completed in exercise 1. Create the model object, add the constant to the model, define the decision variable, and set the objective function. Then, submit the problem to the Stride hybrid solver.

Open `tsp_list_submit.py`.

   1. Repeat steps 1 to 6 of exercise 1. You may copy all the work you submitted in `tsp_list_initial_states.py`.
   
   2. Lock the model explicitly to prevent further changes.

   3. Instantiate the nonlinear sampler and name it `sampler`.
   
   4. Submit the nonlinear model to the Stride hybrid solver. Label your problem "TPS_List" using the `label` parameter. This label will show in your Leap dashboard when you submit your problem. Note that this label is case sensitive and uses an underscore.

   5. Return the best solution for the list variable symbol and store it in `route_state`.

   6. Return the objective value of the best solution and store it in `objective_value`.