import threading
# Test threading daemon
from threading import Thread

from core.Parameters import Parameters
from core.main.LookupTable import LookupTable
from core.main.OutputFile import OutputFile
from core.index.Index import Index
from core.index.Index import CV2 as Dx1
from core.index.Index import CV3 as Dx2
from core.index.Index import CV4 as Dx3
from core.index.Index import CV5 as Dx4
from core.index.Index import CLV0 as CLI


def main(t, *args):
    par = Parameters()
    par.read_parameters()
    par.read_tf_parameters(t)
    o = OutputFile()
    o.create(par.output)
    o.write_output(par)
    if par.indexation == 'ALL':
        par.indexation = 'DX1,DX2,DX3,DX4,CLI'
    main_kit = [Index, Index, Index, Index, Index]
    main_kit[0].main_index[0] = Dx1
    main_kit
