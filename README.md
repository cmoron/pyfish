# Fish Swarm Multi-Agent Simulation

## Overview

This project is a basic multi-agent system simulating the behavior of a fish swarm in a 2D environment. Fish agents move according to a set of simple rules based on potential fields. The fish agents are attracted to food and repelled by predators, while also maintaining a certain distance from each other. The simulation is visualized using Pygame.

## Features

- 2D graphical representation using Pygame
- Fish agents with basic behavior based on potential fields
- Attraction towards food elements in the environment
- Repulsion from predator elements and other fish agents
- Simple exploration behavior for fish agents
- Dynamic addition of food and predator elements during simulation

## Installation

### Prerequisites

- Python 3.x
- Pygame

### Steps

1. Clone the repository.
    ```bash
    git clone https://github.com/your_username/your_project_name.git
    ```

2. Navigate to the project directory.
    ```bash
    cd your_project_name
    ```

3. Install the requirements.
    ```bash
    pip install -r requirements.txt
    ```

4. Run the main script.
    ```bash
    python src/main.py
    ```

## Usage

Run `main.py` to start the simulation. The fish agents will move according to the behavior defined in `src/physics/potential_fields.py`. You can modify the constants in this file to alter the behavior of the agents.

## Contributing

Feel free to fork this repository and create a pull request if you have something to add.

## License

MIT License

