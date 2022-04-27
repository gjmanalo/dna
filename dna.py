import csv
import sys
value = []
longest_run = []
def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        return(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        database = list(reader)
        #print(database)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as f:
        sequence = f.read()
        #print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    #print(len(reader.fieldnames))
    for i in range(1, len(reader.fieldnames)):
        subsequence = reader.fieldnames[i]
        longest_run.append(longest_match(sequence,subsequence))
    #print(longest_run[0:])
    
    # TODO: Check database for matching profiles
    keys = reader.fieldnames[1:]
    #print(keys)
    for i in range(len(database)):
        check = 0
        for j in range(len(keys)):
                if longest_run[j] == int((database[i][keys[j]])):
                    check = check + 1
                if check == (len(keys)):
                    print(database[i]['name'])
                    return(0)
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
