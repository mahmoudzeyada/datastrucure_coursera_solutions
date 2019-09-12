import pytest

import job_queue as app


@pytest.mark.parametrize("i", [i for i in [1, 2, 8]])
def test_app(i):
    with open('tests/{:02d}'.format(i), 'r') as f:
        all_lines = f.readlines()

    with open('tests/{:02d}.a'.format(i), 'r') as f:
        output_lines = []
        for line in f.readlines():
            output_lines.append(list(map(int, line.split(' '))))

    input_values = all_lines
    output = []

    def mock_input():
        return input_values.pop(0)

    app.input = mock_input
    app.print = lambda s, x: output.append([s, x])
    app.main()

    assert output == output_lines
