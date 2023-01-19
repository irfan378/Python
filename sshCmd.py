import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(ip, port=port, username=user, password=passwd)
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines()+stderr.readlines()
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())


if __name__ == '__main__':
    import getpass
   # user=getpass.getuser() #Get the username from the environment or password database.
# First try various environment variables, then the password database. This works on Windows as long as USERNAME is set.
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)