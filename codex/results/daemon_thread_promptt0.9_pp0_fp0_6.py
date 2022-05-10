import threading
# Test threading daemon
from solve_distributed_write import SolveDistributedWrite

def main():
    # Create solver
    s = SolveDistributedWrite("127.0.0.1", 24242, 1)
    
    
if __name__ == "__main__":
    main()
