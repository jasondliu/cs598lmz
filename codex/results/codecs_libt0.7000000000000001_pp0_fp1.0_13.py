import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Tfs(object):

    def __init__(self):
        self.path = 'C:\\Users\\i309983\\PycharmProjects\\TFS_API\\'
        self.df_users = pd.read_csv(self.path + 'users.csv', encoding='utf-8')
        self.df_teams = pd.read_csv(self.path + 'teams.csv', encoding='utf-8')
        self.df_releases = pd.read_csv(self.path + 'releases.csv', encoding='utf-8')

    def get_user_story_count(self, project):
        """
        Get user stories count
        :param project:
        :return:
        """
        pass

    def get_release_info(self, project):
        """
        Get release information
        :param project:
        :return:
        """
        pass

    def get_user_info(
