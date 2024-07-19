import os

# Define a hard-coded list of files/folders to ignore (make sure these are in a normalized format)
additional_ignores = [
    'README.md',
    'LICENSE',
    'venv/',
    '__pycache__/',
    '.git/'
]

def find_gitignore(directory):
    gitignore_path = os.path.join(directory, '.gitignore')
    if os.path.exists(gitignore_path) and os.path.isfile(gitignore_path):
        return gitignore_path
    return None

def parse_gitignore(gitignore_path):
    ignores = []
    with open(gitignore_path, 'r') as file:
        for line in file:
            # Strip whitespace including newline characters
            line = line.strip()
            # Ignore comments and wildcard lines
            if not line.startswith('#') and '*' not in line and line:
                # Add directories with trailing slash
                if os.path.isdir(line):
                    line = os.path.join(line, '')
                ignores.append(line)
    return ignores

def should_ignore(path, ignore_list):
    for ignore in ignore_list:
        if os.path.isdir(ignore) and path.startswith(ignore):
            return True
        elif ignore in path:
            return True
    return False

def get_all_files(directory, ignore_list):
    all_files = []
    for root, dirs, files in os.walk(directory):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if not should_ignore(os.path.relpath(os.path.join(root, d), directory), ignore_list)]
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            if not should_ignore(file_path, ignore_list):
                all_files.append(os.path.abspath(os.path.join(root, file)))
    return all_files

def print_file_content(file_path, current_directory):
    relative_path = os.path.relpath(file_path, current_directory)
    _, extension = os.path.splitext(file_path)
    # Determine the language for code block based on file extension
    language_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.sh': 'bash',
        # Add more mappings as required
    }
    language = language_map.get(extension, '')  # Default to no language if not found
    # print(f"---\n{file_path}\n```{language}")
    # print(f"\n---\n{file_path}\n```{language}")
    print(f"\n---\nFile: `{relative_path}`\n```{language}")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
    print("```\n")

def print_directory_tree(directory, ignore_list, prefix=''):
    entries = os.listdir(directory)
    entries = [e for e in entries if not should_ignore(os.path.relpath(os.path.join(directory, e), directory), ignore_list)]
    entries.sort()
    pointers = ['├── '] * (len(entries) - 1) + ['└── ']

    for pointer, entry in zip(pointers, entries):
        path = os.path.join(directory, entry)
        print(prefix + pointer + entry)
        if os.path.isdir(path):
            extension = '│   ' if pointer == '├── ' else '    '
            print_directory_tree(path, ignore_list, prefix + extension)

def main():
    # Get the current directory
    current_directory = os.getcwd()

    # Step 1: Locate the .gitignore file
    gitignore_path = find_gitignore(current_directory)

    if gitignore_path:
        # Step 2: Read and parse the .gitignore file
        gitignore_ignores = parse_gitignore(gitignore_path)
    else:
        print("No .gitignore file found.")
        gitignore_ignores = []

    # Print the items found in .gitignore
    # print("Ignores from .gitignore:")
    # for item in gitignore_ignores:
    #     print(item)

    # Step 4: Add hard-coded ignores
    combined_ignores = gitignore_ignores + additional_ignores

    # remove duplicates
    combined_ignores = list(set(combined_ignores))

    # Normalize ignore list
    combined_ignores = [os.path.normpath(ignore) for ignore in combined_ignores]

    # Print the combined ignore list
    print("Ignoring files:")
    for item in combined_ignores:
        print(f" - {item}")

    # Print the directory tree
    print("\nDirectory Tree:")
    print_directory_tree(current_directory, combined_ignores)

    # Step 5: Get all files in the current directory, excluding ignored ones
    remaining_files = get_all_files(current_directory, combined_ignores)

    # Step 6: Print the contents of each file in an appropriate markdown code block
    for file in remaining_files:
        print_file_content(file, current_directory)

if __name__ == "__main__":
    main()
