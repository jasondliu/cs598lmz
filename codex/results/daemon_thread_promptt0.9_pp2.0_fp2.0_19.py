import threading
# Test threading daemon

num_of_users = int(input('How many users? '))
print('Please note that if you set number of users too high, the script will take much longer time to run\n')
comments_count = 0


print('Starting...')


# Make session to store requests
client = MongoClient(
    'mongodb://localhost:27017/')

db = client.instagram  # DB name

# Get all users
coll_users = db.users  # Table name

# try:
#     coll_users.drop()
# except:
#     pass


def crawl_post_comment(post):
    try:
        post_cursor = post.comments_all
        if len(post['comments_all']):
            for comments in post_cursor:
                coll_users.find_one_and_update(
                    {'username': user['username']},
                    {'$push': {'comments_all': comments}})
                comments_count += 1
    except:
        print()

    # try:
    #     post_cursor =
