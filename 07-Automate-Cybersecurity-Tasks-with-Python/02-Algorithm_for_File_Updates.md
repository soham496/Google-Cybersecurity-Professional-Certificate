Algorithm for file updates in Python
Project description
[In this task, I worked with a file that contains an allow list of IP addresses. The goal was to update the file by removing certain IPs listed in a separate remove list, and then save the revised allow list back into the file.]
Open the file that contains the allow list
[I used Python’s open() function in read mode to access the file. This allowed me to read all the IP addresses currently stored in the allow list file.]
Read the file contents
[After opening the file, I used the .read() method to read its contents into a string variable. This way I could work with the data inside Python.]
Convert the string into a list
[Since the file contents were read as a single string, I used .split() to break the string into a Python list where each element represented one IP address.]
Iterate through the remove list
[I created or defined a separate remove list with the IP addresses that needed to be deleted from the allow list. Using a for loop, I iterated through each IP in this list.]
Remove IP addresses that are on the remove list
[Inside the loop, I checked if each IP existed in the allow list. If it did, I used the .remove() method to delete it. This left only the allowed IPs in the list.]
Update the file with the revised list of IP addresses 
[Finally, I re-opened the allow list file in write mode ("w") and used .write() to save the updated list of IPs back into the file.]
Summary
[Through this activity, I practiced basic Python file handling, list operations, and loops. I learned how to open, read, update, and overwrite files. This is useful for automating security tasks, like managing allow and block lists for networks.]

