import numpy as np
import h5py
from silx.io import fabioh5, convert
from pathlib import Path

EXTENSION_H5 = '.h5'


def create_h5_from_folder(directory='', pattern='*.edf', h5_file=''):
    # Transform string into Path instance
    directory = Path(directory)

    fabio_series = get_fabioserie_from_dir(
        directory=directory,
        pattern=pattern,
    )

    if not h5_file:
        h5_file = directory.joinpath(f'{directory.name}{EXTENSION_H5}')
    
    convert.write_to_h5(
        infile=fabio_series,
        h5file=str(h5_file),
        h5path=str(directory),
        mode='a',
        overwrite_data=True,
    )


def search_files_recursively(directory=str(), pattern='*.edf'):
    # Transform string into Path instance
    directory = Path(directory)

    # Return if the path does not exist
    if not directory.exists():
        return None
    
    # Search files recursively
    list_files = sorted(
        directory.rglob(
            pattern=pattern,
        )
    )
    return list_files


def get_fabioserie_from_dir(directory=str(), pattern='*.edf'):
    """
    Args:
        path_of_files (_type_, optional): _description_. Defaults to str().
        wildcards (str, optional): _description_. Defaults to '*.edf'.
    """
    list_files = search_files_recursively(
        directory=directory,
        pattern=pattern,
    )
    fabio_serie = fabioh5.File(file_series=list_files)
    return fabio_serie