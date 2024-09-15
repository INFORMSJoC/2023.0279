from exporter import Exporter
from graph import Graph
from time import perf_counter
from typing import Dict, List
from datetime import datetime
import pandas as pd
import gc, os
from cbd import CBD
from tqdm import tqdm


def run_experiments(instances: List[Graph], optimizers: List[str], extra_info1: str) -> List[Dict]:
    main_dir = os.path.dirname(os.getcwd())
    SALOME_result_file = f"{main_dir}/data/Instances_Sikora2022/SALOME_result_file.xlsx"
    df = pd.read_excel(SALOME_result_file)

    for optimizer in optimizers:
        extra_info = f"{optimizer}_{extra_info1}"
        is_title = True
        for instance in tqdm(instances):
            if optimizer == "CBD":
                experiment = CBD()
            else:
                exit(f"### the optimizer model is not available, got model: {optimizer} ###")

            experiment.SALOME_result = df.copy()
            experiment.run(instance)
            # write current instance's result
            Exporter.export_instance_result(experiment.solutions, optimizer, extra_info, is_title)
            is_title = False

            del experiment
            gc.collect()

def main():

    # instances type
    type_list = ["small_dataset_n=20", "medium_dataset_n=50", "large_dataset_n=100"]
    # Create instances and optimization procedures
    instances = Graph.create_instances(type_list=type_list)
    optimizers = ["CBD"]
    extra_info = "all_instances"

    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    extra_info = f"{now}_{extra_info}"

    # run experiments
    run_experiments(instances, optimizers, extra_info)


if __name__ == "__main__":
    main()
    print("\n ####### End of main function! ########")
