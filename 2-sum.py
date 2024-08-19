def two_sum(nums, target):
    # Dictionary to store the indices of the elements
    num_to_index = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement of the current element
        complement = target - num

        # If the complement is found in the dictionary, return the indices
        if complement in num_to_index:
            return [num_to_index[complement], i]

        # Otherwise, store the index of the current element in the dictionary
        num_to_index[num] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
