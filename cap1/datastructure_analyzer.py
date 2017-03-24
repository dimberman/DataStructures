

class BigOAnalyzer(object):
    def __init__(self, data_structure):
        self._data_structure = data_structure

    @property
    def data_structure(self):
        return self._data_structure

    @data_structure.setter
    def data_structure(self, ds):
        self._data_structure = ds

    # TODO I don't like that this class is directly reading from files.
    # It should take in a list of lines and act accordingly

    def test_input(self, lines):
        num_lines = len(lines)
        max_steps = 0
        avg = 0.0
        for l in lines:
            curr = self.data_structure.insert(l)
            max_steps = max(max_steps, curr)
            avg = avg + curr
        avg /= num_lines

        print "for inputting {} lines the average was {} and the max steps was {}".format(num_lines, max_steps, avg)

    def test_lookup(self, lines):
        num_lines = len(lines)
        max_steps = 0
        avg = 0.0
        for l in lines:
            curr = self.data_structure.lookup(l)
            max_steps = max(max_steps, curr)
            avg = avg + curr
        avg /= num_lines

        print "for deleting {} lines the average was {} and the max steps was {}".format(num_lines, max_steps, avg)

    def test_delete(self, path, num_lines):
        f = open(path, 'r')
        max_steps = 0
        avg = 0.0
        for i in range(0, num_lines):
            curr_line = f.readline()
            curr = self.data_structure.lookup(curr_line)
            max_steps = max(max_steps, curr)
            avg = avg + curr

        avg /= num_lines
        print "for {} lines the average was {} and the max steps was {}".format(num_lines, max_steps, avg)
