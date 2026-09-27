import os
from app import add, get_secret_key

def test_add():
    assert add(2, 3) == 5

def test_secret_key_loaded():
    key = get_secret_key()
    assert key is not None
    assert len(key) > 0
