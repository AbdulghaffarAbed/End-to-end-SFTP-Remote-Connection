# End-to-End SFTP Remote Connection

## Description:
The Secure File Transfer Protocol (SFTP) Server Agent is a Python script designed to facilitate the secure transfer of files or directories from a local machine to a remote machine using the SFTP protocol. This project aims to provide a convenient and reliable method for transferring sensitive data between machines in a secure manner.

![Simple project workflow diagram](https://github.com/AbdulghaffarAbed/End-to-end-SFTP-Remote-Connection/blob/master/images/remote_connection.PNG)
## Prerequisites:

1. Python and pip installed on the local machine.
2. Installation of required Python packages using the provided requirements 
   file.
3. Firewall must be disabled on the remote machine to allow for SFTP 
   connections.

## Usage:

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages by running:
```doctest
    pip install -r requirements.txt
```
4. Run the server_agent.py script with the following arguments:
```doctest
    python server_agent.py [remote_ip] [remote_username] [remote_password] [local_file/directory_path]
```

- [remote_ip]: IP address of the remote machine.
- [remote_username]: Username for accessing the remote machine.
- [remote_password]: Password for the specified username on the remote machine.
- [local_file/directory_path]: Absolute path of the file or directory to be 
  transferred to the remote machine.
## Example:
```doctest
python server_agent.py 192.168.1.100 user123 password123 /path/to/local/file_or_directory
```

## Notes:

- Ensure that the provided local file/directory path is correct and accessible.
- It is recommended to review security measures before transferring sensitive 
  data over the network (you need to disable the firewall in some cases).

## Code Formatting and Analysis:

- The project code is formatted using the Black formatter to ensure 
consistency and readability.
- Pylint is utilized as a static code analyzer to maintain code quality and 
  identify potential issues.

## Acknowledgements:

- This project utilizes the Paramiko library for SSH communication.
