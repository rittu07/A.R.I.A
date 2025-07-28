from setuptools import setup
import os
from glob import glob

package_name = 'helrit_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Install resource index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # Install package.xml
        ('share/' + package_name, ['package.xml']),

        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),

        # Install robot_description (your xacro files)
        (os.path.join('share', package_name, 'robot_description'),
            glob('robot_description/*.xacro')),  # ONLY .xacro files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rittu',
    maintainer_email='rittu@example.com',
    description='Robot description and launch files for helrit_bot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

