# Databricks notebook source
# Strings json para criação do schema dos campos atráves da StructType

#### ao final é gerado uma lista de variaveis com todas as strings

d_accounts = '''
{
    "fields":[
        {
            "metadata":{},
            "name":"account_id",
            "nullable":false,
            "type":"long"
        },{
            "metadata":{},
            "name":"status",
            "nullable":true,
            "type":"string"
        },{
            "metadata":{},
            "name":"account",
            "nullable":false,
            "type":"string"
        },{
            "metadata":{},
            "name":"created_at",
            "nullable":true,
            "type":"timestamp"
        }
    ],
    "type":"struct"
}
'''

f_movements = ''' 
{
    "fields":[
        {
            "metadata":{},
            "name":"account_id",
            "nullable":false,
            "type":"long"
        },{
            "metadata":{},
            "name":"amount",
            "nullable":true,
            "type":"double"
        },{
            "metadata":{},
            "name":"in_or_out",
            "nullable":true,
            "type":"string"
        },{
            "metadata":{},
            "name":"status",
            "nullable":true,
            "type":"string"
        },{
            "metadata":{},
            "name":"requested_at",
            "nullable":true,
            "type":"integer"
        },{
            "metadata":{},
            "name":"completed_at",
            "nullable":true,
            "type":"string"
        }
    ],
    "type":"struct"
}
'''  


json_str_list_silver = [d_accounts, f_movements]