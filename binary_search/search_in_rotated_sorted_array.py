from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This follows basically the same procedure as the
        # find_min_in_rotated_sorted_array problem at first, and then
        # we binary search between the boundaries we find.

        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = n - 1
        # Binary search to find the start & end indices of the original
        # array first.
        while left <= right:
            mid = (left + right) // 2
            if nums[(mid - 1) % n] < nums[mid] and nums[mid] > nums[(mid + 1) % n]:
                # found the start
                left = right + 1
            elif nums[left] > nums[mid]:
                # end of array must be in left half of search window.
                right = mid - 1
            else:
                # end of array must be in right half of search window.
                left = mid + 1
        
        # Made mistake of translating indices before necessary
        # Don't rotate L/R, only rotate mid when needed.
        start = mid + 1
        left = 0
        right = n - 1
        while left <= right:
            # Hm. Is this correct?
            mid = (left + right) // 2
            if nums[(mid + start) % n] == target:
                return (mid + start) % n
            elif nums[(mid + start) % n] < target:
                left = mid + 1
                # right = mid - 1
            else:
                # left = mid + 1
                right = mid - 1

        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))

        