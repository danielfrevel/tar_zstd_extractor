from zstandard import ZstdDecompressor
from pathlib import Path
from tarfile import open
from os import remove, listdir, path

all_files = [f for f in listdir('.') if path.isfile(f)]

all_zst_files = [f for f in all_files if '.zst' in all_files]

zst_file = all_zst_files


def decompress_tar(tar_file_path):
    tar = open(tar_file_path)
    tar.extractall('./')
    tar.close()


def decompress_zstandard(zstd_file_path):
    zstd_file_path = Path(zstd_file_path)
    with open(zstd_file_path, 'rb') as compressed:
        decomp = ZstdDecompressor()
        with open('./tar', 'wb') as destination:
            decomp.copy_stream(compressed, destination)
    return './tar'


tar_file_path = decompress_zstandard(zst_file)
decompress_tar(tar_file_path)
remove('./tar')
