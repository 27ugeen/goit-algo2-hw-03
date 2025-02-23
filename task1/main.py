from graph_data import create_graph
from graph_visualization import draw_graph
from max_flow import compute_max_flow
import pandas as pd

G = create_graph()

draw_graph(G, "Модель логістичної мережі (початкова)")

flow_value, flow_dict = compute_max_flow(G)

print(f"\n🔹 Максимальний потік у логістичній мережі: {flow_value}")

draw_graph(G, "Модель логістичної мережі (фактичні потоки)", flow_dict)


terminals = ["Термінал 1", "Термінал 2"]
terminal_flows = {t: sum(flow_dict[t].values()) for t in terminals}

print("\n📌 Потік товарів через термінали:")
for term, flow in terminal_flows.items():
    print(f"🔹 {term}: {flow} одиниць")

store_flows = {}
for store in [f"Магазин {i}" for i in range(1, 15)]:
    if store in flow_dict:
        store_flows[store] = sum(flow_dict[store].values())  # Сума всіх вхідних потоків
    else:
        store_flows[store] = 0  # Якщо магазину немає у flow_dict, потік = 0

bottlenecks = [(u, v, d["capacity"]) for u, v, d in G.edges(data=True) if flow_dict[u][v] == d["capacity"]]

print("\n📌 Маршрути, що працюють на межі пропускної здатності (вузькі місця):")
for u, v, cap in bottlenecks:
    print(f"🔹 {u} → {v} (Макс: {cap})")

df_stores = pd.DataFrame(store_flows.items(), columns=["Магазин", "Фактичний потік"])
df_stores = df_stores.sort_values(by="Фактичний потік", ascending=True)

print("\n📌 Магазини з отриманим товаром:")
print(df_stores)

low_supply_stores = df_stores[df_stores["Фактичний потік"] < 10]

if not low_supply_stores.empty:
    print("\n📌 ❗ Магазини з малим постачанням:")
    print(low_supply_stores)


print("\n📌 Вузькі місця та рекомендації щодо покращення:")
for u, v, cap in bottlenecks:
    print(f"🔹 Рекомендується збільшити пропускну здатність ребра {u} → {v} (Макс: {cap})")

# Рекомендації щодо магазинів з малим постачанням
if not low_supply_stores.empty:
    print("\n📌 Рекомендації щодо покращення постачання магазинів:")
    for _, row in low_supply_stores.iterrows():
        print(f"🔸 Магазин {row['Магазин']} отримав лише {row['Фактичний потік']} одиниць товару. "
              f"Рекомендується збільшити потік через склади або знайти альтернативні маршрути.")