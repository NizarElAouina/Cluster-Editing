# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:19:35 2023

@author: nizar
"""
import numpy as np
from itertools import combinations

def find_squares_ones(matrix):
    squares = []                    # initialize an empty list to store the squares of ones
    for i in range(len(matrix)):    # loop through the rows of the matrix
        for j in range(i+1):  # loop through the columns, but only the triangular half bottom of the adjacency matrix.
            if matrix[i][j] == 1:        # if the current element is 1, start looking for a square
                square_size = 1  # start with a square of size 1
                # keep increasing the size of the square as long as all the elements within the square are 1's
                while i + square_size < len(matrix) and j + square_size < len(matrix[i]) and all(matrix[x][y] == 1 for x in range(i, i + square_size + 1) for y in range(j, j + square_size + 1)):
                    square_size += 1
                # if we find a square of size greater than 1, add it to the list of squares
                if square_size > 1:
                    squares.append([[1]*square_size]*square_size)
    return squares  # return the list of squares of ones

def find_squares(matrix):
    squares = []
    sizes = []
    for i in range(len(matrix)):   # initialize an empty list to store the squares of ones
        for j in range(i+1):       # loop through the rows of the matrix
            if matrix[i][j] == 1:  # loop through the columns, but only the triangular half bottom of the adjacency matrix.
                square_size = 1    # if the current element is 1, start looking for a square
                # start with a square of size 1
                # keep increasing the size of the square as long as all the elements within the square are 1's
                while i + square_size < len(matrix) and j + square_size < len(matrix[i]) and all(matrix[x][y] == 1 for x in range(i, i + square_size + 1) for y in range(j, j + square_size + 1)):
                    square_size += 1
                    # i + square_size < len(matrix) : ensures that our square bottom row is inside our matrix
                    # j + square_size < len(matrix[i]) : ensures that the right column of the square is inside it too
                    # all(matrix[x][y] == 1 for x in range(i, i + square_size + 1) for y in range(j, j + square_size + 1)) : ensures that all element of the square is 1
                # if we find a square of size greater than 1, add it to the list of squares and sizes
                if square_size > 1:
                    squares.append([(i, j), (i + square_size - 1, j + square_size - 1)]) # Get the sizes in a list
                    sizes.append(square_size)
    return squares, sizes

def find_squares_boolean(matrix):
    squares = []
    sizes = []
    found_squares = False
    for i in range(len(matrix)):
        for j in range(i+1):
            if matrix[i][j] == 1:
                square_size = 1
                while i + square_size < len(matrix) and j + square_size < len(matrix[i]) and all(matrix[x][y] == 1 for x in range(i, i + square_size + 1) for y in range(j, j + square_size + 1)):
                    square_size += 1
                if square_size > 1:
                    squares.append([(i, j), (i + square_size - 1, j + square_size - 1)])
                    sizes.append(square_size)
                    found_squares = True
    if found_squares:
        return squares, sizes
    else:
        return False

def find_squares2(matrix):
    squares = []
    for i in range(len(matrix)):
        for j in range(i+1):
            if matrix[i][j] == 1:
                square_size = 1
                while i + square_size < len(matrix) and j + square_size < len(matrix[i]) and all(matrix[x][y] == 1 for x in range(i, i + square_size + 1) for y in range(j, j + square_size + 1)):
                    square_size += 1
                if square_size > 1:
                    squares.append([(i, j), (i + square_size - 1, j + square_size - 1), square_size])
    return squares

def extract_first_elements_x(lst):
    index = []
    for inner_list in lst:
        inner_result = []
        for tup in inner_list:
            inner_result.append(tup[0])
        index.append(tuple(inner_result))
    return index

def extract_first_elements_y(lst):
    index = []
    for inner_list in lst:
        inner_result = []
        for tup in inner_list:
            inner_result.append(tup[1])
        index.append(tuple(inner_result))
    return index

def index_of_biggest_value(lst):
    max_val = max(lst)
    max_index = lst.index(max_val)

    if lst.count(max_val) == 1:
        return max_index

    closest_index = None
    min_distance = len(lst)

    for i, val in enumerate(lst):
        if val == max_val:
            distance = abs(i - max_index)
            if distance < min_distance:
                closest_index = i
                min_distance = distance

    return closest_index

def get_element_combination(index,result_x,result_y):
    u = result_x[index]
    v = result_y[index]
    return u,v

def get_numbers_between_tuples(tuples):
    start = min([min(t) for t in tuples])
    end = max([max(t) for t in tuples])
    return [num for num in range(start, end+1)]


def get_combinations(lst):
    # Generate all 2-dimensional combinations of the numbers in the list
    combos = combinations(lst, 2)
    
    # Filter out any tuples that have a length other than 2
    valid_combos = [combo for combo in combos if len(combo) == 2]
    
    return valid_combos

def write_tuples_to_file(tuples_list, filename):
    with open(filename, "a") as file:
        for tpl in tuples_list:
            incremented_tpl = (tpl[0] + 1, tpl[1] + 1)
            file.write(str(incremented_tpl[0]) + " " + str(incremented_tpl[1]) + "\n")

def set_triangular_rows_to_zero(matrix, row_indexes):
    for i in row_indexes:
        matrix[i, :i] = 0
    return matrix

def make_cluster(matrix,filename):
    result, sizes = find_squares(b)
    while result : 
        x_result = extract_first_elements_x(result)
        y_result = extract_first_elements_y(result)
        biggest = index_of_biggest_value(sizes)
        elements_of_combination = get_element_combination(biggest,x_result,y_result)
        numbers = get_numbers_between_tuples(elements_of_combination)
        combo = get_combinations(numbers)
        write_tuples_to_file(combo,filename)
        matrix = set_triangular_rows_to_zero(matrix, numbers)
        result,sizes = find_squares(b)
        print("iteration")
    else : 
        print("Done")


graph = open("C:/Users/nizar/Desktop/wiss/heur/heur003.gr", 'r')
p,cep,n_vertices, n_edges=graph.readline().split()    #get first line of data in variables
adjacency_matrix = [[0] * int(n_vertices) for _ in range(int(n_vertices))]  #Declare a n_edges dimension matrix full of zeros 
for line in graph:     #Traverse the matrix
    u, v = map(int, line.split())    #Split the line into two variables since we have 2 integers
    adjacency_matrix[u-1][v-1] = 1   #Replacing zeros with 1 if there is a link between 2 vertices
    adjacency_matrix[v-1][u-1] = 1
#print(adjacency_matrix)
a=np.matrix(adjacency_matrix)        #W
b=np.tril(a)
make_cluster(b,"C:/Users/nizar/Desktop/S2/IA/cluster2")
