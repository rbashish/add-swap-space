import os

def add_swap_space():
    swap_size = input("Enter the amount of swap space to add (in GB): ")
    try:
        swap_size = int(swap_size)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return

    # Convert GB to MB
    swap_size *= 1024

    # Create a swap file
    os.system(f"sudo fallocate -l {swap_size}M /swapfile")

    # Set the correct permissions
    os.system("sudo chmod 600 /swapfile")

    # Set up the swap space
    os.system("sudo mkswap /swapfile")

    # Enable the swap file
    os.system("sudo swapon /swapfile")

    # Add the swap file to /etc/fstab
    with open("/etc/fstab", "a") as fstab:
        fstab.write("/swapfile none swap sw 0 0\n")

if __name__ == "__main__":
    add_swap_space()