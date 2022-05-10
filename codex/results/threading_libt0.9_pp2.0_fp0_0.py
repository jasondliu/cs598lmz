import threading
threading.stack_size(20000000)
numthreads = 0
svr_env = sv.Server()
svr_env.open('A')
data = sv.Data()
cmd = sv.Command()
cmd = svr_env.new_command_query()

class agent():
    def __init__(self):
        self.views = []
        self.view_ratings = []
        self.init_rand_views(10)
        #self.get_sensory_input(2)
    def init_rand_views(self, num_views):
        for i in range(0, num_views):
            row = random.randint(0, 1000)
            col = random.randint(0, 1000)
            self.views.append(sv.view_simple(row, col, 1, 1))
            self.view_ratings.append(0)
    def get_sensory_input(self, view_index):
        cmd.set_name(self.views[view_index].get_table_name
