class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a empty array,
        # we also have a variable that is 0, set that variable as we iterate 
        # as we iterate we replace that variable and add stuff to the array if greater or equal to 
        # But then we run into the issue where what happens if its not in order do we make it in order first? 

        # It has to be O(n) if we use sort it is not longer in O(n). Not sure if this is true. If this is not true then |
        # i feel like the question is alot easier. 

        # Output is one variable. I know we have to append it to a array and get the length of it 

        # What happens if we store it in an hashmap 

        # Looking back at what we did in previous problems, could bucket be used? If we create buckets and the assign we can see what is consecutive?

        max_length = 0
        current_length = 0
        bank = set()
        for num in nums:
            bank.add(num)


        
        # What i currently have 

        # all nums are alreadyi n the bankj. If num is -1 is not in the bank then it can be started as a sequence.

        # Now what are we doing after? We are looking for num+ 1 ( curernt num ) is in the bank if it is restart and go to the next num in nums. else current_length +=1 .
        # How can I search for the next number?
        for num in nums:
            if num - 1 not in bank:
                current_num = num
                while current_num in bank:
                    current_length += 1 
                    current_num += 1
                    if current_length > max_length:
                        max_length = current_length
                current_length = 0
        return max_length               

