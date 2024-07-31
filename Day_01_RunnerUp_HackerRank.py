"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains . The second line contains an array A[]  of  integers each separated by a space.

Constraints
    2 <= n <= 10
    -100 <= A[i] <= 100

Sample Input
    5
    2 3 6 6 5

Sample Output
    5

"""


def using_set(arr):
    if len(set(arr)) < 2:
        return None
    else:
        return sorted(list(set(arr)),reverse=True)[1]

def single_pass(arr):
    if len(arr) < 2:
        return None
    else:
        first = second = float('-inf')
        for element in arr:
            if element > first:
                second = first
                first = element
            elif first > element > second:
                second = element

    return second if second != float('-inf') else None

import heapq
def using_heap_queue(arr):
    if len(arr) < 2:
        return None
    else:
        second_largest = heapq.nlargest(2,list(set(arr)))
        return second_largest[-1]

from collections import OrderedDict 
def using_ordered_dict(arr):
    unique_arr = list(OrderedDict.fromkeys(arr))
    if len(unique_arr) < 2:
        return None
    else:
        return sorted(unique_arr,reverse=True)[1]
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"Set => {using_set(arr)}")
    print(f"Single Pass => {single_pass(arr)}")
    print(f"Heap Queue => {using_heap_queue(arr)}")
    print(f"Ordered Dict => {using_ordered_dict(arr)}")
    






