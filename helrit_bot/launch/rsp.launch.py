from launch import LaunchDescription
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('helrit_bot')
    xacro_file = os.path.join(pkg_share, 'robot_description', 'helrit_bot.urdf.xacro')

    # Convert xacro to URDF
    from xacro import process_file
    doc = process_file(xacro_file)
    robot_description_config = doc.toxml()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_config}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        )
    ])
