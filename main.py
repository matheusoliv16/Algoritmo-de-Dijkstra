import heapq
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

def read_graph_from_file(filename):
    """
    Lê um arquivo de matriz de adjacência e converte para uma matriz esparsa (csr_matrix).
    
    Parâmetros:
    filename (str): O nome do arquivo que contém a matriz de adjacência.
    
    Retorna:
    csr_matrix: A matriz de adjacência em formato esparso.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    
    return csr_matrix(matrix)

def main():
    # Lê o grafo a partir do arquivo de matriz de adjacência
    graph = read_graph_from_file('adj_matrix.txt')
    
    # Executa o algoritmo de Dijkstra a partir do nó 0 (correspondente ao 'A')
    distances, _ = dijkstra(csgraph=graph, directed=False, return_predecessors=True, indices=0)
    
    # Converte o array de distâncias para um dicionário com os vértices nomeados
    distance_dict = {chr(65 + i): distance for i, distance in enumerate(distances)}
    
    # Exibe as distâncias a partir do nó inicial
    print("Menores distâncias de A:", distance_dict)

if __name__ == "__main__":
    main()
