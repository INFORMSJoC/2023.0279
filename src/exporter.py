import csv, os
import pathlib
from typing import Dict, List


class Exporter:
    
    @staticmethod
    def _write_csv(filepath, solutions: List[Dict], is_title, write_mode, optimizer) -> None:
        """Exports solutions to csv"""

        # optimizer = filepath.split("/")[1]
        if optimizer[0:3] == "CBD":
            fieldnames = ['Optimizer', 'Instance', 'Cycle time', 'Runtime', 'CBD-UB', 'CBD-LB', 'Iteration', 'Cut', 'Feasibilty cut',
                          'Optimality cut', 'Vairable fixing cut', 'Runtime-M', 'Runtime-M1', 'Runtime-M2', 'Runtime-S']
        else:
            exit(f"### the optimizer model is not available, got model: {optimizer} ###")

        with open(filepath, write_mode, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if is_title:
                writer.writeheader()

            for solution in solutions:
                # write solution to csv
                writer.writerow(solution)
            
    @classmethod
    def export_results(cls, solutions: List[Dict], optimizers: List[str], extra_info: str = "", is_title: bool = True) -> None:
        """Export all results to a single csv-file"""
        
        # Set filepath
        main_dir = os.path.dirname(os.getcwd())
        filepath = f"{main_dir}/results/{extra_info}.csv"
        
        cls._write_csv(filepath, solutions, is_title, 'w', optimizers[0])


    @classmethod
    def export_instance_result(cls, instance_solutions: List[Dict], optimizer: str, extra_info: str = "", is_tile: bool = False) -> None:
        """Export the results of solving an instance to a separate csv-file"""

        main_dir = os.path.dirname(os.getcwd())
        filepath = f"{main_dir}/results/{optimizer}/{extra_info}.csv"

        cls._write_csv(filepath, instance_solutions, is_tile, 'a', optimizer)

