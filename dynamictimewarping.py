class DTW:
    def __init__(self):
        pass

    def setup_cost_matrix(self, n, m):
        #build cost matrix
        cost_matrix = [[(0,None) for i in range(m+1)] for j in range(n+1)]
            
        #initialise cost matrix
        cost_matrix[0][0] = (0, None)

        for i in range(1, n+1):
            cost_matrix[i][0] = (float("inf"), None)

        for j in range(1, m+1):
            cost_matrix[0][j] = (float("inf"), None)

        return cost_matrix

    def warp(self, x, y):
        #Build Cost Matrix

        n = len(x)
        m = len(y)

        cost_matrix = self.setup_cost_matrix(n, m)

        #calculate cost matrix
        for i in range(1, n+1):
            for j in range(1, m+1):
                distance = abs(x[i-1] - y[j-1])
                
                match = cost_matrix[i-1][j-1][0]
                insertion = cost_matrix[i-1][j][0]
                deletion = cost_matrix[i][j-1][0]

                op = None
                take = min(match, insertion, deletion)
                if take == match: op = "Match"
                if take == insertion: op = "Insert"
                if take == deletion: op = "Delete"

                cost_matrix[i][j] = (distance + take, op)

        #compute alignment path and cost
        alignment_cost = cost_matrix[n][m][0]

        
        index = (n, m)
        alignment_path = [index]

        while index != (0,0):
            i = index[0]
            j = index[1]

            curr = cost_matrix[i][j]
            op = curr[1]

            if op == "Match": index = (i-1, j-1)
            if op == "Insert": index = (i-1, j)
            if op == "Delete": index = (i, j-1)

            alignment_path.append(index)

        return alignment_cost, alignment_path[::-1]

dtw = DTW()

#An example
X = [0,2,0,1,0,0]
Y = [0,0,0.5,2,0,1,0]

print(dtw.warp(X, Y))
