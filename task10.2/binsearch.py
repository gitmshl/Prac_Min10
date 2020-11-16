
class BinSearch:

    def __init__(self):
        pass

    def search(self, arr, key):
        l, r = 0, len(arr)
        while r - l > 1:
            mid = int((r + l) / 2)
            if arr[mid] <= key:
                l = mid
            else:
                r = mid
        
        if l >= len(arr):
            return -1
        return l if arr[l] == key else -1