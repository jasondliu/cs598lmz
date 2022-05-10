import threading
threading.stack_size(67108864)
execfile("../conf.py")
execfile("../load_actions_kernel.py")
print "********** start *************"
start = time.time()

if len(sys.argv)<5:
    print "usage: python load_users_kernel.py user_id_from user_id_to step action_id"
    sys.exit(1)

user_id_from = int(sys.argv[1])
user_id_to = int(sys.argv[2])
step = int(sys.argv[3])
action_id = int(sys.argv[4])
user_id = user_id_from

i = 1
while user_id < user_id_to:
    print "loading %s %d user id:%d" %(str(datetime.datetime.now()),i,user_id)
    i = i + 1
    if len(sys.argv)==6:
        db.users_kernel.insert({"_id":user_
