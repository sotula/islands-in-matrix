def bfs(x, y, matrix, shape, matrixStates):
	elementsQueue = [(x,y)]                                       # queue for an unexplored parts of island
	m, n = shape 
	moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]                    # just horizontal and vertical moves

	for (s, k) in elementsQueue:                                  # for every unexplored part of island
		for (i, j) in moves:                                      # try all posible moves from point  
			if 0 <= (s + i) < m:                                  # check does row index exist
				if 0 <= (k + j) < n:                              # check does column index exist
					if not matrixStates[s+i][k+j]:                # check is it unexplored
						if matrix[s + i][k + j] == 1:             # check is it part of island
							elementsQueue.append((s + i, k + j))  # append to unexplored parts of island
		matrixStates[s][k] = True                                 # mark that point is explored 
	return matrixStates

def get_islands_number_bfs(matrix, shape):
	m, n = shape
	matrixStates = [[False for i in range(n)] for j in range(m)] # create matrix for checking were we in point
	islandsCnt = 0
	for i in range(m):
		for j in range(n):
			if matrix[i][j] and not matrixStates[i][j]: # if point is part of island and it's not visited before
				matrixStates = bfs(i, j, matrix, (m, n), matrixStates)
				islandsCnt += 1
	return islandsCnt