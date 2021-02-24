import time


#Original Algorithm
#====================================================================================================================================================================================
#====================================================================================================================================================================================

def lookupTable(substring, subLen):
    """
    Defines the lookup table used in the Original Algorithm. 
    This function pairs characters in the substring and records the indices of the first character in the pair in a lookup table.
    The pairing format is determined in accordance with the lenght of the substring.

    Arguments : Substring, length of Substring 
    Returns : Dictionary containing the paired character as keys, and the list of indices they occur at as values.

    For example : 

    Substring : "AABCACD"

    The distance between each character in the pair is determined using the equation "subLen // 2", in this case distance is 7 // 2 = 3
    Hence the character pairs in the dictionary will include : ---C--D (index = 3), --B--C- (index = 2), -A--A-- (index = 1), A--C--- (index = 0)

    The dictionary will be represented as follows : 

    dict = {
    'CD' = [3],
    'BC' = [2],
    'AA' = [1],
    'AC' = [0]
    }

    In case the same pair occurs more than once, its occurence index will be appended to the corresponding list.

    """
    gap = subLen // 2

    #Starts pairing from the last character in the substring
    subPoint = [subLen - 1 - gap, subLen - 1]

    #Dictionary that stores the indices of each pair. The key of the dictionary is the pair of characters, and the value is a list of its occurrences.
    jumpLen = {}

    #Pairing continues until the indices of the pairs are >- 0
    while(subPoint[0] >= 0):
        txt = substring[subPoint[0]] + substring[subPoint[1]]
        
        #If the pair exists in the dictionary, the index is appened to the exising indices for the same pair. Multiple occurrences of the same pair are recorded.
        if(txt in jumpLen):
            jumpLen[txt].append(subPoint[0])
        else:
        # If the pair does not exist in the dictionary, then a new key value pair is created for it.
            jumpLen[txt] = []
            jumpLen[txt].append(subPoint[0])

        #Updates subPoints to record the next pair of characters.
        subPoint = updateSubPoint(subPoint)

    #Returns the dictionary containing the pairs and there corresponding occurrences
    return jumpLen

def updateSubPoint(subPoint):
    """
    Function to update the pairing points for the lookuptable() function.

    Arguments : list containing the indices of the current pair
    Returns : Updated list containing the new pair to be recorded.

    Example : 

    Substring = "AABCACD"
    Suppose the current pair being recorded is ---C--D (index = 3 and index = 6), therefore subPoint holds a list = [3, 6]
    Updated value of subPoint = [3 - 1, 6 - 1] = [2, 5], which is the retuned list containing the positions of the next two characters to be paired.
    """

    subPoint[0] -= 1
    subPoint[1] -= 1
    return subPoint


def updateCheckpointsEven(checkpoints, gap):
    """
    Updates the checkpoints created on the mainstring when the length of the substring is even. The distance between each checkpoint is determined 
    by the length of the substring as subLen // 2.

    Arguments : List containing current checkpoint indices on the main string, gap (distance between 2 checkpoints)
    Returns : List containing the indices of the next checkpoint in the mainstring

    Example : 

    Main string = "AAABBBCDABCDAABCACDBCAC"
    Substring   = "AABCAC"

    gap = 6 // 2 = 3

    Initial checkpoints = "---B--C----------------"
    Updated checkpoitns = "------C--B-------------"

    where - represents a character in the main string and the distance between 2 checkpoints is the value of gap.
    """

    checkpoints[0] = checkpoints[1]
    checkpoints[1] += gap
    return checkpoints

def updateCheckpointsOdd(checkpoints, gap):
    """
    Updates the checkpoints created on the mainstring when the length of the substring is odd. The distance between each checkpoint is determined 
    by the length of the substring as subLen // 2.

    Arguments : List containing current checkpoint indices on the main string, gap (distance between 2 checkpoints)
    Returns : List containing the indices of the next checkpoint in the mainstring

    Example : 

    Main string = "ACAABCDBCBDCB"
    Substring   = "AABCD"

    gap = 5 // 2 = 2

    Initial checkpoints = "--A-B--------"
    Updated checkpoitns = "-----C-B-----"

    In this case the checkpoints are moved by 1 extra position every time this function is called. This is because when the length of the substring is odd, 
    duplicate matches may occur if the checkpoints are not updated in this manner.

    Example of a bad shift of checkpoints:

    Initial checkpoints = "--A-B--------"
    Substring =           "AABCD"

    Updated checkpoints when subLen is eveb = "----B-D------"

    AB pair occurs at index [0, 2]

    Indices =             "0123456789"
    Initial checkpoints = "--A-B--------"
    Substring =             "AABCD"

    Further matching carried out:
    Initial checkpoints = "ACAABCDBCBDCB"
    Substring =             "AABCD"
    Match found, add index 2 to matched indices

    Now checkpoints are updated since every pair has been compared. In a bad update of checkpoints, this would occur
    
    Indices =                   "0123456789"
    Badly Updated checkpoints = "--A-B--------"
    Substring =                 "AABCD"

    AB pair occurs at [0,2] of the substring

    Indices =                   "0123456789"
    Badly Updated checkpoints = "--A-B--------"
    Substring =                   "AABCD"

    Match found, add index 2 to matched indexes.

    Indices =                   "0123456789"
    Badly Updated checkpoints = "----B-D------"
    Substring =                   "AABCD"

    BD pair occurs at index [2, 4] of the substring


    Now matched indices contain [2, 2], which is a duplicate. Hence, checkpoints need to be updated by 1 extra position.

    Indices =                       "0123456789"
    Correctly Updated checkpoitns = "-----C-B-----"
    Substring =                     "AABCD"

    CB pair does not occur, skip checkpoint. No duplicates recorded in this case.

    CB pair found at index 

    where - represents a character in the main string and the distance between 2 checkpoints is the value of gap.
    """

    checkpoints[0] = checkpoints[1] + 1
    checkpoints[1] += gap + 1
    return checkpoints

def original(subString,mainString):
    """
    Function definition for the Original algorithm for substring matching. Uses the lookupTable() function and the two updateCheckpoint() functions.

    Arguments:
    -> subString : the substring that needs to be found 
    -> mainString : The full genome sequence within which the pattern will be searched.

    Returns:
    -> Void

    Working:

    The algorithm works by setting checkpoints along the mainstring, where each checkpoint is ahead of the previous one by (len(subString) // 2) characters.
	At ever iteration, 2 checkopoint characters are taken together to find a substring match in the main string. Every iteration, the checkpoints are updated 
	in the manner defined in the above 2 updateCheckpoints functions depending on the length of the substring. The algorithm uses the lookup table (function definition above)
	to find matches of the substring in the mainstring.

	Example of Algorithm working (Using the same example in the presentation sides):

	Index =	 	 "01234567"
	Substring  = "TATACGTG"
	Mainstring = "ACTGACTGACTAACTGACTATACGTGA"

	Index here is only shown for explanation purposes to see where the match occurs.

	gap(checkpoint distance) = 7 // 2 = 3

	lookupTable(substring) will return the following dictionary. The way lookupTable works has already been defined in its function definition.

	lookup table = {
	'CG' : [4]
	'AT' : [3]
	'TG' : [2]
	'AC' : [1]
	'TA' : [0]
	}

	Checkpoints on main string in first iteration

	Index =	 	 "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "----A--G-------------------"

	-> Current checkpoint pair = "AG"
	-> look for 'AG' in lookup table
	-> AG not found in lookup table, skip to next pair of checkpoints on mainstring

	Updated checkpoints(mathod described in the update checkpoint functions):

	Index =	 	 "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "-------G--T----------------"

	-> Look for 'GT' in the lookup table
	-> 'GT' not found
	-> Skip to next checkpoints.

	Index =	 	 "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "----------T--C-------------"

	-> Look for "TC" in the lookup table.
	-> Not found, skip to next checkpoint.


`	Index - 10 =	 	   "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "-------------C--A----------"

	-> Look for 'CA' in the lookup table.
	-> 'CA' not found, move to next checkpoints

	
	Index - 10 =	 	   "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "----------------A--A-------"

	-> 'AA' not found in the lookup table, skip to next checkpoints

	Index - 20 =	 	   			 "0123456789"
	Substring  = "TATACGTG"
	Mainstring = "-------------------A--C----"

	-> "AC" found in the lookup table at substring index [1]. So we have a potential match.
	-> Position substring such that it lines up with the checkpoint match as shown below.

	Index - 20 =	 	   			 "0123456789"
	Substring  = 				   "TATACGTG"
	Mainstring = "-------------------A--C----"


	-> Now start comparing the remaining characters in order to confirm if it is a match, as shown below.

	Index - 20 =	 	   			 "0123456789"
	Substring  = 				   "TATACGTG"
	Mainstring = "----------------ACTATTCGTGA"

	-> Upon comparing the remaining characters, we find that it is a match at position 18. We store the index position of the match.
	-> Subsequently, we check if there is another 'AC' pair in the substring. If not, we continue to the nexh checkpoint and resume search.

    """

    #Tracking the execution time
    start_time = time.time()

    matches = []
    mainLen = len(mainString)
    subLen = len(subString)

    gap = subLen // 2

    #Retrives the lookup dictionary for the query sequence.
    jumpLen = lookupTable(subString, subLen)

    lastIndex = mainLen - subLen

    #Initializes the initial checkpoints for searching along the main string
    checkpoints = [subLen - 1 - gap, subLen - 1]

    #Checkpoints are repeatedly updated until the last index for search
    while(checkpoints[0] <= lastIndex):

        #Retrives the checkpoint pair from the mainstring, so that it can be searched in the dictionary containing the substring pairs to look for an occurrence.
        matchText = mainString[checkpoints[0]] + mainString[checkpoints[1]]

        #If the checkpoint pair is contained in the substring, matching of the remaining characters is carried out.
        if(matchText in jumpLen):
            indices = jumpLen[matchText]
            for temp in indices:
                mainStart = checkpoints[0] - temp
                matched = 0

                while(matched <= (subLen - 1) and (mainString[mainStart] == subString[matched])):
                    matched += 1
                    mainStart += 1

                if(matched == subLen):
                    matches.append(mainStart)
                else:
                    continue

        #The checkpoints in the main genome sequence is updated according to the odd-even rule described in the respective functions.
        if(subLen % 2 == 0):
            checkpoints = updateCheckpointsEven(checkpoints, gap)
        else:
            checkpoints = updateCheckpointsOdd(checkpoints, gap)

    print("\n\nNumber of matched Found : ", len(matches))
    print("--- %s seconds ---" % (time.time() - start_time))

    #Uncomment the below line to display the indices
    # print("Matched Indices : ", matches)

#====================================================================================================================================================================================
#====================================================================================================================================================================================