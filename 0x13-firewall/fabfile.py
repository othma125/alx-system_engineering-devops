from fabric.api import env, run

# Setting the environment variables
env.user = 'ubuntu'
env.hosts = ["54.146.65.131", "18.208.120.199"]
env.key_filename = "~/.ssh/school"

def restart_nginx():
    """
    Restart Nginx on remote hosts
    """
    run('sudo systemctl restart nginx')
