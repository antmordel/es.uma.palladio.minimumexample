import json

class PalladioData:
    def __init__(self, file, case_study, time):
        self.file = file
        self.case_study = case_study
        self.time = time
        self.response_time = -1

    def read(self):
        f = open(self.file)
        parsed_json = json.load(f)
        try:
            self.response_time = parsed_json.get(self.case_study).get(self.time)
        except AttributeError:
            self.response_time = -1
        return self.response_time
