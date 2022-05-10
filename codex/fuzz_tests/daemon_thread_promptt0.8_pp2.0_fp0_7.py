import threading
# Test threading daemon

def f(name):
    print('hello', name)

t = threading.Thread(target=f, args=('alice',))
t.start()
t.join()
# Test multiprocessing daemon

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    p.join()
# Applying threading to the multiple target locations

def actor_solver_function_for_multiple_actors(p_actor, p_actor_mover_object, p_percept_object):  
    actor_name = p_actor.name
    percept_location = p_percept_object.location
    #print("actor name", actor_name, "percept location", percept_location)
    actor_location = p_actor.location
    #print("actor location", actor_location)
    actor_mover_function = p_actor_mover_object.move_actor_to_
