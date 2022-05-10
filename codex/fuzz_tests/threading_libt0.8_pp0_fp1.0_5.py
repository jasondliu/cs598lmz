import threading
threading.stack_size(67108864)

def run_simulation(field, particles, T, dt, sigma, epsilon, m,
                   temperature, save_traj, save_config):

    # set the random number generator
    np.random.seed(0)

    # set the initial positions and velocities
    init_positions = np.random.rand(particles, 3)
    init_velocities = np.random.rand(particles, 3)

    # calculate the initial energy
    init_energy = calc_energy(init_positions, sigma, epsilon, m)

    # rescale the velocities so that the initial temperature is equal to
    # the desired temperature
    init_velocities = rescale_velocities(init_velocities, init_energy,
                                         temperature, particles, m)


    # initialize the particle object
    p = Particle(particles, init_positions, init_velocities,
                 sigma, epsilon, m)

    # the list of positions to save
    saved
