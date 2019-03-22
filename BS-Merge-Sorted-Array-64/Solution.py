class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    @staticmethod
    def mergeSortedArray(A, m, B, n):
        # write your code here
        
        # check B empty
        if len(B) == 0:
            return A
        
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
                k -= 1
            else:
                A[k] = B[j]
                j -= 1
                k -= 1
        
        if j < 0:
            return A       
        else:
            for l in range(j + 1):
                A[l] = B[l]
        return A         



A = [1, 2, 3, None, None]
B = [4, 5]
m, n = 3, 2
print("Answer is [1, 2, 3, 4, 5], the calculation result is: " + str(Solution.mergeSortedArray(A, m, B, n)))