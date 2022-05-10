import bz2
bz2_or_no = True

# Output file
outpath = './results/'
if not os.path.exists(outpath):
    os.makedirs(outpath)

savefile = outpath + '1MGA_FIRE_LOWZ_0.9'

print('Output file is: ' , savefile)

# Load Halotools pre-calculated tables
halocat = CachedHaloCatalog(simname = 'bolshoi', redshift = 0, dz_tol = 0.001)

# Load halo catalog
halocat.halo_table = process_halo_catalog_pynbody(halocat.ptcl_table, halocat.halo_table, savepath = outpath, savefile = savefile
                                                  + '_hlist_1.00000.list')

# Load Galaxy catalog
if bz2_or_no == False:
    with open(savefile + '.pkl', 'rb') as handle:
        gal_table = pickle.load(handle)

if bz
