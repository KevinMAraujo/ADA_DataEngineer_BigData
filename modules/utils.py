# Databricks notebook source
import os


def create_path(path):
    """
    Criar diretório.

    Parameters
    ----------
    path: string
        Caminho do diretório.

    Returns
    -------
    null

    """
    path_name = path.rsplit('/', 2)[1]

    if not os.path.exists(path):
        dbutils.fs.mkdirs(path)
        print(f'\n A pasta {path_name} foi criada.')
    else:
        print(f'\n A pasta {path_name} já existe.')
                