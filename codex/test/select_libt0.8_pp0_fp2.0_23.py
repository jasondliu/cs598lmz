import selectors

import environment
import policy


if __name__ == '__main__':
    opt = 'global'

    def best_action(state, q_fn, agent_idx):
        best_vals = np.max(q_fn(state), axis=1)
        best_actions = np.argmax(q_fn(state), axis=1)
        if agent_idx == -1:
            return best_actions
        else:
            return best_actions[:, agent_idx]

    def optimal_action(state, agent_idx):
        if opt == 'local':
            return environment.locally_optimal_action(state)
        elif opt == 'global':
            if agent_idx == -1:
                return environment.globally_optimal_action(state)
            else:
                return environment.globally_optimal_action(state)[:, agent_idx]
        else:
            return 0

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

