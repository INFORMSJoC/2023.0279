# from __future__ import annotations
from typing import List
from task import Task
import csv, os
import pandas as pd


class Graph:

    def __init__(self, tasks: List[Task], num_stations: int, num_robots: int, name: str = "") -> None:
        self.tasks = tasks
        self.num_stations = num_stations
        self.num_robots = num_robots
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    @staticmethod
    def parse_instance(filepath: str):# -> Graph
        """Import-function for the data set of the generated ALBP-HRC instances (csv files)

        line 1:                     title = ["File name", "Number of stations", "Number of robots", "Number of tasks", "RD", "RF",
                                            "West ratio", "Graph structure", "Desired OS", "Times distribution"]
        line 2:                     data corresponding to line 1
        line 3:                     title = ["Task id", "Human time", "Robot time", "Collaboration time", "Predecessors"]
        line 4 to 4 + num_task - 1  data corresponding to line 3
        """
        tasks = []
        file_name = ""
        num_stations = 0
        num_robots = 0
        num_tasks = 0
        task_index = 1
        with open(filepath, "r", encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            file_index = 0
            for item in csv_reader:
                file_index += 1
                if file_index == 1 or file_index == 3:
                    continue
                elif file_index == 2:
                    file_name = item[0]
                    num_stations = int(item[1])
                    num_robots = int(item[2])
                    num_tasks = int(item[3])
                else:
                    # Create tasks with id and processing times
                    if task_index > num_tasks:
                        break
                    tasks.append(Task(int(item[0])-1, int(item[1]), int(item[2]), int(item[3]))) # task id index from 0 to num_tasks -1
                    predecessor_lsit = str(item[4]).replace(" ","").split(",")
                    for i in range(len(predecessor_lsit)):
                        predecessor = predecessor_lsit[i]
                        if len(predecessor) > 0:
                            tasks[int(item[0]) -1].predecessors.append(int(predecessor) -1)
                    task_index += 1
        csvfile.close()

        print(f"*Import of {filepath} successful!*")
        return Graph(tasks, num_stations, num_robots, file_name)

    @staticmethod
    def create_instances(type_list: List = ["small_dataset_n=20"]):  # -> List[Graph]
        """Creates instances for each type of graphs"""
        main_dir = os.path.dirname(os.getcwd())
        data_dir = f"{main_dir}/data/Instances_Sikora2022"
        instances = [
            Graph.parse_instance(
                f"{data_dir}/{graph}/instance_n={int(graph.split('=')[-1])}_{number}_RF{rf}_R{robot}_S{station}.csv")
            for graph in type_list
            for number, rf, robot, station in Graph.read_sikora_index(graph) ]

        return instances

    @staticmethod
    def read_sikora_index(instance_type):
        main_dir = os.path.dirname(os.getcwd())

        instance_dir = f"{main_dir}/data/Instances_Sikora2022"
        selected_instance_index = "Sikora_CBD_index.xlsx"
        df_index = pd.read_excel(f"{instance_dir}/{selected_instance_index}", header=1)
        num_tasks = int(instance_type.split("=")[-1])
        df = df_index[df_index["# Operations"] == num_tasks]

        instances_paras = []

        for i in range(len(df)):
            task_id = int(df.iloc[i, 0])
            num_stations = int(df.iloc[i, 2])
            num_robots = int(df.iloc[i, 3])
            rf = round(int(df.iloc[i, 4]) / 100, 1)

            tmp_list = [task_id, rf, num_robots, num_stations]
            instances_paras.append(tmp_list)

        return instances_paras


if __name__ =="__main__":
    file_path = "data/Instances/small_dataset_n=20/instance_n=20_1_RD0.4_RF0.4.csv"
    g = Graph.parse_instance(file_path)

    print("############ End of program! ################")
