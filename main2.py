import subprocess

def run_cli_command(command):
    """Runs a CLI command and returns the output as a list of lines."""
    print(f"Running command: {command}")  
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            output = result.stdout.strip().split("\n")
            print(f"Output:\n{output}\n")  
            return output
        else:
            print(f"Error running command: {command}\n{result.stderr}")
            return []
    except Exception as e:
        print(f"Exception while running command: {command}\n{e}")
        return []

# Step 1: Get all AVS (network) addresses
avs_output = run_cli_command("python symb.py nets")