# 0100020000A2B02B112424262701

def main():
    while True:
        # Get dna input from user
        dna = input("Enter DNA sequence: ")

        # pad the DNA to 64 characters
        dna = dna.ljust(64, '0')

        # Convert Hex to int
        dna = int(dna, 16)
    
        print(dna)


if __name__ == "__main__":
    main()
