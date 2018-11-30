# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    """Create two stacks: one stores location nodes, another stores action nodes"""
    from util import Stack

    node = [problem.getStartState()]
    openStack = Stack()
    openStack.push(node)
    
    action = []
    actionStack = Stack()
    actionStack.push(action)

    """When openStack is not empty, continue searching"""
    while not openStack.isEmpty():
        currNode = openStack.pop()
        endState = currNode.pop()
        currNode.append(endState)
        currAction = actionStack.pop()
        
        """Check whether the state is goal state when removing the node from the stack"""
        if problem.isGoalState(endState):
            return currAction

        for x in problem.getSuccessors(endState):
            """Path checking"""
            if not x[0] in currNode:
                newNode = currNode[:]
                newNode.append(x[0])
                openStack.push(newNode)

                newAction = currAction[:]
                newAction.append(x[1])
                actionStack.push(newAction)
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    """Create two Queues: one stores location nodes, another stores action nodes"""

    from util import Queue

    node = [problem.getStartState()]
    openQueue = Queue()
    openQueue.push(node)
    
    action = []
    actionQueue = Queue()
    actionQueue.push(action)

    visited = []


    """When openQueue is not empty, continue searching"""
    while not openQueue.isEmpty():
        currNode = openQueue.pop()
        endState = currNode.pop()
        currNode.append(endState)
        currAction = actionQueue.pop()
        
        """Check whether the state is goal state when removing the node from the queue"""
        if problem.isGoalState(endState):
            return currAction

        """Full Cycle checking"""
        if not endState in visited:
            visited.append(endState)
            
            for x in problem.getSuccessors(endState):    
            
                newNode = currNode[:]
                newNode.append(x[0])
                openQueue.push(newNode)

                newAction = currAction[:]
                newAction.append(x[1])
                actionQueue.push(newAction)

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    "*** YOUR CODE HERE ***"
    """Create two PriorityQueues: one stores location nodes, another stores action nodes"""
    from util import PriorityQueue

    """Initializa the priority queue"""
    node = [problem.getStartState()]
    openQueue = PriorityQueue()
    openQueue.push(node, 0)
    
    action = []
    actionQueue = PriorityQueue()
    actionQueue.push(action, 0)

    visited = []

    """When openQueue is not empty, continue searching"""
    while not openQueue.isEmpty():
        currNode = openQueue.pop()
        endState = currNode.pop()
        currNode.append(endState)
        currAction = actionQueue.pop()
        
        """Check whether the state is goal state when removing the node from the queue"""
        if problem.isGoalState(endState):
            return currAction

        """Full Cycle checking"""
        if not endState in visited:
            visited.append(endState)
            for x in problem.getSuccessors(endState):
                
                newNode = currNode[:]
                newNode.append(x[0])
                newAction = currAction[:]
                newAction.append(x[1])

                """Get the current cost of the path and updated the queue"""
                newCost = problem.getCostOfActions(newAction)
                openQueue.update(newNode, newCost)
                actionQueue.update(newAction, newCost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Create two PriorityQueues: one stores location nodes, another stores action nodes"""
    from util import PriorityQueue

    """Initializa the priority queue"""
    node = [problem.getStartState()]
    openQueue = PriorityQueue()

    """Get the heuristic of the initial state"""
    initialHeu = heuristic(problem.getStartState(), problem)
    initailCost = 0
    openQueue.push(node, initailCost + initialHeu)
    
    action = []
    actionQueue = PriorityQueue()
    actionQueue.push(action, initailCost + initialHeu)

    visited = []

    """When openQueue is not empty, continue searching"""
    while not openQueue.isEmpty():
        currNode = openQueue.pop()
        endState = currNode.pop()
        currNode.append(endState)
        currAction = actionQueue.pop()
        
        """Check whether the state is goal state when removing the node from the queue"""
        if problem.isGoalState(endState):
            return currAction

        """Full Cycle checking"""
        if not endState in visited:
            visited.append(endState)
            for x in problem.getSuccessors(endState):
                
                newNode = currNode[:]
                newNode.append(x[0])
                newAction = currAction[:]
                newAction.append(x[1])

                """Get the new cost and heuristic of the path and updated the priority queue"""
                newCost = problem.getCostOfActions(newAction)
                newHeu = heuristic(x[0], problem)
                openQueue.update(newNode, newCost + newHeu)
                actionQueue.update(newAction, newCost + newHeu)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
