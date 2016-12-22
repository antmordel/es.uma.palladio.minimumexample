import sys
from AnalysisData import AnalysisData
from PalladioData import PalladioData

palladio_file ='palladio/case_studies.json'

errors = [10, 20]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception('Incorrect number of args! use: <filename> maudefilename')

    data = AnalysisData(open(sys.argv[1]))
    palladio = PalladioData(palladio_file, sys.argv[2], sys.argv[3])
    data.read()
    rt = palladio.read()
    print(" -- Execution stats")
    print("  #rewrites: {}".format(data.rewrites))
    print("  cpu time:  {}".format(data.execution_time))
    print(" -- Descriptive analysis")
    print('  #elements: {}'.format(data.nelements))
    print("  mean:      {}".format(data.mean))
    print("  sd:        {}".format(data.std))
    print("  max:       {}".format(data.max))
    print("  min:       {}".format(data.min))

    if rt > -1:
        diff = abs(rt - data.mean)
        res = diff * 100 / data.mean
        print(" -- Comparison")
        if res < errors[0]:
            print('\033[32m    Palladio <{}>  eMotions <{:.4f}> --> {:.2f}% <--\033[m'.format(rt, data.mean, res))
        elif res < errors[1]:
            print('\033[33m    Palladio <{}>  eMotions <{:.4f}> --> {:.2f}% <--\033[m'.format(rt, data.mean, res))
        else:
            print('\033[31m    Palladio <{}>  eMotions <{:.4f}> --> {:.2f}% <--\033[m'.format(rt, data.mean, res))
    # printing dictionary
    print(" -- Rules/mtes applications")
    print("   #rules_applications: ", sum(data.rules.values()))
    table_format = '{:>35}{:>20}{:>20}'
    print(table_format.format("e-Motions Action", "Rules", "MTEs"))
    print(table_format.format("-" * 30, "-" * 18, "-" * 18))
    for rule in data.rules.keys():
        aux_rule = rule[:rule.find('@')]
        n_rules = data.rules.get(rule) if data.rules.get(rule) else 0
        n_mte = data.mte.get(aux_rule) if data.mte.get(aux_rule) else 0
        print(table_format.format(aux_rule, n_rules, n_mte))
