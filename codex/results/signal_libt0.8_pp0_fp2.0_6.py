import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on ctrl-c

#==============================================================================
# Export global parameters
#==============================================================================

__all__ = ['START', 'STOP', 'RESET',
           'START_SCAN', 'STOP_SCAN', 'TRIGGER', 'PRESET_ADD', 'PRESET_REMOVE',
           'PRESET_MOVE', 'PRESET_CLEAR',
           'ERROR', 'SCAN', 'PRESETS', 'VIEW',
           'PRESET_ADDED', 'PRESET_REMOVED', 'PRESET_MOVED', 'PRESET_CLEARED', 'SCANNED',
           'VIEW_SELECTED',
           'BASE_URL', 'START_SCAN_URL', 'STOP_SCAN_URL', 'TRIGGER_URL',
           'PRESET_ADD_URL', 'PRESET_REMOVE_URL', 'PRESET_MOVE_URL',
           'PRESET_CLEAR_URL', 'RESET_URL',
          
