from collections import Counter
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    # Your code here
    unique = [item for item, count in Counter(arr).items() if count < 2]
    return unique[0] if unique[0] else None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")