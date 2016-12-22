import numpy as np


class AnalysisData:
    def __init__(self, file):
        self.file = file
        self.rules = {}
        self.mte = {}
        self.rewrites = 0
        self.execution_time = ""
        self.nelements = 0
        self.mean = 0
        self.std = 0
        self.max = 0
        self.min = 0

    def read(self):
        whole_file = self.file.read()
        rules_string = whole_file[:whole_file.find("rewrites:")]
        model = whole_file[whole_file.find("rewrites:"):]

        self.analyzerules(rules_string)
        self.analyzemodel(model)

    def analyzerules(self, rules_string):
        for line in rules_string.split('\n'):
            if line.startswith('mte '):
                mte_key = AnalysisData.get_mte_name(line)
                if self.mte.get(mte_key):
                    self.mte[mte_key] += 1
                else:
                    self.mte[mte_key] = 1
            elif line.startswith(' -> '):
                rule_key = AnalysisData.get_rule_name(line)
                if self.rules.get(rule_key):
                    self.rules[rule_key] += 1
                else:
                    self.rules[rule_key] = 1

    def analyzemodel(self, model):
        self.rewrites = int(model[(model.find(":") + 2):model.find(" ", model.find(":") + 2)])
        self.execution_time = model[model.find("(")+1:model.find(")")-4]
        resp_time_values = AnalysisData.crop_response_time(model)
        self.nelements = len(resp_time_values)
        self.mean = np.mean(resp_time_values)
        self.max = np.max(resp_time_values)
        self.min = np.min(resp_time_values)
        self.std = np.std(resp_time_values)


    def crop_response_time(model):
        aux = model[model.find("allRT@ObResponseTime@pcmflatten"):]
        # crop starting of the Sequence
        aux = aux[aux.find("{") + 1:]
        # crop ending of the Sequence
        aux = aux[:aux.find("}")]
        # cleaning it up!
        aux = aux.replace("\n", "")
        aux = aux.replace(" ", "")
        # list of values
        list_emotions_str = aux.split('#')
        list_emotions_values = []
        for pair in list_emotions_str:
            if [pair] == pair.split('/'):
                list_emotions_values.extend([float(str(pair))])
            else:
                aux_tuple = pair.split('/')
                list_emotions_values.extend([float(str(aux_tuple[0])) / float(str(aux_tuple[1]))])
        return list_emotions_values
    crop_response_time = staticmethod(crop_response_time)

    def get_mte_name(line):
        return line[line.find(' ') + 1:line.find(' ', line.find(' ') + 1)]
    get_mte_name = staticmethod(get_mte_name)

    def get_rule_name(line):
        return line[4:line.find(' ', 4)]
    get_rule_name = staticmethod(get_rule_name)
