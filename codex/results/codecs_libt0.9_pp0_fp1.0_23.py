import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

################################################################################
#                                                                              #
#                           TEXT DATA PRE-PROCESSING                           #
#                                                                              #
################################################################################
dataset = pd.read_csv('G:/Project/Data Science/Sentiment Analysis/Sentiment Analysis/review.csv')
df = pd.DataFrame(dataset)

df['Label'].value_counts()

df = df.drop(['Id'],axis='columns')
df = df.drop(['ProductId'],axis='columns')
df = df.drop(['UserId'],axis='columns')
df = df.drop(['ProfileName'],axis='columns')
df = df.drop(['HelpfulnessNumerator'],axis='columns')
df = df.drop(['HelpfulnessDenominator'],axis='columns')
df = df.drop(['Time'],axis='columns')
df = df.drop(['
