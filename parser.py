import re
import requests
import yaml
import tldextract
from urllib.parse import urlparse
from pprint import pprint


def get_list(url):
    response = requests.get(url)
    return response.text

class Parser:
    def __init__(self, url, list_type):
        self._url = url
        self._list_type = list_type

    def parse(self, _get_list=get_list):
        text = _get_list(self._url)
        text = self.sanitize(text)

        if self._list_type == "ip domain":
            raw_domains = self.extract_ip_domain(text)
            domains = self.filter_valid_domains(raw_domains)
            return domains
        
        if self._list_type == "domain":
            raw_domains = self.extract_domain(text)
            domains = self.filter_valid_domains(raw_domains)
            return domains

        if self._list_type == "url":
            raw_domains = self.extract_url(text)
            domains = self.filter_valid_domains(raw_domains)
            return domains

        raise Exception("list_type is invalid")

    def sanitize(self, blacklist):
        output = re.sub("#.*?\n", "", blacklist)
        output = re.sub("\n+", "\n", output)
        return output


    def extract_ip_domain(self, blacklist):
        result = re.findall(".+?[\t ]+(.+)", blacklist)
        return result

    def extract_domain(self, blacklist):
        result = re.findall("[\t ]*(.+)", blacklist)
        return result

    def extract_url(self, blacklist):
        result = [urlparse(url).netloc for url in blacklist.splitlines()]
        return result


    def filter_valid_domains(self, blacklist):
        def predicate(x):
            extracted = tldextract.extract(x)
            return extracted.suffix != ""

        return tuple(filter(predicate, blacklist))
