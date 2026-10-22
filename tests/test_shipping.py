from shop.shipping import cache_key, is_admin, shipping_cost


def test_shipping_cost_light_and_heavy():
    assert shipping_cost(5) == 9.99
    assert shipping_cost(25) == 19.99


def test_is_admin(monkeypatch):
    monkeypatch.setenv("ADMIN_PASSWORD", "pw")
    assert is_admin("pw")
    assert not is_admin("nope")


def test_cache_key_is_a_sha256_hex_digest():
    assert len(cache_key(1)) == 64
    assert cache_key(1) != cache_key(2)