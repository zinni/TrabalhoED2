graph = {
    '1' : ['2'],
    '2' : ['1','3','6'], 
    '3' : ['2','4','8'], 
    '4' : ['3','17'],
    '5' : ['10'],
    '6' : ['2'],
    '7' : ['8','12'], 
    '8' : ['3','7','9'],
    '9' : ['8'],
    '10' : ['5','11','25'],
    '11' : ['10','12','18'],
    '12' : ['7','11','19'],
    '13' : ['14','15'],
    '14' : ['13','21'],
    '15' : ['13','16'],
    '16' : ['15'],
    '17' : ['4'],
    '18' : ['11'],
    '19' : ['19','20'],
    '20' : ['19','28'],
    '21' : ['14','22','29'],
    '22' : ['21','35'],
    '23' : ['24'], 
    '24' : ['23','27'],
    '25' : ['10','26','30'],
    '26' : ['25','32'],
    '27' : ['24','28'],
    '28' : ['20','27','34'],
    '29' : ['21'],
    '30' : ['25'],
    '31' : ['32'],
    '32' : ['26','31','33'],
    '33' : ['32'],
    '34' : ['28','35'],
    '35' : ['34','36'],
    '36' : ['35', 'exit'],
    }

visited = set() # Set to keep track of visited nodes.
caminho = []

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        if node == 'exit':
            print("Você achou a saída!")
            quit()
        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, '1')