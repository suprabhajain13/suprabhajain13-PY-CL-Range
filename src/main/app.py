from lab import *

def main():
    # Generate a sequence of integers from zero to stop-1
    stop = int(input("Enter the stop value for the range: "))
    print("Range with stop value:", range_with_stop(stop))

    # Generate a sequence of integers from start to stop-1
    start = int(input("Enter the start value for the range: "))
    stop = int(input("Enter the stop value for the range: "))
    print("Range with start and stop values:", range_with_start_stop(start, stop))

    # Generate a sequence of integers starting from start, incrementing by step, and stopping before stop
    start = int(input("Enter the start value for the range: "))
    stop = int(input("Enter the stop value for the range: "))
    step = int(input("Enter the step value for the range: "))
    print("Range with start, stop, and step values:", range_with_start_stop_step(start, stop, step))

if __name__ == "__main__":
    main()
