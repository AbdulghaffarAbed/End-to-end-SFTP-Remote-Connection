"""Sever Agent to connect with the remote machine"""
# pylint: disable= logging-fstring-interpolation

import argparse
import os
import logging as log
import sys

import pysftp
from paramiko.ssh_exception import SSHException


def get_user_input():
    """
    Parse command line arguments for connecting to a remote server via SSH.

    Returns:
        Namespace: An object containing the parsed arguments.

    Raises:
        SystemExit: If there is an error while parsing arguments,
        the function exits with a message guiding on the expected command
        line format.
    """
    log.info("Define arguments for connecting to remote server")
    arguments_parser = argparse.ArgumentParser(
        description="server Agent to connect to a remote using SSH"
    )

    arguments_parser.add_argument(
        "-ip",
        "--ip_address",
        help="IP address of " "the remote " "machine",
        required=True,
    )
    arguments_parser.add_argument(
        "-u",
        "--username",
        help="username for the remote machine",
        required=True,
    )
    arguments_parser.add_argument(
        "-s",
        "--password",
        help="password for the remote machine",
        required=True,
    )
    arguments_parser.add_argument(
        "-p",
        "--path",
        help="file or directory path to copy it",
        required=True,
    )

    try:
        log.info("Parse command line arguments")
        arguments = arguments_parser.parse_args()
        return arguments

    except SystemExit:
        print("Error while parsing arguments")
        print("Expected command:")
        print(
            "python python_file.py -ip IP_address -u username -p password "
            "-n file_or_directory_name"
        )
        sys.exit(1)


def copy_files_or_dir(sftp, file_path):
    """
    Helper function to copy a given file or directory to the remote machine
    using sftp protocol.

    Args:
    sftp : pysftp client.
    file_path : the name of the local directory or file name.
    in the remote machine.

    Raises:
         FileNotFoundError: In case of the given file does not exist in the
         local machine.
    """
    log.info("Check if the file exists or not")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error! Cannot find {file_path}")

    if os.path.isdir(file_path):
        log.info(f"Copying {file_path} directory to the remote machine")
        sftp.put_d(file_path)

    if os.path.isfile(file_path):
        log.info(f"Copying {file_path} file to the remote machine")
        sftp.put(file_path)


def open_sftp_connection(ip_address, username, password, file_or_dir_name):
    """
    Helper function to open sftp connection with the remote machine.

    Args:
    ip_address: Ip address of the remote machine.
    username: Username for the remote machine.
    password: Password for the remote machine.
    file_or_dir_name: the name of the local directory or file name.
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    log.info(f"Open sftp connection with {ip_address}")
    try:
        with pysftp.Connection(
            host=ip_address, username=username, password=password, cnopts=cnopts
        ) as sftp:
            log.info(f"Connected to {ip_address}")
            log.info(f"Start copying {file_or_dir_name} to the remote machine")
            copy_files_or_dir(
                sftp=sftp,
                file_path=file_or_dir_name,
            )
            log.info("Successfully copied files to the remote machine")

    except SSHException as exp:
        log.error(exp)
        print(exp)
    except FileNotFoundError as e:
        log.error(e)
        print(e)

    finally:
        log.info("Close sftp connection")
        sftp.close()


def main():
    """
    The entry point for the server agent logic
    """
    arguments = get_user_input()
    open_sftp_connection(
        ip_address=arguments.ip_address,
        username=arguments.username,
        password=arguments.password,
        file_or_dir_name=arguments.path,
    )


if __name__ == "__main__":
    main()
