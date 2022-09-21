"""
    Cleaning the data
"""
import logging
import string
from pathlib import Path

import pandas as pd

logging.basicConfig(filename = 'log.txt', format = '%(levelname)s:%(message)s'\
                    , level = logging.INFO)

def data_cleaning(file: str,work_dir: str = Path.cwd()) -> pd.DataFrame:
    """
        Clear all our data
    """

    logging.info("Cleaning".center(50,"*"))
    df = pd.read_csv(work_dir + '/' + file)
    logging.info("Doing the address more clean")
    df['address'] = df['address'].str.replace(r'['+ string.punctuation + ']'," ",)
    logging.info("Reviews has more than reviews, bad")
    df['reviews_list'] = df['reviews_list'].str.replace(r'['+ string.punctuation + ']'," ")
    df['phone'] = df['phone'].str.replace(r'[+ ]',"")
    logging.info("Doing my better")
    df[['contact number 1','contact number 2']] = df['phone'].str\
                                                .split("\r\n",expand=True).fillna("No info")
    logging.info("Nulls information".center(50,"*"))
    logging.info(df.isnull().sum())
    logging.info("*" * 50 )
    return df
    