import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL) # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) # KeyboardInterrupt: Ctrl-C

def real_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="/home/hadoop/disk1/jd_competition_data/")
    parser.add_argument("--week_day", type=int, default=0)
    parser.add_argument("--action_file", default="jdata_action.csv")
    parser.add_argument("--user_file", default="jdata_user.csv")
    parser.add_argument("--product_file", default="jdata_product.csv")
    parser.add_argument("--comment_file", default="jdata_comment.csv")
    parser.add_argument("--output_file", default="jdata_train.csv")
    parser.add_argument("--start_day", type=int
