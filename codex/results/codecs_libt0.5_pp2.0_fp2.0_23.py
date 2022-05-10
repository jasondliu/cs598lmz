import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Deployment:
    def __init__(self, name, url, username, password, project):
        self.name = name
        self.url = url
        self.username = username
        self.password = password
        self.project = project


def get_deployments():
    with open('deployments.json') as json_file:
        data = json.load(json_file)
        deployments = []
        for deployment in data:
            deployments.append(Deployment(deployment["name"], deployment["url"], deployment["username"], deployment["password"], deployment["project"]))
        return deployments


def get_deployment(name):
    deployments = get_deployments()
    for deployment in deployments:
        if deployment.name == name:
            return deployment
    return None
