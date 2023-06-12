import threading
import time
from database import DataBase
from cosmos_lib2 import *

def saveData():
    data_inf = {}
    client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})
    cosmosdb = client.create_database_if_not_exists(id=database_name)
    container = cosmosdb.create_container_if_not_exists(id="temper_humin",
                                                        partition_key=PartitionKey(path='/id'))
    data_list = read_items(container)
    # print(user_list[user]['id'])
    for i in range(len(data_list)):
        data_inf[data_list[i]['pre_temp']] = data_list[i]['pre_humin']
    print("=============================================")
    print(data_inf)

    threading.Timer(5, saveData).start()


saveData()
