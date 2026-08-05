import os

from launch.substitutions import Command
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory


def generate_launch_description():
    packageName = 'robot_description'
    urdfFile = 'assembly_1.urdf.xacro'

    pkgShare = get_package_share_directory(packageName)
    urdfPath = os.path.join(pkgShare, 'urdf', urdfFile)

    robotStatePublisherNode = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', urdfPath])
        }]
    )

    jointStatePublisherGuiNnode = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    return LaunchDescription([
        robotStatePublisherNode,
        jointStatePublisherGuiNnode
    ])
