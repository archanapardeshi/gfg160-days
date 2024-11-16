    def getSecondLargest(self, arr):
        # Code Here
        max =-1
        max2=-1
        if len(arr)<2:
            return -1
        
        for ele in arr:
            if ele>max2 and ele<max:
                # max = 
                max2 = ele
            if ele>max:
                max2 = max
                max =ele
        return max2
