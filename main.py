"""
Created on Fri Feb 24 10:19:35 2023

@author: nizar
"""
import FunctionsCluster as cl
import numpy as np


graph = open("C:/Users/nizar/Desktop/wiss/heur/heur001.gr", 'r')
p,cep,n_vertices, n_edges=graph.readline().split()    #get first line of data in variables
adjacency_matrix = [[0] * int(n_vertices) for _ in range(int(n_vertices))]  #Declare a n_edges dimension matrix full of zeros 
for line in graph:     #Traverse the matrix
    u, v = map(int, line.split())    #Split the line into two variables since we have 2 integers
    adjacency_matrix[u-1][v-1] = 1   #Replacing zeros with 1 if there is a link between 2 vertices
    adjacency_matrix[v-1][u-1] = 1
#print(adjacency_matrix)
a=np.matrix(adjacency_matrix)        #W
b=np.tril(a)
cl.make_cluster(b,"C:/Users/nizar/Desktop/S2/IA/Clustering/cluster1")
