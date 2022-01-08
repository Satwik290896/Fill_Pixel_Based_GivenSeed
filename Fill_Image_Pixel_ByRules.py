'''Use BFS/Queue logic'''
'''Queue is filled when the First entry in the Queue is popped and Expanded'''
'''When Expanded to fill the Queue, Add only those that needs to be processed as '2'. 
This will make sure that 'we considering the Boxes with '1' as Boundaries and will not be processed'''
'''Algorithm will run until all the Boxes that needs to be processed are once in the Queue and gets processed completely.
Thus, Queue becomes Empty'''

'''Input and Output Examples:
1. Command Line Argument: python Image_Pixel.py [[0,0,0,0,0,0],[1,0,1,1,1,0],[0,1,0,0,0,1],[0,0,1,1,1,0],[0,0,0,0,0,0]] [2,4]
Console:
Input Image: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
Input Tuple: [2, 4]
Output: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 2, 2, 2, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]

2. Command Line Argument: python Image_Pixel.py [[0,0,0,0,0,0],[1,0,1,1,1,0],[0,1,0,0,0,1],[0,0,1,1,1,0],[0,0,0,0,0,0]] [0,0]
Console:
Input Image: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
Input Tuple: [0, 0]
Output: [[2, 2, 2, 2, 2, 2], [1, 2, 1, 1, 1, 2], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]

3. Command Line Argument: python Image_Pixel.py [[0,0,0,0,0,0],[1,0,1,1,1,0],[0,1,0,0,0,1],[0,0,1,1,1,0],[0,0,0,0,0,0]] [1,0]
Console:
Input Image: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
Input Tuple: [1, 0]
Output: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]

4. Command Line Argument: python Image_Pixel.py [[0,0,0,0,0,0],[1,0,1,1,1,0],[0,1,0,0,0,1],[0,0,1,1,1,0],[0,0,0,0,0,0]] [1,1]
Console:
Input Image: [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
Input Tuple: [1, 1]
Output: [[2, 2, 2, 2, 2, 2], [1, 2, 1, 1, 1, 2], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]
'''


import sys
import numpy as np


def check_if_Queue_Empty(Queue):
    if len(Queue)==0:
        return 1
    else:
        return 0

def Append_to_Queue(Image,Queue,M,N):
    R = Queue[0][0]
    C = Queue[0][1]
    R_High = R+1
    R_Low = R-1
    C_High = C+1
    C_Low = C-1
    
    #Append only when the Box/Node is to be filled with '2' and needs to be processed
    if R_High < M:
        if Image[R_High][C] == 0:    
            Queue.append((R_High,C))
    if R_Low >= 0:
        if Image[R_Low][C] == 0:    
            Queue.append((R_Low,C))
    if C_Low >= 0:
        if Image[R][C_Low] == 0:    
            Queue.append((R,C_Low))
    if C_High < N:
        if Image[R][C_High] == 0:    
            Queue.append((R,C_High))
    
    return Queue

def Fill_the_image(Image, M,N, Tuple, Output, Queue):
    if check_if_Queue_Empty(Queue)==1:
        return Output,Queue
    else:
        #Pop the fist node in the Queue and fill it
        Output[Queue[0][0]][Queue[0][1]] = 2
        #Expand the 1st element of Queue and Add the expanded elements to the Queue
        Queue = Append_to_Queue(Image,Queue,M,N)
        del Queue[0]
        #Call Recursively until Queue is Empty
        Output,Queue = Fill_the_image(Image, M,N, Tuple, Output, Queue)
        return Output,Queue


def main():
    A = sys.argv[1]
    B = A[2:len(A)-2].split('],[') 
    #Create the Argv[1] as a 2D-List
    Image = []
    for ele in B:
        temp = ele.split(',') 
        temp1 = []
        for j in temp: 
            temp1.append(int(j))
        Image.append(temp1)
    print('Input Image: %s' % Image)

    T = sys.argv[2]
    T1 = T[1:len(T)-1].split(',')
    #Create the Argv[2] as a Tuple/Pair
    Tuple = []
    for j in T1:
        Tuple.append(int(j))
    print('Input Tuple: %s' % Tuple)

    M = len(Image)
    N = len(Image[0])
    Output = Image
    Queue = []
    if Image[Tuple[0]][Tuple[1]] == 0: 
        Queue.append(Tuple)

    #Recursively call and Gather the Output
    Output,Queue = Fill_the_image(Image, M, N, Tuple, Output, Queue)
    print('Output: %s' % Output)
    
if __name__ == '__main__':
    main()


