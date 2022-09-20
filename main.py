from data_quality import data_cleaning
from file_check import watcher

if __name__ == '__main__':   
    file_ = watcher('AmplivaTest/test_folder',5)
    data_cleaning(file_,'AmplivaTest/test_folder')
