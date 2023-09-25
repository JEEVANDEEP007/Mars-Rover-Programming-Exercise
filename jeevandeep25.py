from abc import ABC, abstractmethod

# Command pattern: Define commands as objects
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete commands
class MoveCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.move()

class LeftTurnCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_left()

class RightTurnCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_right()

# Rover class
class Rover:
    def __init__(self, x, y, direction, grid, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.obstacles = obstacles

    def move(self):
        new_x, new_y = self._get_new_position()
        if self._is_valid_move(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def _get_new_position(self):
        if self.direction == 'N':
            return self.x, self.y + 1
        elif self.direction == 'S':
            return self.x, self.y - 1
        elif self.direction == 'E':
            return self.x + 1, self.y
        elif self.direction == 'W':
            return self.x - 1, self.y

    def _is_valid_move(self, new_x, new_y):
        if (new_x, new_y) in self.obstacles:
            return False
        return 0 <= new_x < self.grid[0] and 0 <= new_y < self.grid[1]

    def get_status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."

# Composite Pattern: Represent the grid and obstacles
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

if __name__ == "__main__":
    # Initialize the grid and obstacles
    grid = Grid(10, 10)
    grid.add_obstacle(2, 2)
    grid.add_obstacle(3, 5)

    # Initialize the rover
    rover = Rover(0, 0, 'N', (10, 10), grid.obstacles)

    # Execute commands
    commands = ['M', 'M', 'R', 'M', 'L', 'M']
    for cmd in commands:
        if cmd == 'M':
            move_command = MoveCommand(rover)
            move_command.execute()
        elif cmd == 'L':
            left_turn_command = LeftTurnCommand(rover)
            left_turn_command.execute()
        elif cmd == 'R':
            right_turn_command = RightTurnCommand(rover)
            right_turn_command.execute()

    # Get the status report
    status_report = rover.get_status_report()
    print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
    print(status_report)
