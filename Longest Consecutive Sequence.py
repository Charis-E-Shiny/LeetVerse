class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = set(nums)  # Step 1: Insert all elements into a set
        max_length = 0
        
        for num in num_set:
            # Step 2: Check if this is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                current_num = num
                
                # Step 3: Count the length of the sequence
                while current_num + 1 in num_set:
                    length += 1
                    current_num += 1
                
                # Step 4: Update max_length
                max_length = max(max_length, length)
        
        return max_length  # Corrected indentation here
