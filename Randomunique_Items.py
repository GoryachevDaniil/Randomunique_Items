from random import randint


print('Enter the list items on one line separated by a space:', end=' ')
input_list = [m for m in input().split()]
N = len(input_list)

print('Enter the number of elements to sample:', end=' ')
k = int(input())

if 0 <= k <= N:
    index_list = [i for i in range(0, N)]
    output_list = []
    while N != k + len(index_list):
        index = randint(0, len(index_list) - 1)
        output_list.append(input_list[index_list[index]])
        index_list.pop(index)
    print('List:', output_list)
    print("Algorithm complexity: O(k) =", k)
else:
    print('Invalid input. Try one more times.')
