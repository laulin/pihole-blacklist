from parser import get_list
import re
from pprint import pprint

if __name__ == "__main__":

    output = []
    for i in range(1000,1001000, 1000):
        url = "http://stuffgate.com/stuff/website/top-{}-sites".format(i)
        print(url)
        page = get_list(url)
        domains = re.findall(r'<td><a href=.+?target=.+>(.+)</a></td>', page)
        output.extend(domains)

    with open("top_1000000.txt", "w") as f:
        f.write("\n".join(output))

