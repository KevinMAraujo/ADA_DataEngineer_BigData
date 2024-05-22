# Databricks notebook source
# MAGIC %md
# MAGIC Instalando o Great Expectations

# COMMAND ----------

# MAGIC %pip install great-expectations

# COMMAND ----------

from datetime import datetime
import great_expectations as gx
from great_expectations.checkpoint import Checkpoint

# Importar o módulo SparkDFDataset do Great Expectations
from great_expectations.dataset import SparkDFDataset

# COMMAND ----------

def verifica_colunas_datetime(gx_df, colunas_datetime:list):
    for coluna in colunas_datetime:
        condicao_tipo = gx_df.expect_column_values_to_be_in_type_list(coluna, ['TimestampType']).success
        condicao_data_valida = gx_df.expect_column_values_to_be_between(coluna, datetime(2008,8,1), datetime.now()).success
        if condicao_tipo and condicao_data_valida:
            print(f"A coluna '{coluna}' é válida. (Tipo e Valor)")
        else:
            if not condicao_tipo:
                print(f"ERRO: A coluna '{coluna}' não está no formato correto. Esperado: timestamp.")
            if not condicao_data_valida:
                print(f"ERRO: A coluna '{coluna}' tem valores fora do intervalo permitido.")

# COMMAND ----------

def verificar_colunas_categoricas(gx_df, coluna_a_ser_analisada, valores_esperados):
    result = gx_df.expect_column_values_to_be_in_set(coluna_a_ser_analisada, valores_esperados)
    if result.success:
        print(f"Os valores da coluna {coluna_a_ser_analisada} contêm apenas valores esperados. ({valores_esperados})")
    else:
        print(f"ERRO: Os valores da coluna {coluna_a_ser_analisada} contêm valores inesperados. ({result.result['unexpected_list']})")

# COMMAND ----------

def verificar_colunas_booleanas(gx_df, list_of_columns:list):
    for column in list_of_columns:
        condicao_tipo = gx_df.expect_column_values_to_be_in_type_list(column, ['int', 'int64']).success
        condicao_valor_valido = gx_df.expect_column_values_to_be_in_set(column, [0, 1]).success
        if condicao_tipo and condicao_valor_valido:
            print(f"A coluna '{column}' é válida. (Tipo e Valor)")
        else:
            if not condicao_tipo:
                print(f"ERRO: A coluna '{column}' não está no tipo correto. Esperado: int.")
            if not condicao_valor_valido:
                print(f"ERRO: A coluna '{column}' tem valores inválidos.")                

# COMMAND ----------

def verificar_colunas_com_none(gx_df, list_of_columns:list):
    for column in list_of_columns:
        condicao_valores_nulos = gx_df.expect_column_values_to_not_be_null(column).success
        if condicao_valores_nulos:
            print(f"A coluna '{column}' é válida. (Não tem valores nulos)")
        else:
            print(f"ERRO: A coluna '{column}' contém valores nulos.")

# COMMAND ----------

def verificar_valores_min_max(gx_df, list_of_columns:list, min, max):
    for column in list_of_columns:
        condicao_valores = gx_df.expect_column_values_to_be_between(column, min_value=min, max_value=max).success
        if condicao_valores:
            print(f"A coluna '{column}' está entre os valores de {min} e {max}.")
        else:
            print(f"ERRO: A coluna '{column}' não está entre os valores de {min} e {max}.")

# COMMAND ----------

def verificar_colunas_id(gx_df, list_of_id_columns:list):

    correct_types = ['LongType']
    for column in list_of_id_columns:
        condicao_tipo = gx_df.expect_column_values_to_be_in_type_list(column, correct_types).success
        condicao_valores_nulos = gx_df.expect_column_values_to_not_be_null(column).success
        valor_max_bigint = 9223372036854775807
        condicao_valores = gx_df.expect_column_values_to_be_between(column, min_value=0, max_value=valor_max_bigint).success

        if condicao_tipo and condicao_valores_nulos and condicao_valores:
            print(f"A coluna '{column}' é válida. (Tipo e Valor)")
        else:
            if not condicao_tipo:
                print(f"ERRO: A coluna '{column}' não está no tipo correto. Esperado: ",' ou '.join(correct_types))
            if not condicao_valores_nulos:
                print(f"ERRO: A coluna '{column}' possui valore(s) nulos.")
            if not condicao_valores:
                print(f"ERRO: A coluna '{column}' possui valore(s) acima ou abaixo do range permitido {[0,valor_max_bigint]}.")