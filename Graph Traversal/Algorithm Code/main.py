import networkx as nx
import random as rand
import sys
from Tree import *
from Queue import *
from multiSourceBFS import *
import time

(_ADD, _DELETE, _INSERT) = range(3)
(_ROOT, _DEPTH, _WIDTH) = range(3)

#Function to get the graph from a text file and store it in a networkx graph object
def getGraphFromFile():
	print("\nSelect a file to use : ")
	print("1. California Road Network (1.96 Million Nodes)")
	print("2. Texas Road Network Subset (1 Million Nodes approx.)")
	print("3. Pennsylvania Network Subset (200K Nodes Approx.)")
	print("4. Custom graph file.")
	fileNo = str(input("\nWhich file would you like to use? : "))
	G = nx.Graph()

	retStr = ""
	
	while(1):
		if(fileNo == "1"):
			retStr = "californiaRdNet"
			break
		elif(fileNo == "2"):
			retStr = "texasRdNet"
			break
		elif(fileNo == "3"):
			retStr = "pennsylvaniaRdNet"
			break
		elif(fileNo == '4'):
			retStr = str(input("Please enter the name of the text file (excluding .txt extension) : "))
			break
		else:
			print("Invalid value. Enter a valid file number.")
			continue

	toOpen = retStr + ".txt"
	f = open(toOpen)
	for line in f:
		if(line[0] == "#"):
			continue

		nodes = line.rstrip().split("\t")
		G.add_edge(int(nodes[0]), int(nodes[1]))

	f.close()

	hospitals = []
	f = open("hospitals.txt")
	for line in f:
		line = line.rstrip()
		if(line[0] == '#'):
			continue
		
		hospitals.append(int(line))

	f.close()

	return G, hospitals, retStr

def writeOutputToFile(hFound, paths, G, hospitals, fileName):
	orderedNodes = list(G.nodes)
	orderedNodes.sort()

	orig_stdout = sys.stdout
	outFile = fileName + "_output.txt"
	f = open(outFile, 'w')
	sys.stdout = f
	print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
	print("| Node             | Hospitals      | Distance            | Path                                                                                                  |")
	print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

	for n in orderedNodes:
		if(n in hospitals):
			continue

		if(not(n in hFound)):
			print("Disconnected Node.")
			continue

		for hosp in hFound[n].keys():
			path = " "
			try:
				path = "{:<100}".format(paths[hosp].showPath(str(n)))
			except:
				path = " "

			print("| ", f'{n :>8}', "       | ", f'{hosp :> 8}', "     | ", f'{hFound[n][hosp] :> 6}', "            | ", path, "|")
		print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

	sys.stdout = orig_stdout
	f.close()
	return



if __name__ == "__main__":
	G = None
	hospitals = []
	writeBack = ""
	choice = -1
	while choice != 0:
		if(choice == -1):
			choice = '3'
		else:
			print("\n1. Find nearest hospital from each node.")
			print("2. Find the nearest k hospitals from each node.")
			print("3. Change file.")
			print("0. Exit.")
			choice = str(input("Enter your choice : "))

		if(choice == '1'):
			start_time = time.time()
			hFound, paths = findKNearestH(1, G, hospitals.copy(), True)
			print("Nearest hospitals found.")
			print("----Time Taken to complete search---- = ", (time.time() - start_time), " s")

			print("Writing output to text file.....")
			writeOutputToFile(hFound, paths, G, hospitals, writeBack)

		elif choice == '2':
			k = int(input("\nEnter the number of nearest hospitals to find: "))
			#hFound contains the k nearest hospitals for each node and its distance
			#paths is the tree generated during bfs traversal. This tree is used to highlight the path from the nodes to their nearest hospitals
			print("Writing the path to each hospital to the text file may be very time consuming for large number of nodes.")
			findPath = str(input("Would you like to include path to each hospital in the output? (Y/N)"))

			writePath = False
			if(findPath.upper() == "Y"):
				writePath = True

			start_time = time.time()
			hFound, paths = findKNearestH(k, G, hospitals.copy(), writePath)
			print("Nearest hospitals found.")
			print("----Time Taken to complete search---- = ", (time.time() - start_time), " s")

			print("Writing output to text file.....")
			writeOutputToFile(hFound, paths, G, hospitals, writeBack)

		elif choice == '3':
			G, hospitals, writeBack = getGraphFromFile()
			print("Number of nodes : ", G.number_of_nodes())

			r = str(input("Generate random hospitals? (Y/N) : "))
			if(r.upper() == 'Y'):
				#Generating random hospital nodes
				num_nodes = G.number_of_nodes()

				if(G.number_of_nodes() > 100000):
					num_nodes = num_nodes // 100
				elif num_nodes > 100:
					num_nodes = num_nodes // 10

				nodes = list(G.nodes)
				maxVal = max(nodes)
				hospitals = []
				n = rand.randint(3, num_nodes)

				while(n > 0):
					# hNode = rand.randint(0, maxVal)
					num = rand.randint(0, len(nodes)-1)
					hNode = nodes[num] 
					
					if(hNode in hospitals):
						continue
					n = n - 1
					hospitals.append(hNode)

				print("\nNumber of hospitals generated : ", len(hospitals))
				choice = 1
			else:
				hospitals = []
				f = open("hospitals.txt")
				for line in f:
					line = line.rstrip()
					if(line[0] == '#'):
						continue
					
					hospitals.append(int(line))

				f.close()

		elif choice == '0':
			print("\nExiting program...\n\n")
			sys.exit()

		else:
			print("\nInvalid entry, try again.")


	








