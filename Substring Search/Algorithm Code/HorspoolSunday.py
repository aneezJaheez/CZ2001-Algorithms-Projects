import time
#Boyer Moore Horsepool Sunday Algorithm

#====================================================================================================================================================================================
#====================================================================================================================================================================================
def badCharHeuristic(string, size):
    """ 
    Defines the lookup table used for the 
    Bad Character shift and the Sunday Shift 
    in the Boyer-Moore-Horspool-Sunday Search Algorithm.
    The shift in this case refers to how many characters of the main string
    can be skipped during the search process.

    Arguments : Substring, Lebgth of Substring
    Returns : dictionary containing shift values for each character
    """ 

    #Dictionary that will hold all the shift values for each character.
    badChar = {}

    for i in range(size):

        #The last character in the substring will have a shift value of 0 if it is unique is
        #So the last character is assigned a shift value of "size" if it does not already exist in the dictionary
        if i == size - 1:
            if string[i] in badChar:
                continue
            else:
                badChar[string[i]] = size

        #Every other character is assigned a shift value that depends on the position of its rightmost occurence in the substring, and the size of the string
        else:
            badChar[string[i]] = int(size - 1 - i)

            if badChar[string[i]] <= 0:
                badChar[string[i]] = size

        #When shift valui is <= 0, we assign a shift size equal to the length of the substring


    #Returns the resutling character lookup table
    return badChar


def BMHS(txt, pat):
    """
    Function definition of the Boyer-Moore-Horspool-Sunday Search Algorithm

    Arguments : Main String, Substring
    Return value : void
    """

    #Tracking the execution time
    start_time = time.time()

    subLen = len(pat)
    mainLen = len(txt)

    #Uses the accepted substring to retrive the lookup table containing the shift values for each mismatched character in the substring
    badChar = badCharHeuristic(pat, subLen)

    #List of matched indices
    matchedIndex = []

    #Search starts at index 0 and ends at index lastIndex
    currentIndex = 0
    lastIndex = mainLen - subLen

    #Search continues until the below condition is not satisfied. 
    #We use  < and not <= because when using the Sunday heuristic, we compare one character ahead of the main string, hence search should end one character before mainLen - subLen
    while currentIndex < lastIndex:

        #horseIndex defines the shift value produced by the mismatched character
        horseIndex = currentIndex

        #Tracks the number of unmatched characters per iteration
        unmatched = subLen - 1

        while(txt[currentIndex + unmatched] == pat[unmatched]) and unmatched >= 0:
            unmatched -= 1

        if unmatched == -1:
            #When all characters match, it means the substring has occured at this location in the mainstring. The index is recorded.
            matchedIndex.append(currentIndex)

            #When there is no mismatched character, the bad character does not exist and the substring is shifted by 1 character.
            currentIndex += 1
        else:
            #When all characters do not match, it indictaes the substring needs to move forward along the main string
            matched = (subLen - 1) - unmatched
            unmatchedChar = txt[currentIndex + unmatched]
            
            #Retrives the chracter that is positioned 1 index ahead of the current main string being compared
            sundayChar = txt[currentIndex + subLen]
            sundayIndex = currentIndex

            #Uses the Sunday character to determine how much the substring can be shifted in accordance with this character. Works in a similar manner as the bad character but adds an additional shift
            shift = subLen + 1
            if sundayChar == pat[subLen - 1]:
                shift = 1
            elif sundayChar in badChar:
                shift = badChar[sundayChar] + 1

            sundayIndex = currentIndex + shift

            #Checks if the bad character exists in the lookup table. If it does not, then the substring can be moved ahead of the main string.
            if unmatchedChar in badChar:
                temp = badChar[unmatchedChar] - matched
                shift = temp if temp > 1 else 1
            else:
                shift = subLen - matched

            horseIndex = currentIndex + shift

            #Chooses the character that produces the larger shift value
            currentIndex = sundayIndex if(sundayIndex > horseIndex) else horseIndex

    print("\n\nNumber of matched found : ", len(matchedIndex))
    print("--- %s seconds ---" % (time.time() - start_time))

    #Uncomment this line to display the indices.
    # print("Matched Indices : ", matchedIndex)

#====================================================================================================================================================================================
#====================================================================================================================================================================================


#Original Algorithm
#====================================================================================================================================================================================
#====================================================================================================================================================================================