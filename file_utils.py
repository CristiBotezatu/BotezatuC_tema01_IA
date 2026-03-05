def read_file(filename: str = "in.txt") -> tuple[list[float], list[float]]:
    """
    Reads two lines of space-separated numbers from a text file.

    Args:
        filename (str): The path to the text file. Defaults to "in.txt".

    Returns:
        tuple: Two lists of floats representing the first and second vectors.
    """
    with open(filename, "r") as f:
        v1 = [float(x) for x in f.readline().split()]
        v2 = [float(x) for x in f.readline().split()]

    return v1, v2


if __name__ == "__main__":
    v1, v2 = read_file()
    print("Vector 1:", v1)
    print("Vector 2:", v2)
