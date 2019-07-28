import pytest

import process_packages as app


@pytest.mark.parametrize("i", [i for i in range(1, 23)])
def test_app(i):
    with open('tests/{:02d}'.format(i), 'r') as f:
        all_lines = f.readlines()

    with open('tests/{:02d}.a'.format(i), 'r') as f:
        output_line = list(map(int, f.readlines()))
    input_values = all_lines
    output = []

    def mock_input():

        return input_values.pop(0)
    app.input = mock_input
    app.print = lambda s: output.append(s)
    app.main()

    assert output == output_line
