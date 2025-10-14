# Algorithm to update allow list by removing unwanted IPs

# Open and read the allow list
with open("allow_list.txt", "r") as file:
    data = file.read()

# Convert string to a list of IPs
allow_list = data.split()

# Example remove list
remove_list = ["192.168.1.100", "10.0.0.25"]

# Remove IPs that are in the remove list
for ip in remove_list:
    if ip in allow_list:
        allow_list.remove(ip)

# Update the file with the revised allow list
with open("allow_list.txt", "w") as file:
    for ip in allow_list:
        file.write(ip + "\n")

print("Allow list updated successfully!")
