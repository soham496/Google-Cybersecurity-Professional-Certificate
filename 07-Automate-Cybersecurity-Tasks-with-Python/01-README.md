# Algorithm for File Updates in Python  

## 📌 Project Description  
This project is part of **Course 7, Module 4 of the Google Cybersecurity Professional Certificate**.  
The goal of this activity is to write a Python script that manages an allow list of IP addresses by removing specific entries based on a given remove list.  

This simulates a real-world cybersecurity task where administrators must update and maintain access control lists to ensure only authorized systems are allowed.  


## 📝 Steps Implemented  
1. **Open the file that contains the allow list**  
   - The script reads the contents of a file containing approved IP addresses.  

2. **Read the file contents**  
   - The list of IP addresses is loaded into the program as a string.  

3. **Convert the string into a list**  
   - The string is split into a Python list for easier processing.  

4. **Iterate through the remove list**  
   - The script loops through the list of IP addresses to be removed.  

5. **Remove IP addresses that are on the remove list**  
   - Any matching IPs are deleted from the allow list.  

6. **Update the file with the revised list of IP addresses**  
   - The updated allow list is written back to the file.  


## ⚙️ Technologies Used  
- **Python 3**  
- File handling (`open`, `read`, `write`)  
- List manipulation  


## 📂 Files Included  
- `update_allow_list.py` → Python script implementing the algorithm  
- `Course7_Certificate.pdf` → Certificate of completion  
- `Project_Report.md` → Written project description or notes  


## ✅ Summary  
This project demonstrates how automation with Python can be used in cybersecurity tasks to:  
- Maintain allow lists efficiently  
- Reduce manual errors in file updates  
- Apply algorithmic thinking to real-world security processes  


