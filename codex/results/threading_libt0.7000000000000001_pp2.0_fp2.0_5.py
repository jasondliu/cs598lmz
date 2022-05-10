import threading
threading.Thread(target=lambda: jupman.run_notebook('../tests/test_manual_solution_exercise.ipynb')).start()
 

# NOTE: if you want to check the solution
#       run test_manual_solution_exercise.ipynb
#       in the folder "tests"
 
 
 
# ===== SOLUTION



def pytest_funcarg__explorer(request):
    return Explorer(Board(9,9),(7,7))


def test_explorer_init(explorer):
    assert explorer.board.is_valid_position((7,7))
    assert explorer.board.is_valid_position((0,0))
    assert not explorer.board.is_valid_position((-1,0))
    assert not explorer.board.is_valid_position((0,-1))


def test_explorer_init_pos(explorer):
    assert explorer.pos == (7,7)
    assert explorer.x == 7
    assert explorer.y == 7
    assert explorer.pos == explorer
