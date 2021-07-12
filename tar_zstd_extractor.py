from zstandard import ZstdDecompressor
import pathlib
import tarfile
import os

all_files = [f for f in os.listdir('.') if os.path.isfile(f)]

all_zst_files = [f for f in all_files if '.zst' in f]

zst_file = all_zst_files[0]


def decompress_tar(tar_file_path):
    tar = tarfile.open(tar_file_path)
    tar.extractall('./')
    tar.close()


def decompress_zstandard(zstd_file_path):
    zstd_file_path = pathlib.Path(zstd_file_path)
    with open(zstd_file_path, 'rb') as compressed:
        decomp = ZstdDecompressor()
        with open('./tar', 'wb') as destination:
            decomp.copy_stream(compressed, destination)
    return './tar'


tar_file_path = decompress_zstandard(zst_file)
decompress_tar(tar_file_path)
os.remove('./tar')
