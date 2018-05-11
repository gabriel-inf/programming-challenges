# Quick briefing

A dynamic-programming algorithm solves each
subsubproblem just once and then saves its answer in a table, thereby avoiding the
work of recomputing the answer every time it solves each subsubproblem.

We typically apply dynamic programming to optimization problems. Such problems
can have many possible solutions. Each solution has a value, and we wish to
find a solution with the optimal (minimum or maximum) value. We call such a
solution an optimal solution to the problem, as opposed to the optimal solution,
since there may be several solutions that achieve the optimal value.


### Steps: 

1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information

-- Cormen