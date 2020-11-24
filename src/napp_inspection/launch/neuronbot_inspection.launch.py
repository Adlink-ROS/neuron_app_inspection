import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions.node import Node
from pathlib import Path

import pdb
def generate_launch_description():
    # Path
    nb2_launch_dir = os.path.join(get_package_share_directory('neuronbot2_bringup'), 'launch')
    nb2nav_launch_dir = os.path.join(get_package_share_directory('neuronbot2_nav'), 'launch')
    your_map_path = str(Path.home())+'/neuron_app_slam/yourmap.yaml'

    if not os.path.isfile(your_map_path):
        raise RuntimeError('\x1b[0;37;41m'+'Please run Neuron APP SLAM to create your own map first.'+'\x1b[0m')

    # Parameters
    open_rviz = LaunchConfiguration('open_rviz', default='True')
    map_path = LaunchConfiguration('map', default=your_map_path)
    use_camera = LaunchConfiguration('use_camera', default='top')

    neuron_app_bringup = GroupAction([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nb2_launch_dir, 'bringup_launch.py')),
            launch_arguments={'use_camera': use_camera}.items()),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nb2nav_launch_dir, 'bringup_launch.py')),
            launch_arguments={'open_rviz': open_rviz,
                              'map': map_path}.items()),
    ])

    image_saver = Node(
        package='image_view',
        executable='image_saver',
        remappings=[('image', 'color/image_raw')],
        parameters=[{
            'save_all_image': False
            }],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(neuron_app_bringup)
    ld.add_action(image_saver)
    return ld
