import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

THREAD_COUNT = 1

for i in range(1, 123):
    with open("C:\\Users\\Vasilis\\Desktop\\Work\\Data\\fakes\\fakes_" + str(i) + ".csv", "r") as file:
        for line in file:
            chunks = line.rstrip().split(";")
            if len(chunks) == 3:
#                 date_time_str = chunks[0]
#                 date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#                 print(date_time_obj.date(), date_time_obj.time().hour, date_time_obj.time().minute)
                print("INSERT INTO public.fake_news(url, content, retweets) VALUES ('" + chunks[1] + "', '" + chunks[2] + "
