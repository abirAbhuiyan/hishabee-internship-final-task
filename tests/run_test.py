import subprocess

# List of scripts to run
scripts = [
    "P001.py", "P002.py", "P003.py", "P005.py", "P006.py", 
    "P007.py", "P010.py", "S003.py", "S004.py", "S005.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python3", script])
    print(f"Finished {script}\n")
