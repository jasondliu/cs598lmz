import bz2
bz2file = '../meta/threads_all.csv.bz2'
from pathlib import Path
if not Path(bz2file).is_file():
    print("create bz2 file")
    with bz2.BZ2File(bz2file, 'w') as f:
        for line in df_dummy_threads_threads.index:
            d = df_dummy_threads_threads.loc[line].to_json(force_ascii=False)
            f.write(bytes(d+'\n','utf-8'))
else:
    print("bz2 file exists")
# with bz2.BZ2File(bz2file, 'r') as f:
#     for line in f:
#         print(line)
# df_dummy_threads_posts_json = pd.DataFrame(df_dummy_threads_posts).to_json(force_ascii=False)
# df_dummy_threads_posts_json

# print(yaml.dump(
