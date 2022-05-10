import weakref
from srhd_simulation import Simulation

class FluxBudget(object):
    def __init__(self, simulation, flux_fname):
        self.simulation = weakref.ref(simulation)
        self.flux_fname = flux_fname
        self.flux_fh = open(self.flux_fname, "w")
        self.flux_fh.write("# Time   dY      dZ      dVy     dVz     dV_rad\n")
        self.flux_fh.flush()

    def fill_grid(self, grid, quantity, num_ghosts):
        patch_num_ghosts = num_ghosts * self.simulation().num_patches
        grid.fill_halo(quantity, patch_num_ghosts)
        grid.fill_guard_cells(quantity, patch_num_ghosts)

    def write_fluxes(self, grid_data, ghost_cell_size=0):
        grid_dims = self.simulation().solver.grid
