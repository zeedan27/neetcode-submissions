class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0;
        count = 0;
        for i in nums:
            if i != 1:
                count = 0;
                continue;
            
            count += 1;
            if count > max_num:
                max_num = count;
        
        return max_num;
    


          

                
                