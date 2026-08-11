# Time Complexity: O(V + E)
# - Building the adjacency list takes O(V + E).
# - DFS visits each node at most once: O(V).
# - DFS checks the neighbors/edges: O(E).
#
# Space Complexity: O(V + E)
# - Adjacency list: O(V + E)
# - Visited set: O(V)
# - Recursion stack: O(V)
# - Overall: O(V + E)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            # Create adjancency list
            graph = []

            for i in range(n):
                graph.append([])

            # Add edges
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)

            # Track Visited nodes
            visited = set()

            # DFS
            def dfs(node):
                # Destination found
                if node == destination:
                    return True

                # Mark node as visited
                visited.add(node)
                
                # Check all neighbors
                for neighbor in graph[node]:
                    
                    if neighbor not in visited:
                        
                        if dfs(neighbor):
                            return True

                return False    

            # Start DFS  from source
            return dfs(source)