import types
types.ModuleType("http.client")

def config(URL, user, password, agent, dir_report, proxy=None, proxy_auth=None):
    variables.URL = URL
    variables.user = user
    variables.password = password
    variables.agent = agent
    variables.dir_report = dir_report
    variables.proxy = proxy
    variables.proxy_auth = proxy_auth
    variables.reporters = []
    variables.publishers = []
    variables.plugins = []
    variables.plugins_dict = {"nmap":[], "dnsrecon":[], "msf":[]}
    variables.scans = {}
    variables.cmd_options = {}
    variables.verbose_level = 0
    variables.masscan_rate = 100
    variables.nmap_rate = 0

