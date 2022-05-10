import sys, threading

def run():
    print( "Running " + sys.version )

    from pymol import cmd
    cmd.feedback('disable', 'executive', 'actions')
    cmd.feedback('disable', 'executive', 'results')

    cmd.feedback('disable', 'symmetry objectmolecule executive')

    cmd.set('auto_zoom', 0)

    cmd.load( os.path.join( os.path.dirname(__file__), "model.pdb.gz" ), "model" )

    cmd.mset("1x180")

    cmd.turn("y", 180)
    cmd.zoom("center", 10)

    cmd.png("%s.180.png" % (os.path.splitext(__file__)[0]))

    cmd.turn("y", 180)

    cmd.png("%s.360.png" % (os.path.splitext(__file__)[0]))

    cmd.mset("1x120")

    cmd.turn("y", 120)
    cmd.zoom("center", 10)

   
