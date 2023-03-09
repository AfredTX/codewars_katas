"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""
from urllib.parse import urlparse


def domain_name(url):
    r = urlparse(url)
    objections = ["www", "com", "co", "ru", "org", "net"]
    domain = r.path.split(".") if r.netloc == '' else r.netloc.split(".")
    for i in domain:
        if i not in objections:
            return i