import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

#usage-
#Run python script
#A new cmd will open up, you can now run the commands directly
#Example:
#>net user
#>net user "UserName" "YourPassword" (set password)
#>net user "UserName" "YourPassword" /add (add user)
#>net user "UserName" /delete (delete user)
#>net localgroup Administrators "UserName" /add (add user to admin group)
#>wmic useraccount get name,fullname (get list of users)
#>net group "GroupName" (get group's members list)
#>net localgroup "GroupName" "UserName" /delete (remove user from group)
#>net group "GroupName" "UserName" /add (add user to group)
#>net group "GroupName" "UserName" /delete (remove user from group)

#refer:
#https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/net-user
