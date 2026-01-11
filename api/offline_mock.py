import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHADOW_DIR = os.path.join(BASE_DIR, "shadow_erp")

class ERPMirror:
    @staticmethod
    def read_file(filename):
        path = os.path.join(SHADOW_DIR, filename)
        if not os.path.exists(path):
            return []
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_inventory(self):
        return self.read_file("inventory.json")

    def get_products(self):
        return self.read_file("products.json")

erp_mirror = ERPMirror()
# Legacy alias for routes
offline_system = erp_mirror 
