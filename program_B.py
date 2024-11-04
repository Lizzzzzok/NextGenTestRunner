import subprocess
import statistics

# Send the required command to program A and get the answer
def send_command(process, command):
    process.stdin.write(f"{command}\n")
    process.stdin.flush()
    return process.stdout.readline().strip()

# Get 100 random numbers and append them to "random_numbers" list for future sort
def get_random_numbers(process, count=100):
    random_numbers = []
    # Send the 'GetRandom' command to program A 100 times
    for _ in range(count):
        response = send_command(process, "GetRandom")
        try:
            # Add random numbers to the list
            random_numbers.append(int(response))
        except ValueError:
            raise ValueError(f"Invalid random number: {response}")
    return random_numbers

def main():
    # Defining communication channels
    with subprocess.Popen(
        ["python3", "program_A.py"], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True) as process:
        try:
            # Send "Hi" command to Program A and verify the correct response
            response = send_command(process, "Hi")
            if response == "Hi":
                print("Program A responded correctly to 'Hi' command")
            if response != "Hi":
                raise RuntimeError("Program A did not respond correctly to 'Hi' command")

            # Get 100 random numbers
            random_numbers = get_random_numbers(process)

            send_command(process, "Shutdown")
            # Making sure program B waits for program A to fully terminate
            process.wait()

            sorted_random_numbers = sorted(random_numbers)
            median = statistics.median(sorted_random_numbers)
            average = statistics.mean(sorted_random_numbers)

            print("Sorted Random Numbers:", sorted_random_numbers)
            print("Median:", median)
            print("Average:", average)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
