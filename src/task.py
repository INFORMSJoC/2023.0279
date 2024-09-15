# from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Task0:
    id: int
    human_time: int
    predecessors: List[int] = field(default_factory=list, init=False, repr=False, compare=False)

    def is_predecessor(self, other) -> bool:
        """Returns True if self is a predecessor of other"""
        return self.id in other.predecessors
    
    def remove_predecessor(self, other) -> None:
        """Remove a task from the list of predecessors"""
        self.predecessors.remove(other.id)

@dataclass
class Task:
    id: int
    human_time: int
    robot_time: int # -1 means the task can not assembled by the robot
    collaboration_time: int # -1 means the task can not assembled by the robot
    predecessors: List[int] = field(default_factory=list, init=False, repr=False, compare=False)

    max_task_time: int = field(default=-1, init=False)
    min_task_time: int = field(default=-1, init=False)
    successors: List[int] = field(default_factory=list, init=False)
    all_predecessors: List[int] = field(default_factory=list, init=False)
    all_successors: List[int] = field(default_factory=list, init=False)

    earliest_station: int = field(default=-1, init=False)
    latest_station: int = field(default=-1, init=False)
    feasible_stations: List[int] = field(default_factory=list, init=False)

    assembly_resource: int = -1 # 0/1/2

    def is_predecessor(self, other) -> bool:
        """Returns True if self is a predecessor of other"""
        return self.id in other.predecessors

