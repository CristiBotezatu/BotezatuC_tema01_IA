from utils.file_utils import read_file
from utils.distances import manhattan_manual, manhattan_scipy


def run():
    path = "in.txt"
    print("Loading input data...")
    vec1, vec2 = read_file(path)

    print("First vector:", vec1)
    print("Second vector:", vec2)

    dist_manual = manhattan_manual(vec1, vec2)
    dist_scipy = manhattan_scipy(vec1, vec2)

    print("Manual Manhattan distance:", dist_manual)
    print("SciPy Manhattan distance:", dist_scipy)


if __name__ == "__main__":
    run()
