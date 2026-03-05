from scipy.spatial import distance


def manhattan_manual(v1: list, v2: list) -> float:
    """
    Calculates the Manhattan distance between two vectors manually.

    Args:
        v1 (list): The first vector.
        v2 (list): The second vector.

    Returns:
        float: The Manhattan distance.
    """
    return sum(abs(a - b) for a, b in zip(v1, v2))


def manhattan_scipy(v1: list, v2: list) -> float:
    """
    Calculates the Manhattan (city block) distance between two vectors using SciPy.

    Args:
        v1 (list or np.array): The first vector.
        v2 (list or np.array): The second vector.

    Returns:
        float: The Manhattan distance.
    """
    return distance.cityblock(v1, v2)


if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]

    print("Manhattan distance (manual):", manhattan_manual(v1, v2))
    print("Manhattan distance (SciPy):", manhattan_scipy(v1, v2))
