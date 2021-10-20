# SubChecker


 About Subchecker:
 
 Subchecker is a python tool designed to detect reachable subdomains of websites after then you enumerate possible subdomains. It helps pentesters, bug hunters, and developers to understand which subdomains are actually reachable and how many are accessible or not.
 
 
 Usage:
 
1- open your terminal

2- enter the command: git clone https://github.com/zer0da/SubChecker.git

3- cd SubChecker

4- python3 subChecker.py -i /home/kali/Desktop/BugBounty/dns2-enum.txt


 Parameters:

We have only one parameter.

 -i or --input: You should enter your txt file. This txt file should include your subdomains. The program will check these subdomains' response codes. 
 
 
 Screenshot:
 
 ![image](https://user-images.githubusercontent.com/65029938/138122115-50c67851-2eb2-49a8-b9d4-530f8fdc7a8b.png)
