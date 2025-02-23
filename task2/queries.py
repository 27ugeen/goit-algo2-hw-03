class ProductQueries:
    def __init__(self, storage):
        self.storage = storage

    def range_query_tree(self, min_price, max_price):
        """Швидкий пошук у OOBTree (ефективний діапазонний запит)"""
        return [item for _, item in self.storage.tree.items(min_price, max_price)]

    def range_query_dict(self, min_price, max_price):
        """Знаходить товари у діапазоні цін за допомогою dict (лінійний пошук)"""
        return [item for item in self.storage.dict_store.values() if min_price <= item["Price"] <= max_price]