Files in this folder : 

main.py		  - Driver code to execute graph search algorithms

multiSourceBFS.py - This file contains the implementation of the multi-source bfs function

Queue.py	  - Contains a user-defined queue structure that is used when conducting BFS.

Tree.py 	  - Contains a user-defined tree structure that is used to generate the path sequence from each node to its respective nearest hospital.

Please note that the above tree structure is not our own work, but has only been minimally modified to suit the needs of our application. It was written by : Brett Kromkamp, Stack Overflow : https://stackoverflow.com/users/932800/brett-kromkamp


pennsylvaniaRdNet.txt, texasRdNet.txt, californiaRdNet.txt - The graphs on which the code can be run, and are of varying sizes ranging from 200,000 to 2 million nodes.

pennsylvaniaRdNet_output.txt, texasRdNet_output.txt - Outputs for the graphs containing 200K and 1,000,000 nodes respectively. 

hospitals.txt - A text file containing the hospital numbers, in the format defined in the assignment rubrics. 

cutomGraph.txt - Contains a user-defined graph. Any graph that you choose to run can be used on the application.


All the text files given above have been compressed since they are too large to be saved directly. They have to be extracted before they can be viewed.



Requirements to run main.py:

-> All files must be contained within the same folder in order for the imports to be successful.

-> The input files have to be in .txt format.

-> The file names should not be changed, except the customGraph file if you would like to use your own graph. The hospital file name should not be changed.

-> The execution path should be specified to the location of the driver program.

-> The executable code also uses networkx, which is a graph library in python. In order to use this library it will have to be installed using the following command:

	$ pip install networkx

Additional details for installation can be found here : https://networkx.org/documentation/stable/install.html


Input format : 

The driver code uses a menu based approach, where an input of 0 can be used to exit the program.

Input 1: Text file selection, to choose the graph to be used to run the program.
	-> You are free to choose one of the existing text files or define your own and key in the file name.
	-> After choosing the input file, you can choose to either generate random hospitals or use pre-defined hospitals from hospitals.txt
	-> When choosing a custom input file, key in the file name without the .txt extension in order for the program to open it successfully.

Input 2: Choose whether you would like to generate hospitals randomly.
	-> If no, hospitals will be chosen from a user defined hospitals.txt file.

Input 3: Find nearest hospital or k-nearest hospitals
	-> At this point you also have the option to change the file being used.
	-> This is also the point where the program can be terminated.

Input 4 : Choose whether you would like to include the paths in the output file.

Output format :
	-> A text file containing a tabulated list of all nodes and its path to its k nearest hospitals.
	-> If you have chosen not to include the paths, the path will not be included.











