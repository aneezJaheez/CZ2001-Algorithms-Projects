import time

#Importing search algorithms
import HorspoolSunday
import OriginalAlgo
import BruteForce
    
def main():
    #User input for string to be search and text file

    choice = '1'

    while(choice != '0'):
        print("\n\n1. Brute-Force")
        print("2. Boyer Moore Horspool Sunday")
        print("3. Original Algorithm")
        choice = str(input("\nEnter your choice. Enter 0 to exit."))

        if choice == '0':
            break

        dataset_name = str(input("Please enter file name: "))

        my_file = open(dataset_name)
        contents = my_file.read()
        contents = str(contents)
        my_dna = contents.rstrip("\n")

        str_userinput = str(input("Please enter search text: "))
        str_userinput = str_userinput.upper()

        if choice == '1':
            BruteForce.naive(my_dna, str_userinput)
        elif choice == '2':
            HorspoolSunday.BMHS(my_dna, str_userinput)
        elif choice == '3':
            OriginalAlgo.original(str_userinput, my_dna)
        else:
            print("Invalid Input")

    return

if __name__ == '__main__':
    main()
