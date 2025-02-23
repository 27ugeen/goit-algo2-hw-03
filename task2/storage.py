from BTrees.OOBTree import OOBTree

class ProductStorage:
    def __init__(self):
        """Ініціалізація сховищ OOBTree та Dict"""
        self.tree = OOBTree()
        self.dict_store = {}

    def add_item_to_tree(self, item):
        """Додає товар у OOBTree"""
        self.tree[item["ID"]] = item

    def add_item_to_dict(self, item):
        """Додає товар у стандартний словник"""
        self.dict_store[item["ID"]] = item

    def load_items(self, items):
        """Додає всі товари у обидві структури"""
        for item in items:
            self.add_item_to_tree(item)
            self.add_item_to_dict(item)