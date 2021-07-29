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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    openState = util.Stack()
    closeState = []
    startState = problem.getStartState()
    # print("INIT= ", startState)
    startNode = (startState, [])  # tuples
    openState.push(startNode)

    # print(" openState: ", openState)
    # while open is not empty
    while not openState.isEmpty():
        # remove first in from open, call it X
        x, actions = openState.pop()
        # if X is a goal
        if problem.isGoalState(x):
            # print("SUCCESS")
            # return SUCCESS
            # print(actions)
            return actions
        # else
        else:
            # generate children of X
            successor = problem.getSuccessors(x)
            # put X on closed
            closeState.append(x)
            # discard children of X if already on open or closed
            for childSuccessor, childAction, childStepCost in successor:
                # pop remaining children
                if (childSuccessor, childAction not in openState.list) and (childSuccessor not in closeState):
                    newAction = actions + [childAction]
                    currentNode = (childSuccessor, newAction)
                    # print(actions)
                    openState.push(currentNode)
                    
      
    # return FAIL
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    openState = util.Queue()
    closeState = []
    startState = problem.getStartState()
    startNode = (startState, [], 0)  # tuples
    openState.push(startNode)

    # print(" openState: ", openState)
    # while open is not empty
    while not openState.isEmpty():
        # remove first in from open, call it X
        x, actions, cost = openState.pop()
        # print("x= ", x, "   action= ", actions)
        # if X is a goal
        if (x, actions, cost not in openState.list) and (x not in closeState):
        #if (childSuccessor, childAction, childStepCost not in openState.list) and (childSuccessor not in closeState):

            if problem.isGoalState(x):
                # print("SUCCESS")
                return actions
            # else
            else:
                # generate children of X
                successor = problem.getSuccessors(x)
                # put X on closed
                closeState.append(x)
                # discard children of X if already on open or closed
                for childSuccessor, childAction, childStepCost in successor:
                     # pop remaining children
                    # if (childSuccessor not in closeState):
                    newAction = actions + [childAction]
                    newCost = cost + childStepCost
                    currentNode = (childSuccessor, newAction, newCost)
                    # print(actions)
                    openState.push(currentNode)

    # return FAIL
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    openState = util.PriorityQueue()
    closeState = []
    firstNode = (problem.getStartState(), [])
    openState.push(firstNode, heuristic(problem.getStartState(), problem))

    while not openState.isEmpty():
        x, actions = openState.pop()
        if problem.isGoalState(x):
            return actions
        elif x not in closeState:
            closeState.append(x)
            for cand_state, cand_action, cand_cost in problem.getSuccessors(x):
                if cand_state not in closeState:
                    tmpAction = actions + [cand_action]
                    tmpG = heuristic(cand_state, problem)
                    tmpH = problem.getCostOfActions(actions + [cand_action])
                    openState.update((cand_state, (actions + [cand_action])), (tmpG + tmpH))
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
