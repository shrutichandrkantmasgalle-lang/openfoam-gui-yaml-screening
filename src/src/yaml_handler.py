import yaml

def write_yaml(data, filename):
    with open(filename, "w") as f:
        yaml.dump(data, f)
      
