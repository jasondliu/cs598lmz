import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

radiation_options = {
    'radiation_method'     : 'RRTM',
    'RH_method'            : 'RH_from_Td',
    'radiation_lw'         : 'on',
    'radiation_sw'         : 'on',
    'rrtm_lw_nband'        : '21',
    'rrtm_sw_nband'        : '26',
    'radiation_cloud'      : 'on',
    'radiation_turb'       : 'on',
    'radiation_lw_fluxdown': 'on',
    'radiation_sw_fluxdown': 'on',
    'radiation_lw_fluxup'  : 'on',
    'radiation_sw_fluxup'  : 'on',
    'radiation_lw_net'     : 'on',
    'radiation_sw_net'     : 'on',
   
