# Neuron APP: Inspection

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage

1. Launch Navigation as well as Rviz with the Gazebo simulation.
    ```
    ros2 launch napp_inspection gazebo_inspection.launch.py
    ```
2. Launch Behavior Tree and camera snapshot.
    ```
    ros2 launch napp_inspection bt_inspection_snapshot.launch.py
    ```
 ![](readme_resource/bt_demo.gif)
