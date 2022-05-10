import socket

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


class JenkinsCollector():

    def __init__(self, url, user, password, prefix, target, port, job_whitelist=None, job_blacklist=None):
        self.url = url
        self.user = user
        self.password = password
        self.prefix = prefix
        self.target = target
        self.port = port
        self.job_whitelist = job_whitelist
        self.job_blacklist = job_blacklist

    def collect(self):
        registry = CollectorRegistry()
        jobs = self.get_jobs()
        for job in jobs:
            if self.job_whitelist and not job["name"] in self.job_whitelist:
                continue
            if self.job_blacklist and job["name"] in self.job_blacklist:
                continue
            if job["color"] == "disabled":
                continue
