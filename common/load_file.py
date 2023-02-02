import yaml


def load_yaml(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)




# if __name__ == '__main__':
#     d = load_yaml('../data/data.yaml')
#     print(d)