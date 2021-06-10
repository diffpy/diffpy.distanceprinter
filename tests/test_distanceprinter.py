import os

from DistancePrinter.distanceprinter import main


def test_distanceprinter():
    cwd = os.getcwd()
    example_file_dir = cwd / "test_files"
    # must be cif, stru, or xyz file
    strufile = os.path.join(example_file_dir, "Ni-9008476.cif")
    # atoms typically pull from list of elements in stru output of PDFFitStructure. 'all' is always first option
    atomi = 'all'
    atomj = 'all'
    # lb and ub are lower an upper bound of distance to list in angstroms
    lb = 1
    ub = 10
    #  1 means keep duplicate atom pairs with same inter-atomic distance, 0 means not to
    comp = 1
    main(args=[strufile, atomi, atomj, lb, ub, comp, 'temp.res'])
    f = file('temp.res', 'r')
    rv0 = f.readlines()
    rv0 = ''.join(rv0)
    resultstr = rv0
    os.remove(os.path.join(cwd, 'temp.res'))
    output_file_dir = cwd / "ouputs"
    example_output = os.path.join(example_file_dir, "temp_test.res")
    f = file(example_output, 'r')
    rv1 = f.readlines()
    rv1 = ''.join(rv1)
    teststr = rv1
    assert resultstr == teststr