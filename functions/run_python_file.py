import os
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.lower().endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python", abs_file_path], timeout = 30,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd = abs_working_dir )
        
        stdout = result.stdout.decode()
        stderr = result.stderr.decode()
        if len(stdout) == 0 and len(stderr) == 0:
            if result.returncode != 0:
                return f'Process exited with code {result.returncode}'
            return "No output produced."
        else:
            output_lines = []
            if stdout.strip():
                output_lines.append(f"STDOUT: {stdout}")
            if stderr.strip():
                output_lines.append(f"STDERR: {stderr}")
            if result.returncode != 0:
                output_lines.append(f'Process exited with code {result.returncode}')
            return "\n".join(output_lines)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
