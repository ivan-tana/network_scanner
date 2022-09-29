import asyncio
from pyclbr import Function
import platform
import socket

async def shell_command(command: str,ip: str, callback: Function, errcallback: Function):
    
    # run a shell command
    Process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await Process.communicate()

    
    if Process.returncode == 0:
        # if the command exexutes without an error
        callback(stdout, ip)
    else:
        # if the command exexutes with an error
        errcallback(stderr, ip)


# run multiple shell commands at the same time
async def shell_commands(args: list):
    commands_to_run = []

    for arg in args:
        commands_to_run.append(shell_command(*arg))
        print(commands_to_run)
    result = await asyncio.gather(*commands_to_run)

    return result

def build_commands(success, failed):
    current_device_ip = socket.gethostbyname(socket.gethostname())
    base_ip = current_device_ip.rsplit('.',1)[0] + '.'
    commands = []
    if platform == 'linux' or 'linux2':
        for i in range(0,255):
            ip =  base_ip + str(i)
            command = ['ping -c 1 ' + ip,ip, success, failed]
            commands.append(command)
        return commands
    if platform == 'win32':
        for i in range(1,255):
            ip = base_ip + str(i)
            command = ['ping -n 1 ' + ip,ip, success, failed]
            commands.append(command)
        return commands
    if platform == 'darwin':
        pass
    return commands


async def networkDevices(success, failed):
    try:
        await shell_commands(build_commands(success, failed))
        return True
    except:
        return False