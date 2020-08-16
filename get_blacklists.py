import yaml
from pprint import pprint
from parser import Parser
from multiprocessing import Pool
from glob import glob
from pathlib import Path

def get_blacklist(name, parameters):
    print(name)
    parser = Parser(parameters["url"], parameters["format"])
    domain_list = parser.parse()

    Path("blacklists").mkdir(parents=True, exist_ok=True)

    with open("blacklists/"+name + ".blacklist.txt", "w") as f:
        f.write("\n".join(domain_list))



if __name__ == "__main__":
    with open("config.yml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    p = Pool()
    p.starmap(get_blacklist, config.items())

    tmp = []
    for b in glob("blacklists/*.txt"):
        with open(b, "r") as input_file:
            data=input_file.read()
            lines = data.splitlines()
            tmp.extend(lines)

    tmp = sorted(set(tmp))

    with open("blacklist.txt", "w") as output_file:
        data = "\n".join(tmp)
        output_file.write(data)