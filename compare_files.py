"""Script for comparing files.

"""

from absl import flags
from absl import app

flags.DEFINE_string(
    'file1_path', None, 'Path to file 1.')
flags.DEFINE_string(
    'file2_path', None, 'Path to file 2.')
flags.DEFINE_string(
    'output_file_path', None, 'Path to output file.')

FLAGS = flags.FLAGS


def compare_two_files(file1, file2, output_file):
    with open(file1, 'r', encoding="utf8") as f1, open(file2, 'r', encoding="utf8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    with open(output_file, 'w', encoding='utf8') as output:
        for i, line1 in enumerate(lines1, start=1):
            for j, line2 in enumerate(lines2, start=1):
                if line2 in line1:
                    output.write(f"Line {i} in {file1} matches Line {j} in {file2} are the same: {line2}")


def main(_):
    file1_path = FLAGS.file1_path
    file2_path = FLAGS.file2_path
    output_file_path = FLAGS.output_file_path
    compare_two_files(file1_path, file2_path, output_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flags.mark_flag_as_required('file1_path')
    flags.mark_flag_as_required('file2_path')
    flags.mark_flag_as_required('output_file_path')
    app.run(main)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
