list_of_items = [
    {"title": "Modrá kravata", "price": 239, "in_stock": True},
    {"title": "Luxusní psací pero", "price": 1599, "in_stock": True},
    {"title": "Degustační balíček kávy", "price": 599, "in_stock": True},
    {"title": "Parfém", "price": 559, "in_stock": False},
    {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True},
    {"title": "Sklenice na víno", "price": 799, "in_stock": True},
    {"title": "Fitness náramek", "price": 2399, "in_stock": False},
]

for item in list_of_items:
    if item["price"] in range(500, 1001) and item["in_stock"]:
        print(f"Vybraný dárek je {item['title']}")
        break