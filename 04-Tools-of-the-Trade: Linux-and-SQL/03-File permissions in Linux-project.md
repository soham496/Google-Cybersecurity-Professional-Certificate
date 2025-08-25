### File permissions in Linux



Project description



\[In this activity, I practiced using Linux commands to manage and understand file and directory permissions. The goal was to check details of files, read the permission strings, and then use chmod to change access rights for users, groups, and others.]





Check file and directory details



\[I used the command ls -l to see a detailed list of files and directories. This showed me the permissions, owner, group, and size of each file. For example, I noticed that some files had write access for others, which is not safe.]





Describe the permissions string



\[The permission string looks like -rw-r--r--. The first character shows if it’s a file (-) or a directory (d). The next three characters are for the user (owner), the next three for the group, and the last three for others. For example, r means read, w means write, and x means execute.]





Change file permissions



\[To remove unsafe permissions, I used chmod. For example: chmod o-w filename. This removed write permission from others. After running ls -l again, I could see that the file no longer allowed others to modify it. ] 





Change file permissions on a hidden file



\[There was a hidden file called .project\_x.txt. I changed its permissions so that only the user and group could read it, but not write. I did this with: chmod 440 .project\_x.txt Now, both user and group can read it, but no one can write to it.]





Change directory permissions



\[For the drafts directory, I saw that the group had execute permission. I removed it using:

chmod g-x drafts. After that, the group no longer had execute permission, which means they can’t enter the directory anymore.]





Summary



\[Through this task, I learned how to check file and directory permissions using ls -l, how to understand the permission string, and how to use chmod to adjust permissions. I also practiced changing permissions on both normal files and hidden files, as well as on a directory. This exercise helped me understand how Linux manages file security and why correct permissions are important.]





