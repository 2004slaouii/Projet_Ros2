import subprocess
import time

def run_command(command, wait_for=0):
    """Execute a shell command."""
    print(f"Executing: {command}")
    process = subprocess.Popen(command, shell=True)
    if wait_for > 0:
        time.sleep(wait_for)  # Wait for a specific time before moving to the next step
    return process

# Step 1: Launch turtlesim_node
run_command("ros2 run turtlesim turtlesim_node", wait_for=3)

# Step 2: Spawn a turtle at (5.0, 5.0) with name 'light'
run_command("ros2 service call /spawn turtlesim/srv/Spawn '{x: 5.0, y: 5.0, theta: 0.0, name: \"light\"}'", wait_for=2)

# Step 3: Disable the pen for the 'light' turtle
run_command('''ros2 service call /light/set_pen turtlesim/srv/SetPen "{'r': 0, 'g': 0, 'b': 0, 'width': 1, 'off': 1}"''', wait_for=2)

# Step 4: Run the light_publisher node
run_command("ros2 run light_source light_publisher", wait_for=2)

# Step 5: Run the light_indicator node
run_command("ros2 run light_source light_indicator", wait_for=2)

# Step 6: Run the sensor node
run_command("ros2 run sensor_node sensor", wait_for=2)

# Step 7: Run the light_follower node
run_command("ros2 run light_follower follower")

print("All commands executed!")






