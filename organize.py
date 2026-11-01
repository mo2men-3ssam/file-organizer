import os

target_dir = os.path.dirname(os.path.realpath(__file__))

# target_dir = input('Dir Path> ').strip()

if not os.path.exists(target_dir) :
    print('[!]Dir Notfound')
    exit()

try :
    organize = int(input("""
    What will you organize today? (chose number)
    0- all
    1- images
    2- videos
    3- audios
    4- documents
    5- archives
    6- codes
    7- programs
    > """))
except ValueError:
    print("[!]Just Chose Number")

# organize images
def organize_images() :
    for file_name in os.listdir(target_dir) :
        folder_name = 'Images'
        formats = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.gif', '.tiff', '.tif', '.bmp', '.avif', '.heic', '.raw', '.cr2', '.nef', '.eps')
        # check folder exist
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)

        # check file format
        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Image Archived to {dst}')

# organize videos
def organize_videos() :
    folder_name = 'Videos'
    formats = ('.mp4', '.m4v', '.webm', '.ogv', '.mov', '.qt', '.mxf', '.mkv', '.flv', '.f4v', '.avi', '.wmv', '.vob', '.mpg', '.mpeg', '.mp2', '.mpe', '.mpv', '.3gp', '.3g2', '.mts', '.m2ts', '.tsv', '.tsa', '.svi', '.r3d')
    for file_name in os.listdir(target_dir) :
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)
        
        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Video Archived to {dst}')

# organize audios
def organize_audios() :
    folder_name = 'Audios'
    formats = ('.wav', '.aiff', '.aif', '.pcm', '.raw', '.dsf', '.dff', '.flac', '.m4a', '.alac', '.ape', '.wv', '.wma', '.tta', '.shn', '.mp3', '.aac', '.ogg', '.oga', '.opus', '.wma', '.at3', '.aa3', '.mpc', '.amr', '.3ga', '.gsm', '.act', '.dvf', '.dss', '.m4b', '.aax', '.aa', '.mid', '.midi', '.mod', '.s3m', '.xm', '.it')

    for file_name in os.listdir(target_dir) :
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)

        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Audios Archived to {dst}')

# organize documents
def organize_documents() :
    folder_name = 'Documents'
    formats = ('.docx', '.doc', '.odt', '.rtf', '.txt', '.wps', '.pages', '.xlsx', '.xls', '.csv', '.ods', '.numbers', '.pptx', '.ppt', '.ppsx', '.pps', '.odp', '.key', '.pdf', '.xps', '.epub', '.mobi', '.azw', '.azw3', '.djvu', '.indd', '.tex')

    for file_name in os.listdir(target_dir) :
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)

        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Document Archived to {dst}')

# organize archives
def organize_archives() :
    folder_name = 'Archives'
    formats = ('.zip', '.zipx', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.zsr', '.z', '.taz', '.lha', '.lzh', '.iso', '.img', '.dmg', '.vhd', '.vhdx', '.vmdk', '.qcow2', '.cab', '.wim', '.pax', '.cpio', '.ar', '.a', '.bak', '.ace', '.arj', '.zoo', '.pak', '.wad', '.pkg')

    for file_name in os.listdir(target_dir) :
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)

        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Archives Archived to {dst}')

# organize codes
def organize_codes() :
    folder_name = 'Codes'
    formats = ('.js', '.jsx', '.ts', 'tsx', '.py', '.pyw', '.ipynb', '.c', '.c++', '.cpp', '.cp', '.cc', '.h', '.hpp', '.java', '.class', '.jar', '.jav', '.cs', '.php', '.rb', '.ru', '.r', '.go', '.dart', '.rs', '.swift', '.kt', '.kts', '.zsh', '.html', '.htm', '.css', '.scss', '.sass', '.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.properties', '.env', '.sql', '.prisma', '.migration', '.lock', 'Makefile', '.md', '.markdown', '.gitattributes', '.gitignore')

    for file_name in os.listdir(target_dir) :
        if not os.path.exists(folder_name) :
            os.mkdir(folder_name)

        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Code Archived to {dst}')

# organize programs
def organize_programs() :
    folder_name = 'Programs'
    formats = ('.exe', '.msi', '.msix', '.msixbundle', '.appx', '.appxbundle', '.bat', '.cmd', '.ps1', '.app', '.ipa', '.deb', '.rpm', '.pkg.tar.zst', '.pkg.tar.xz', '.AppImage', '.flatpak', '.flatpakref', '.snap', '.sh', '.bash', '.tar.gz', '.tgz', '.tar.bz2', '.apk', '.aab', '.xapk', '.apks', '.apkm', '.hap', '.crx', '.xpi')

    for file_name in os.listdir(target_dir) :
        if os.path.exists(folder_name) :
            os.mkdir(folder_name)

        if file_name.lower().endswith(formats) :
            src = os.path.join(target_dir, file_name)
            dst = os.path.join(target_dir, folder_name, file_name)
            os.replace(src, dst)
            print(f'[-]Programs Archived to {dst}')

if organize == 0 :
    organize_images()
    print('[✔]Images Done')

    organize_videos()
    print('[✔]Videos Done')

    organize_audios()
    print('[✔]Audios Done')

    organize_documents()
    print('[✔]Documents Done')

    organize_archives()
    print('[✔]Archives Done')

    organize_codes()
    print('[✔]Codes Done')

    organize_programs()
    print('[✔]Programs Done')
elif organize == 1 :
    organize_images()
    print('[✔]Images Done')
elif organize == 2 :
    organize_videos()
    print('[✔]Videos Done')
elif organize == 3 :
    organize_audios()
    print('[✔]Audios Done')
elif organize == 4 :
    organize_documents()
    print('[✔]Documents Done')
elif organize == 5 :
    organize_archives()
    print('[✔]Archives Done')
elif organize == 6 :
    organize_codes()
    print('[✔]Codes Done')
elif organize == 7 :
    organize_programs()
    print('[✔]Programs Done')
