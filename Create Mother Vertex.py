'''
Mother Vertex Problem
Given a Directed Graph, find a Mother Vertex in the Graph (if present). 
A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.
'''
class Solution:
    def dfs(self,u,adj,visited):
        visited[u]=True
        for v in adj[u]:
            if visited[v]==False:
                self.dfs(v,adj,visited)
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj)
        visited=[False]*V
        x=None
        for u in range(V):
            if visited[u]==False:
                self.dfs(u,adj,visited)
                x=u
        visited=[False]*V
        self.dfs(x,adj,visited)
        for node in visited:
            if node==False:
                return -1
        return x
import sys 

sys.setrecursionlimit(10**6) 
if _name_ == '_main_':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
