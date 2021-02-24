import networkx as nx
import random as rand
import sys
from Tree import *
from Queue import *
import time

def findKNearestH(k, G, hospitals, findPath = False):
	"""
	Function to find the k nearest hospitals to all the nodes in the graph

	Arguments : 
	-> k, int - the number of nearest hospitals to be found
	-> G, networknx graph object - The graph to be traversed containing the nodes and the hospitals
	-> hospitals, list of integers - A list containing the hospital nodes

	Returns type : Void
	"""

	#Error handling to ensure that the number of hospitals to be found is not greater than the number of available hospitals.
	while k > len(hospitals) or k <= 0:
		k = int(input("Enter value of k that is smaller than the number of hospitals : "))

	#Initializing a queue for each hospital using a dictionary, where the keys are the hospital numbers and the values are the queue for the corresponding hospital to conduct BFS
	hospQ = {}

	#A visited dictionary for the nodes. A copy is maintained for each hospital. Initial values are all false. Once a node is visited it becomes true.
	visited = {}

	#Keeping track of the number of hospitals to be found for each node. This is common for all BFS search sequences
	count = {}

	#Keeping track of the hospitals found for each node and its distance. This is common for all BFS search sequences
	hFound = {}

	#Keeping a track of the path from each node to the hospitals using a tree
	bfsTree = {}

	#Initializing the value of hFound with empty dictionaries, whos key is the nearest hospitals and the value is the distance to it.
	for i in list(G.nodes):
		hFound[i] = {}
		count[i] = 0


	#Initial values in the queue will be the hospital nodes
	for i in hospitals:
		visited[i] = {}
		hospQ[i] = Queue()
		bfsTree[i] = Tree()
		bfsTree[i].create_node(("Node " + str(i)), str(i))
		hospQ[i].enqueue(i)


	#BFS search from each hospital starts here

	#i indicates from which hospital the BFS is currently being conducted.
	i = 0

	#The current distance will indicate which level of BFS we are currently in, and consequently the distance we have travelled from the hospital
	currentDistance = 1
	numHosp = len(hospitals)

	#Each iteration of the below loop represents 1 level of search for BFS for one hospital.
	#Suppose we have 3 hospital nodes, then these 3 hospitals are the roots of 3 different BFS searches that will start concurrently.
	#The first iteration of the below loop will iterate through one level of BFS for hospital 1, the second iteration for 1 level of hospital 2 and so on.
	#If the number of hospitals is h, then all BFS searches starting from each hospital will all reach their second level after h iterations of this loop.
	while numHosp > 0:

		#This list will hold the list of hospitals for which traversal is completed
		removeList = []
		#Retrieving the current hospital node number on which BFS is being conducted.
		for hosp in hospitals:

			if(hospQ[hosp].size() == 0):
				removeList.append(hosp)
				continue

			#This is where the nodes are evaluated and their closest hospitals are assigned.
			#At any point in time, the queue for a BFS search contains all the nodes that needs to be searched, or in other words, all the nodes at the current level
			#The length of the queue hence tells us how many elements whose children we need to evaluate
			#For example, if the queue contains node 6, then the loop below will search all the children of node 6.
			qSize = hospQ[hosp].size()
			for p in range(qSize):
				#Deques the queue, and retrives all the children of the dequeued node  that we need to search
				parent = hospQ[hosp].dequeue()
				nextNodes = list(G[parent])

				#Looping over all the children of the node we just dequeued
				for j in nextNodes:
					nodeName = "Node " + str(j)

					#Try except block to see if the visited list has been initialized. If it is not initialized, it is done here.
					try:
						value = visited[hosp][j]
					except:
						visited[hosp][j] = False

					if visited[hosp][j] or count[j] == k:
					#This case is either that child node has already been visited, or this child node has already found its k nearest hospitals. In both cases
					#The node is skipped and not searched again. It is also indicated that we have visited the node.
						visited[hosp][j] = True
						continue
					else:
					#This is the final case, where we find a node that has not found its k nearest hospitals and it is not a hospital node
					#In this case we :
					# -> Indicate the nearest hospital, which is the root node (hospital) of the BFS search
					# -> Increment the count by 1, incidating we have found 1 more nearest hospital for this node
					# -> Enter the nearest hospital found for this node in the hFound list, as well as the distance of this node to the root hospital
					# -> Add the node we just traversed to the traversal tree 
					# -> Lastly we place this node in the queue, since we need to search its children in the next iteration of BFS for this hospital.
						count[j] = count[j] + 1
						hFound[j][hosp] = currentDistance
						visited[hosp][j] = True
						hospQ[hosp].enqueue(j)


						if(findPath == True):
							bfsTree[hosp].create_node(nodeName, str(j), parent = str(parent))


		#Moving to the next level of traversal, so increase distance by 1 unit
		currentDistance = currentDistance + 1

		#Remove all the hospitals that have been searched
		for m in removeList:
			hospitals.remove(m)

		#Reduce the number of remaining hospitals to continue search from
		numHosp = numHosp - len(removeList)

	return hFound, bfsTree


















