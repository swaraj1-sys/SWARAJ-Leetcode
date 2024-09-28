class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashTable = {}
        count = 0
        for row in grid:
            row_tuple = tuple(row)
            hashTable[row_tuple] = hashTable.get(row_tuple,0) +1
        for col in zip(*grid):
            col_tuple = tuple(col)
            count += hashTable.get(col_tuple,0)
        return count

        



        
        