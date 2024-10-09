# Solution 1 - O(n) runtime
def containsDuplicate(nums: list[int]) -> bool:
    numset = set()
    for num in nums:
        if num in numset: # Check first there's a duplicate
            return True
        numset.add(num) # otherwise add it
    return False # There are no duplicates
    

    
# Solution 2 - O(n) runtime
def containsDuplicate(nums: list[int]) -> bool:
    numset = set()
    for num in nums:
        numset.add(num)
    if len(numset) != len(nums): # Sets cannot contain duplicate values, so they would be different if there was
        return True
    else:
        return False
            

