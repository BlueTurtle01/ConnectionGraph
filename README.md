# ConnectionGraph

# What does this repo do?
It is often easy to forgot how we made the connections to specific people, be it through a job, a society, a friend of a friend, etc. Visualising this helps us to appreciate the importance of taking a job
or going to the party that we may have been tempted to skip in favour of a night in watching Netflix.

# Things I have learnt
This was my first time using PyDot and Graphviz as well as NetworkX. I previously used GraphX and Spark so I was aware of the basic structure of graph creation, but these packages were new to me.
Whilst using PyDot, Graphviz, PyGraphviz, and NetworkX I realised that whilst the structure was similar, the exact code was not. This lead to finding tutorials that solved a problem I was
having in PyDot but the tutorial was written in Graphviz and needed tweaking. Therefore, to save future users having to make these adjustments for use in PyDot I created a separate repo: https://github.com/BlueTurtle01/PydotTutorials

# Things I would like to improve
Currently I am taking 2 approaches to complete the graph:
1. Create the whole graph from 1 csv file and allow PyDot to create the network as it sees fit. This leads to some unpleasant looking subgraphs and long winding edges that can often cross.
2. Create the graph using multiple csv files where each csv represents a subgraph which are then creating in a loop and in the end attached by a single edge to the main graph. 
This often looks better but is more cumbersome to retrieve the data from the user. If this were deployed as a UI it would require more steps to get the required information from the user.
Naturally, this increases the potential for error on the user's part and may lead to the user becoming exhausted and I feel would lead to graphs being created that do not look like the user
expected. In the end this would lead to the user not using the product.

I think approach 2. has more potential as the multigraph approach looks cleaner, but data collection needs to be improved.
