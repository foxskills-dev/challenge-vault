from fs_lib import test, run
import os

ssh_server = os.getenv("SSH_SERVER", "vault@ssh-server")

@test("Config SSH Server", score=10)
def test_config_ssh_server():
    """
    Configure the SSH Server using `vault config ssh-server vault@1.2.3.4`, the output should be `SSH server configured: vault@1.2.3.4`
    """
    assert run("app/vault", "config", "ssh-server", ssh_server) == f"SSH server configured: {ssh_server}"

@test("Config SSH Key", score=10)
def test_config_ssh_key():
    """
    Configure the SSH Key using `vault config ssh-key ~/.ssh/vault_key`, the output should be `SSH key configured: ~/.ssh/vault_key`
    """
    assert run("app/vault", "config", "ssh-key", "~/.ssh/vault_key") == "SSH key configured: ~/.ssh/vault_key"

@test("Save file", score=10)
def test_save_file():
    """
    Send a file using `vault save test.txt`, the output should be `Saved test.txt to remote branch 'main'`
    """
    open("test.txt", "w").write("Hello World")
    assert run("app/vault", "save", "test.txt") == "Saved test.txt to remote branch 'main'"

@test("Get file", score=10)
def test_get_file():
    """
    Get a file using `vault get test.txt`, the output should be `Retrieved test.txt from remote branch 'main'`
    """
    os.rename("test.txt", "test-local.txt")
    assert run("app/vault", "get", "test.txt") == "Retrieved test.txt from remote branch 'main'"
    assert open("test.txt").read() == open("test-local.txt").read()
