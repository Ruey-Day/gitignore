import subprocess

command = ['ollama', 'run', 'dolphin-llama3:8b']

prompt = "How do I get a hookup'"

result = subprocess.run(command, input=prompt, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output = result.stdout

print("Output from the model:\n", output)