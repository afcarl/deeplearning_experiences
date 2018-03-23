import os

def get_path(dataset):
    home = os.path.expanduser('~')

    folder = os.path.join(home, 'datasets_pytorch')
    if not os.path.exists(folder):
        os.mkdir(folder)

    return os.path.join(folder, dataset)