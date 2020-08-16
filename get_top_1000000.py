from parser import get_list
import re
from pprint import pprint
from multiprocessing import Pool
import multiprocessing


def scrap_stuffgate(index):
    url = "http://stuffgate.com/stuff/website/top-{}-sites".format(index)
    print(url)
    page = get_list(url)
    domains = re.findall(r'<td><a href=.+?target=.+>(.+)</a></td>', page)
    return (index, domains)

if __name__ == "__main__":

    p = Pool(multiprocessing.cpu_count()*4)
    output = p.map(scrap_stuffgate, range(1000, 1001000, 1000))
    output = sorted(output)
    output = map(lambda x: x[1], output)
    output = [item for sublist in output for item in sublist]

    with open("top_1000000.txt", "w") as f:
        f.write("\n".join(output))

