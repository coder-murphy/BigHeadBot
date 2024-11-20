import os
import yaml

with open(os.path.join(os.path.dirname(__file__), "config.yaml")) as f:
    config = yaml.load(f,Loader=yaml.FullLoader)

class Configuration():
    def AppID() -> str:
        return config["appid"]
    
    def Token() -> str:
        return config["secret"]
