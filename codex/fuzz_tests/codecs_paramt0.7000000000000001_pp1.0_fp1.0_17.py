import codecs
codecs.register_error('strict', codecs.ignore_errors)

# =============================================================================
# Main
# =============================================================================

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _print_list(list):
    for item in list:
        print(item)

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app = App()
    app.run()
