import networkx as nx
import matplotlib.pyplot as plt

pos_fixed = {
    "Джерело": (1, 4),  # Додаємо джерело вище за термінали
    "Стік": (1, -1),  # Додаємо стік нижче магазинів
    "Термінал 1": (0, 3), "Термінал 2": (2, 3),
    "Склад 1": (-1, 2), "Склад 2": (1, 2), "Склад 3": (0, 2), "Склад 4": (2, 2),
    "Магазин 1": (-2, 1), "Магазин 2": (-1.5, 1), "Магазин 3": (-1, 1),
    "Магазин 4": (0.5, 1), "Магазин 5": (1, 1), "Магазин 6": (1.5, 1),
    "Магазин 7": (-0.5, 0), "Магазин 8": (0, 0), "Магазин 9": (0.5, 0),
    "Магазин 10": (1.5, 0), "Магазин 11": (2, 0), "Магазин 12": (2.5, 0),
    "Магазин 13": (3, 0), "Магазин 14": (3.5, 0)
}

def draw_graph(G, title="Модель логістичної мережі", flow_dict=None):
    """Функція для візуалізації графа"""
    plt.figure(figsize=(12, 7))
    nx.draw(G, pos=pos_fixed, with_labels=True, node_color="lightblue",
            edge_color="black", node_size=2500, font_size=10, font_weight="bold")

    edge_labels = {}
    for u, v, d in G.edges(data=True):
        if flow_dict and u in flow_dict and v in flow_dict[u]:
            edge_labels[(u, v)] = f"{flow_dict[u][v]}/{d['capacity']}"
        else:
            edge_labels[(u, v)] = f"{d['capacity']}"

    nx.draw_networkx_edge_labels(G, pos_fixed, edge_labels=edge_labels, font_size=10)

    plt.title(title, fontsize=14, fontweight="bold", pad=20)
    plt.show()