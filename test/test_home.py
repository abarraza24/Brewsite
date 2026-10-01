from app.brewsite import hello_world

def test_home():
    assert "Hello" in hello_world()