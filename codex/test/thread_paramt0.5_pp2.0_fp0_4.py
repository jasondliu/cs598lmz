import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\033[31m' + '\n'.join(sys.argv) + '\033[0m\n')).start()

# import module snippets
from ansible.module_utils.basic import *

# main
def main():

    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
            state = dict(default='present', choices=['present', 'absent']),
            force = dict(default=False, type='bool'),
            debug = dict(default=False, type='bool'),
        ),
        supports_check_mode = True,
    )

    name = module.params['name']
    state = module.params['state']
    force = module.params['force']
    debug = module.params['debug']

    if debug:
        print(module.params)

    # check for required values
    if not name:
        module.fail_json(msg='name is required')

    # get current state
    cur_state = 'absent'
