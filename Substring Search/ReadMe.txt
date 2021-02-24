Files in this folder : 

main.py		  - Driver code to execute search algorithms

BruteForce.py 	  - Contains the implementation code for the naive search algorithm

HorspoolSunday.py - Contains the implementation code for the Boyer-Moore-Horspool-Sunday Search algorithm

OriginalAlgo.py	  - Contains the implementation code for our own Original Search Algorithm

genomic.fna 	  - Fasta (.fna) that contains the genome sequence to be searched.

R64.txt 	  - Fasta (.txt) document that contains a genome sequence that can be searched.


Requirements to run main.py:

-> All files must be contained within the same folder in order for the imports to be successful.

-> The input files can only be of FASTA (.fna or .txt) format.

-> The execution path should be specified to the location of the driver program.


Input format : 

The driver code uses a menu based approach, where an input of 0 can be used to exit the program.


After choosing an algorithm to run : 

-> Input the file name (Example : "genomic.fna") : This file can be any genomic sequence of FASTA format. The file has to be contained within the same folder as the driver program.

-> Input the query sequence (Example : "AGCTT") : Lower-case or upper-case inputs are accepted.

Output format :

-> Length of list containing the matched indices
-> Time taken to run the algorithm on the genome sequence

-> Uncomment the print instruction at the end of the search function in order to display the matched indices.











