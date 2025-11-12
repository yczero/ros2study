from setuptools import find_packages, setup

package_name = 'my_first_pack'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zero',
    maintainer_email='zero@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_first_node = my_first_pack.my_first_node:main',
            'my_subscriber = my_first_pack.my_subscriber:main',
            'my_publisher = my_first_pack.my_publisher:main',
            'my_custom_publisher = my_first_pack.my_custom_publisher:main',
            'turtle_cmd_and_pose = my_first_pack.turtle_cmd_and_pose:main',
            'my_service_server = my_first_pack.my_service_server:main',
            'dist_turtle_action_server = my_first_pack.dist_turtle_action_server:main'
        ],
    },
)
