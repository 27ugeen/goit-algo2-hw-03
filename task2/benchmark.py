import timeit
from data_loader import load_data
from storage import ProductStorage
from queries import ProductQueries

FILENAME = "generated_items_data.csv"
items = load_data(FILENAME)

print(f"🔹 Total items loaded: {len(items)}")

storage = ProductStorage()
storage.load_items(items)

queries = ProductQueries(storage)

min_price, max_price = 10, 50

tree_time = timeit.timeit(lambda: queries.range_query_tree(min_price, max_price), number=100)

dict_time = timeit.timeit(lambda: queries.range_query_dict(min_price, max_price), number=100)

print(f"\n📌 Benchmark Results:")
print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

# Додатковий аналіз
if tree_time < dict_time:
    print("\n✅ OOBTree працює швидше за Dict для діапазонних запитів.")
else:
    print("\n⚠️ Dict працює швидше за OOBTree. Це може бути через малий набір даних або інші фактори.")