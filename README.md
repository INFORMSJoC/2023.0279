[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# An Improved Combinatorial Benders Decomposition Algorithm for the Human-Robot Collaborative Assembly Line Balancing Problem

This archive is distributed in association with the [INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc)
under the MIT [License](LICENSE.md).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper
[An improved combinatorial Benders decomposition algorithm for the human-Robot collaborative assembly line balancing problem](https://doi.org/10.1287/ijoc.2023.0279).

## Cite

To cite the contents of this repository, please cite both the paper and this
repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2023.0279

https://doi.org/10.1287/ijoc.2023.0279.cd

Below is the BibTex for citing this snapshot of the repository.

```
@misc{Huang2024,
  author =        {D. Huang, Z. Mao, K. Fang, E. Fu and M. Pinedo},
  publisher =     {INFORMS Journal on Computing},
  title =         {{An improved combinatorial Benders decomposition algorithm for the human-Robot collaborative assembly line balancing problem}},
  year =          {2024},
  doi =           {10.1287/ijoc.2023.0279.cd},
  url =           {https://github.com/INFORMSJoC/2023.0279},
  note =          {Available for download at https://github.com/INFORMSJoC/2023.0279},
}
```

## Description

This software implements an improved combinatorial Benders decomposition
algorithm for the human-Robot collaborative assembly line balancing problem.

## Usage

To reproduce the results in our paper, run:
```
python src/main.py
```

## Data

The data in `data/Instances_Sikora2022` are from the papers of [Weckenborg et al. (2020)](http://dx.doi.org/10.1007/s40685-019-0101-y)
and [Sikora and Weckenborg (2022)](https://dx.doi.org/10.1080/00207543.2022.2093684).
The data was provided to us by personal communication with Dr Sikora, and we are
redistributing the data with their permission.
