import subprocess

# Define the output file path
output_file = 'test.txt'

# Attempt to run the command and write the output
try:
    result = subprocess.run(['whoami'], capture_output=True, text=True, check=True)
    output = result.stdout.strip()  # Get the output and strip any extra whitespace
except subprocess.CalledProcessError as e:
    output = f"Command failed with error: {e.stderr.strip()}"
except Exception as e:
    output = f"An unexpected error occurred: {str(e)}"

# Write the output to the file
with open(output_file, 'w') as outfile:
    outfile.write(output)
