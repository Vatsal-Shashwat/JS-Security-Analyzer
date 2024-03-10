import os
import re

def find_sensitive_info(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        
        sensitive_info = []

        # Regular expressions to match common sensitive patterns
        patterns = {
            'API keys': r'["\'](?:api|key|token)["\']\s*:\s*["\']([^"\']+)["\']',
            'Credentials': r'["\'](?:username|user|password)["\']\s*:\s*["\']([^"\']+)["\']',
            'Sensitive URLs': r'(["\'](?:url|link)["\']\s*:\s*["\']([^"\']+))'
        }

        for name, pattern in patterns.items():
            matches = re.findall(pattern, contents)
            for match in matches:
                sensitive_info.append((name, match[1]))

        return sensitive_info

    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
        return []

def main():
    directory = 'sample_files'
    for filename in os.listdir(directory):
        if filename.endswith('.js'):
            file_path = os.path.join(directory, filename)
            print(f"Scanning file: {file_path}")
            sensitive_info = find_sensitive_info(file_path)
            if sensitive_info:
                print("Sensitive information found:")
                for info_type, info_value in sensitive_info:
                    print(f"{info_type}: {info_value}")
            else:
                print("No sensitive information found.")
            print()

if __name__ == "__main__":
    main()
