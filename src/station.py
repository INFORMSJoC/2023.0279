from collections.abc import Sequence
from dataclasses import dataclass, field
from task import Task
from typing import List, Dict


@dataclass(eq=False)
class Station(Sequence):
    station_id: int
    no_robot: bool = field(default=True, init=False)
    station_time: int = field(default=0, init=False)
    feasible_tasks: List[int] = field(default_factory=list, init=False)
    assigned_tasks: List[int] = field(default_factory=list, init=False)
    start_time_resource: List[Dict] = field(default_factory=list, init=False) #task_id, start_time, assembly_resource

    
    def __getitem__(self, key):
        """Return the task at index of the Stations task list"""
        return self.assigned_tasks[key]
    
    def __len__(self):
        return len(self.assigned_tasks)
        
    def empty(self) -> bool:
        """Returns True if there are no tasks assigned to the Station"""
        return len(self) == 0