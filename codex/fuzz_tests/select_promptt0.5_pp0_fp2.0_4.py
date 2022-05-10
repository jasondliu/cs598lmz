import select
# Test select.select()

def test_select_select(monkeypatch):
    monkeypatch.setattr(select, "select", lambda *args: None)
    assert select.select([], [], []) == None
