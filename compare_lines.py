"""Script for comparing files.

"""

from absl import flags
from absl import app

flags.DEFINE_string(
    'file_path', None, 'Path to file.')
flags.DEFINE_string(
    'output_file_path', None, 'Path to output file.')

FLAGS = flags.FLAGS


def compare_lines(file_path, output_file):
    line_dict = {}

    with open(file_path, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf8') as output:
        for i, line in enumerate(lines, start=1):
            line = line.strip()  # Remove leading/trailing whitespace

            if line in line_dict:
                output.write(f"Line {i} and Line {line_dict[line]} are the same: '{line}'\n")
            else:
                line_dict[line] = i


def compare_and_remove_lines(file_path):
    lines = []
    removed_lines = []

    with open(file_path, 'r', encoding='utf8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf8') as file:
        for i, line in enumerate(lines):
            line = line.strip()  # Remove leading/trailing whitespace

            if line in lines[i + 1:] or line in removed_lines:
                removed_lines.append(line)
            else:
                file.write(line + '\n')

def main(_):
    file_path = FLAGS.file_path
    output_file_path = FLAGS.output_file_path
    compare_lines(file_path, output_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flags.mark_flag_as_required('file_path')
    flags.mark_flag_as_required('output_file_path')
    app.run(main)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
