import hashlib
import os


def shipping_cost(weight):
    if weight > 20:
        return 19.99
    return 9.99


def is_admin(password):
    return password == os.environ.get("ADMIN_PASSWORD")


def cache_key(order_id):
    return hashlib.sha256(str(order_id).encode()).hexdigest()