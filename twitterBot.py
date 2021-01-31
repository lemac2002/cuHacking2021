
def load_puzzle(filename):
    '''
     Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
        '''
    
    name_file = [] 
    with open(filename, "r") as f:
        for line in f:
            name_file.append( [str(val) for val in line.strip().split(",")] )
    return name_file

def main():
    print("Welcome to Matei's Sudoku Game")
    filename = input("Please enter in your sudoku puzzle file:")
    names = load_puzzle(filename)
    print(names)

# Guard for main function - do NOT remove or change 
if __name__ == "__main__":
    main()


