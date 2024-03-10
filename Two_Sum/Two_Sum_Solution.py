class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):              #Checks the amount of numbers in the array and iterates i through them
            for j in range(i+1, len(nums)):     #j starts from the next number from where i is and iterates theough the length of numbers in i
                if nums[i] + nums[j] == target: #Adds the number in i and j and then compares it to the target value,
                    return [i, j]               #If true, it prints the position of the two values in the array
        return []
