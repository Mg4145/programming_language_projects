""" Insertion Sort """


def insertion_sort_inc(arr):
    """Insertion Sort Algorithm"""
    for idx, val in enumerate(arr):
        key = val
        j = idx - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     # print("key =\t\t", key)
    #     j = i - 1
    #     # print("j =\t\t", j)
    #     while j >= 0 and key > arr[j]:
    #         arr[j + 1] = arr[j]
    #         # print("arr[j+1] =\t", arr[j+1])
    #         # print(arr)
    #         j -= 1
    #         # print("j =\t\t", j)
    #     arr[j + 1] = key
    #     # print(arr)
    #     # print("arr[j+1] =\t", arr[j+1])
    #     # print()


def insertion_sort(arr):
    """Insertion Sort Algorithm"""
    for idx, val in enumerate(arr):
        key = val
        j = idx - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     # print("key =\t\t", key)
    #     j = i - 1
    #     # print("j =\t\t", j)
    #     while j >= 0 and key < arr[j]:
    #         arr[j + 1] = arr[j]
    #         # print("arr[j+1] =\t", arr[j+1])
    #         # print(arr)
    #         j -= 1
    #         # print("j =\t\t", j)
    #     arr[j + 1] = key
    #     # print(arr)
    #     # print("arr[j+1] =\t", arr[j+1])
    #     # print()


def main():
    """Main function to test insertion sort"""
    my_list = [5, 2, 4, 6, 1, 3]
    # my_list = [3, 3, 1, 1, 1, 1, 1, 1]
    # my_list = [31, 41, 59, 26, 41, 58]
    # my_list = ["b", "e", "a", "n", "s"]
    print(f"Original Array:\t\t{my_list}")
    insertion_sort(my_list)
    print(f"Insertion Sort:\t\t{my_list}")
    insertion_sort_inc(my_list)
    print(f"Insertion Sort Incremented:\t\t{my_list}")


if __name__ == "__main__":
    main()
