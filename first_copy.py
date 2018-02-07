import survey

# copying Mean from thinkstats.py so we don't have to deal with
# importing anything in Chapter 1

def Mean(t):
    return float(sum(t)) / len(t)


def PartitionRecords(table):

    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        if p.outcome != 1:
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)

    return firsts, others


def Process(table):

    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = Mean(table.lengths)


def MakeTables(data_dir='.'):

    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    firsts, others = PartitionRecords(table)

    return table, firsts, others


def ProcessTables(*tables):

    for table in tables:
        Process(table)


def Summarize(data_dir):

    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)

    print('Number of first babies', firsts.n)
    print('Number of others', others.n)

    mu1, mu2 = firsts.mu, others.mu

    print('Mean gestation in weeks:')
    print('First babies', mu1)
    print('Others', mu2)

    print('Difference in days', (mu1 - mu2) * 7.0)


def main(name, data_dir='.'):
    Summarize(data_dir)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
