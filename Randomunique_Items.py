from random import randint

    ## ## Make list  to take elements from. ## ## 

    
print('Enter the list items on one line separated by a space:', end=' ')
input_list = [m for m in input().split()]
N = len(input_list)


    ## ## Enter len of final list. ## ## 

print('Enter the number of elements to sample:', end=' ')
k = int(input())


    ## ## Prepear to accounting. ## ##
    
if 0 <= k <= N:                         # check added
    output_list = []                    # list to display elements
    index_list = []                     # list for accounting added indexes
    steps = 0                           # cicle counter

    
    ## ## Cicle ending only after founding entered number of elements. ## ## 
        
    while len(output_list) != k:
        index = randint(0, N - 1)
        steps += 1                      #scored how much cicles done to find all
        if index not in index_list:
            index_list.append(index)
            output_list.append(input_list[index])
          
        
    ## ## Print result of a programm. ## ##
            
    print('List:', output_list, 'make in', steps, 'steps')
    print("algorithm complexity: O(N**2) =", N**2)
    
    
    ## ## If entered number is more then len of input_list ## ##
    
else:
    print('Invalid input. Try one more times')
