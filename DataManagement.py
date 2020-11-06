import kaggle

from pathlib import Path


def download_competition_data(competition_name: str, path: str = None) -> None:
    """
    Downloads data from a Kaggle competition. This function works similarly to the Kaggle cli command.
    Example:
        kaggle competitions download -c titanic
            is equivalent to
        doanload_competition_data("titanic")
    :param competition_name: name of the competition whose data is to be downloaded
    :param path: path to save the downloaded files to. If not specified, downloads to the root of the working directory.
    :return: None
    """
    if path is None:
        path = Path.cwd()

    kaggle.api.authenticate()
    kaggle.api.competition_download_cli(competition_name, path=path)


if __name__ == '__main__':
    kaggle.api.authenticate()
    kaggle.api.competition_download_cli('titanic')
