import os
from shutil import move

# Defines directory paths
home = os.getenv('HOME')
downloads_dir = f'{home}/Downloads/'
documents_dir = f'{home}/Documents/'
image_dir = f'{home}/Documents/Images/'
software_dir = f'{home}/Documents/Software/'
other_dir = f'{home}/Documents/Other/'

# Defines file types
doc_types = (
    '.doc', '.docx', '.ebook', '.log', '.md', '.msg', '.odt', '.org', '.pages',
    '.pdf', '.rtf', '.rst', '.tex', '.txt', '.wpd', '.wps', '.xls', '.ppt',
    '.xlsx', '.pptx'
)

image_types = (
    '.3dm', '.3ds', '.max', '.bmp', '.dds', '.gif', '.jpg', '.jpeg', '.png',
    '.psd', '.xcf', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps',
    '.ps', '.svg', '.dwg', '.dxf', '.gpx', '.kml', '.kmz', '.webp'
)

software_types = (
    '.exe', '.pkg', '.dmg', '7z', 'a', 'apk', 'ar', 'bz2', 'cab', 'cpio', 'deb',
    'egg', 'gz', 'iso', 'jar', 'lha', 'mar', 'pea', 'rar', 'rpm', 's7z', 'shar',
    'tar', 'tbz2', 'tgz', 'tlz', 'war', 'whl', 'xpi', 'zip', 'zipx', 'xz', 'pak'
)


# Returns files that aren't (1)hidden (2)current file (this very script)
def get_non_hidden_files_except_current_file(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(f) and not
            f.startswith('.') and not f.__eq__(__file__)]


# Moves files to designated directories based on extensions
def move_files(files):
    for file in files:
        if file.endswith(doc_types):
            move(file, f'{documents_dir}/{file}')
            print(f'file {file} moved to {documents_dir}')
        elif file.endswith(image_types):
            move(file, f'{image_dir}/{file}')
            print(f'file {file} moved to {image_dir}')
        elif file.endswith(software_types):
            move(file, f'{software_dir}/{file}')
            print(f'file {file} moved to {software_dir}')
        else:
            move(file, f'{other_dir}/{file}')
            print(f'file {file} moved to {other_dir}')


if __name__ == '__main__':
    downloaded_files = get_non_hidden_files_except_current_file(downloads_dir)
    move_files(downloaded_files)
