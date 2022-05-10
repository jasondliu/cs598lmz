import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Reading user input

def read_input(session):
    sys.stdout.write("> ")
    sys.stdout.flush()
    return sys.stdin.readline().strip()

# Updating the last seen time of a user

def update_last_seen(sender, session):
    query = """
        UPDATE `my_users`
        SET `last_seen` = NOW()
        WHERE `user_id` = "{}"
    """.format(sender)
    session.execute(query)
    session.commit()

# Random

def random_pick(items):
    return random.choice(items)

# Replying to a user

def reply(user_id, msg, session):
    update_last_seen(user_id, session)  # for loop to reply multiple messages
    query = """
        SELECT `type`
        FROM `my_users`
        WHERE `user_id` = "{}"
    """.format(user_
