def merge_lists(list_a, list_b):
    return list(set(list_a) | set(list_b))


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
