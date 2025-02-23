import networkx.algorithms.flow as flow

def compute_max_flow(G):
    """Функція для обчислення максимального потоку в графі"""
    
    G.add_node("Джерело")
    G.add_node("Стік")

    G.add_edge("Джерело", "Термінал 1", capacity=60)
    G.add_edge("Джерело", "Термінал 2", capacity=50)

    for store in [f"Магазин {i}" for i in range(1, 15)]:
        G.add_edge(store, "Стік", capacity=30)

    flow_value, flow_dict = flow.maximum_flow(G, "Джерело", "Стік")
    
    return flow_value, flow_dict