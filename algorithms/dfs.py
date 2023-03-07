def dfs(x, y, matrix, shape, matrixStates):
	m, n = shape 
	moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # just horizontal and vertical moves
	matrixStates[x][y] = True

	for (i, j) in moves:                                                          # try all posible moves from point  
		if 0 <= (x + i) < m:                                                      # check does row index exist
			if 0 <= (y + j) < n:                                                  # check does column index exist
				if not matrixStates[x+i][y+j]:                                    # check is it unexplored
					if matrix[x + i][y + j] == 1:                                 # check is it part of island
						matrixStates = dfs(x+i, y+j, matrix, shape, matrixStates) # recursively mark next point of island
	return matrixStates


def get_islands_number_dfs(matrix, shape):
	m, n = shape
	matrixStates = [[False for i in range(n)] for j in range(m)]       # create matrix for checking were we in point
	islandsCnt = 0
	for i in range(m):
		for j in range(n):
			if matrix[i][j] and not matrixStates[i][j]:                # if point is part of island and it's not visited before
				matrixStates = dfs(i, j, matrix, (m, n), matrixStates) # find all points of island
				islandsCnt += 1                                        # we marked all points of island so we can add one to our counter
	return islandsCnt