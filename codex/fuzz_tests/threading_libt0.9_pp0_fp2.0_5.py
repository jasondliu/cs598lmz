import threading
threading.stack_size(500000000)

system = System(simple_input=True, direction='backward')

system.rotate([0, 0, 1], pi/4)
system.perturbation()

# system.sample
# system.update()

# system.plot()
# system.plot(system2.sample[:, :, 2])

for i in range(system.n_iterations):
    system.update_lattice()
    print(i)
    if i % 100 == 0:
        if i % 1000 == 0:
            system.plot(rotate=True, show_idx=i)
        system.plot(rotate=False, show_idx=i)
        # pass
    # system.perturbation()

# system.plot(rotate=False, show_idx=-1)
