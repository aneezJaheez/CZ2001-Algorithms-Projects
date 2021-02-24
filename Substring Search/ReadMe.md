## Files in this folder : 

* [main.py](https://github.com/aneezJaheez/CZ2001-Algorithms-Projects/blob/main/Substring%20Search/Algorithm%20Code/main.py) - Driver code to execute search algorithms
* [BruteForce.py](https://github.com/aneezJaheez/CZ2001-Algorithms-Projects/blob/main/Substring%20Search/Algorithm%20Code/BruteForce.py) - Contains the implementation code for the naive search algorithm
* [HorspoolSunday.py](https://github.com/aneezJaheez/CZ2001-Algorithms-Projects/blob/main/Substring%20Search/Algorithm%20Code/HorspoolSunday.py) - Contains the implementation code for the Boyer-Moore-Horspool-Sunday Search algorithm
* [OriginalAlgo.py](https://github.com/aneezJaheez/CZ2001-Algorithms-Projects/blob/main/Substring%20Search/Algorithm%20Code/OriginalAlgo.py)	- Contains the implementation code for our own Original Search Algorithm
* genomic.fna 	  - Fasta (.fna) that contains the genome sequence to be searched.
* R64.txt 	  - Fasta (.txt) document that contains a genome sequence that can be searched.


### Requirements to run main.py:

1. All files must be contained within the same folder in order for the imports to be successful.
2. The input files can only be of FASTA (.fna or .txt) format.
3. The execution path should be specified to the location of the driver program.


### Input format : 

The driver code uses a menu based approach, where an input of 0 can be used to exit the program. After choosing an algorithm to run : 

1. Input the file name (Example : "genomic.fna") : This file can be any genomic sequence of FASTA format. The file has to be contained within the same folder as the driver program.
2. Input the query sequence (Example : "AGCTT") : Lower-case or upper-case inputs are accepted.

### Output format :

1. Length of list containing the matched indices
2. Time taken to run the algorithm on the genome sequence
3. Uncomment the print instruction at the end of the search function in order to display the matched indices.











