import sys
import os
import re

def replace_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'\t|    ','#', content)

    for line in content.split('\n'):
        match = re.match(r'^(#{1,4})-', line)  # Find lines that start with one or more hashtags followed by a hyphen
        if match:
            hashes = match.group(1)
            updated_line = re.sub(r'^(#{1,4})-', hashes, line, count=1)
            content = content.replace(line, updated_line, 1)

    content = re.sub(r'^#####','', content)

    for line in content.split('\n'):
        match = re.match(r'^(#+)-', line)  # Find lines that start with one or more hashtags followed by a hyphen
        if match:
            num_hashes = match.group(1)
            replacement = '\t' * (len(num_hashes)-5)  # Replace hashtags with tab characters
            updated_line = line.replace(num_hashes, replacement, 1)
            content = content.replace(line, updated_line, 1)

    # Write updated content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


# Loop through all files in current directory and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)

        # Only process files with .txt extension
        if file_path.endswith('.md'):
            replace_strings(file_path)
