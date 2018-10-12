import os
import re
import sys
import subprocess


def is_submission(filename):
    """Check if the given filename represents a submission."""
    if re.search(r"[a-z]+_[0-9]+", filename):
        return True
    else:
        return False


def break_names(submission_name):
    """Extract the student's name and the original file name
    frin the downloaded submission name
    """
    std_name = re.search(r"[a-z]+", submission_name).group(0)
    filename = re.search(r"(.*[0-9]+_[0-9]+_)(.+)", submission_name).group(2)
    return std_name, filename


def dispatch(path):
    """Organize the submissions into folders.
    Each folder will include all the submitted files of one student.
    """
    files = os.listdir(path)
    for file in files:
        if not is_submission(file):
            continue
        std_name, filename = break_names(file)
        dir_name = path + "/" + std_name
        if not os.path.exists(dir_name):
            subprocess.call(["mkdir", dir_name])
        subprocess.call(["mv", path + "/" + file, dir_name + "/" + filename])


if __name__ == '__main__':
    dispatch(sys.argv[1])