import json
import os

class Loader(object):

    def __init__(self):
        self.instances_dir = os.path.join(os.getcwd(), "examples", "standard")
        self.data = {}

    def load(self):
        standards_fps = sorted(os.listdir(self.instances_dir))
        for standard_fp in standards_fps:
            fn = standard_fp.replace(".json", "")
            standard_file = open(
                os.path.join(self.instances_dir, standard_fp), "r")
            
            json_loaded = json.load(standard_file)
            self.data[fn] = json_loaded
            