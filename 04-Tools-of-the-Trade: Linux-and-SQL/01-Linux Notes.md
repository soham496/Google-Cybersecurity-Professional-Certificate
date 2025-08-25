Linux Notes

Basic commands

pwd → print working directory
ls → list files
ls -a → list all files including hidden
cd → change directory
cat file.txt → display content of a file

File permissions

ls -l → check file permissions
chmod → change permissions
Example: chmod u+x file.txt → give user execute permission
chown user:group file.txt → change owner and group

Users and groups

useradd → create a new user
usermod -a -G group user → add user to secondary group
usermod -g group user → set primary group