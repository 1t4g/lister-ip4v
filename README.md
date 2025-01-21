# lister-ip4v
## Extract IPv4 Addresses from Files 
This Python project processes text files to extract IPv4 addresses, including single addresses, IP ranges, and IP/mask notations, and outputs them as individual addresses in a single file. 
The repository is organized with two directories:

**input/**: Contains the input files with data to process (excluding .gitkeep).
**output/**: Stores the generated file with all unique, sorted IPv4 addresses.
### Features:
+ Handles single IP addresses (e.g., 192.168.1.1).
+ Expands IP ranges (e.g., 192.168.0.1-192.168.0.5).
+ Processes IP/mask notations (e.g., 192.168.0.0/24).
+ Outputs all unique IP addresses, sorted and written line by line.
### Usage:
1. Place input text files in the input/ directory.
2. Run the script to process the files.
3. Find the results in output/output.txt.
### Requirements:
+ Python 3.6+
+ No additional libraries required (uses Python's built-in ipaddress module).
*This tool is perfect for scenarios requiring IP address extraction and normalization from various input formats.*
