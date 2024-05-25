import matplotlib.pyplot as plt
import random
import time

# Get the user's input
graph_type = input(
    "Which graph do you want to see the time complexity of? (bubble sort, hanoi tower,linear search, binary search)")

# Draw the graph based on the user's input
if graph_type == "bubble sort":

    # Generate random input lists of different sizes for bubble sort
    input_sizes = [300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000]
    input_lists = [random.choices(range(1, 1000), k=size) for size in input_sizes]

    # Calculate the execution time of bubble sort for each input list
    bubble_sort_execution_times = []
    for input_list in input_lists:
        start_time = time.time()
        for i in range(len(input_list)):
            for j in range(0, len(input_list) - i - 1):
                if input_list[j] > input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
        end_time = time.time()
        bubble_sort_execution_times.append(end_time - start_time)
    # Draw the graph
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, bubble_sort_execution_times)
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity of Bubble Sort")
    plt.show()
elif graph_type == "hanoi tower":
    # Generate input sizes for Hanoi tower
    hanoi_input_sizes = [i for i in range(10, 20)]


    # Calculate the execution time of Hanoi towers for each input size
    def hanoi(n, from_rod, to_rod, aux_rod):
        if n == 1:
            print("Move disk 1 from rod", from_rod, "to rod", to_rod)
            return
        hanoi(n - 1, from_rod, aux_rod, to_rod)
        print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
        hanoi(n - 1, aux_rod, to_rod, from_rod)


    hanoi_execution_times = []
    for input_size in hanoi_input_sizes:
        start_time = time.time()
        hanoi(input_size, 'A', 'C', 'B')
        end_time = time.time()
        hanoi_execution_times.append(end_time - start_time)

    # Draw the graph
    plt.figure(figsize=(10, 6))
    plt.plot(hanoi_input_sizes, hanoi_execution_times)
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity of Hanoi Tower")
    plt.show()
elif graph_type == "linear search":
    linear_input_sizes = [100, 101, 102, 103, 104, 2000, 30000, 3000000, 5000000, 6000000]
    linear_input_lists = [random.choices(range(1, 10000), k=size) for size in linear_input_sizes]
    linear_search_time = []
    for input_list in linear_input_lists:
        start_time = time.time()
        for i in range(len(input_list)):
            if input_list[i] == 10000000000:
                print("element is present at index", i)
                break
        end_time = time.time()
        linear_search_time.append(end_time - start_time)
    # Draw the graph
    plt.figure(figsize=(10, 6))
    plt.plot(linear_input_sizes, linear_search_time)
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity of linear search")
    plt.show()
elif graph_type == "binary search":
    binary_input_sizes = [100,200,300,400,500,600,700,800,900,1000]
    binary_input_lists = [random.choices(range(1, 1000), k=size) for size in binary_input_sizes]
    binary_search_execution_time = []
    def binary_search(arr, low, high, x):
        while low <= high:
            mid = (low + high) // 2
        # Check if x is present at mid
            if arr[mid] == x:
                return mid
        # If x is greater, ignore left half
            elif arr[mid] < x:
                low = mid + 1
        # If x is smaller, ignore right half
            else:
                high = mid - 1
        # If we reach here, then the element
        # was not present
        return -1


    for input_list in binary_input_lists:
        input_list.sort()
        #print(input_list)
        start_time = time.time()
        result = binary_search(input_list, 0, len(input_list) - 1, 1001)
        if result != -1:
            print("Element is present at index", result)
        else:
            print("Element is not present in array")
        end_time = time.time()
        binary_search_execution_time.append(end_time - start_time)
    # Draw the graph
    plt.figure(figsize=(10, 6))
    plt.plot(binary_input_sizes, binary_search_execution_time)
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity of binary search")
    plt.show()









else:
    print("Invalid input. Please enter either 'bubble sort', 'hanoi towers', or linear search.")