def parse_input(path):
    # Read file and split into lines
    with open(path, 'r') as file:
        result = file.read().splitlines()
    # Optional: Remove any empty lines if needed
    return [line for line in result if line.strip()]


def main():
    # PART 1
    input_path = 'dec1.txt'
    input_lines = parse_input(input_path)
    left=[]
    right=[]
    total=0
    # Print out each line of the resulting list
    for line in input_lines:
        l,r = (int(x) for x in line.split())
        left.append(l)      
        right.append(r)
    for line in input_lines:    
        minimuml= min(left)
        minimumr=min(right)
        diff=abs(minimuml - minimumr)
        total = total + diff
        left.remove(min(left))
        right.remove(min(right))
    print(total)

    # PART 2
    # Calculate and print the similarity score
    score = calculate_similarity_score(left, right)
    print("Similarity Score:", score)
    
    
from collections import Counter

def calculate_similarity_score(left, right):
    # Count occurrences in the right list
    right_counts = Counter(right)
    
    # Initialize similarity score
    similarity_score = 0
    
    # Calculate the similarity score
    for num in left:
        similarity_score += num * right_counts.get(num, 0)  # Multiply by count in right list
        
    return similarity_score



# Run the main function
if __name__ == '__main__':
    main()
