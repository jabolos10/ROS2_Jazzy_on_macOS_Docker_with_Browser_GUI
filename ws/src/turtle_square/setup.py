from setuptools import find_packages, setup

package_name = 'turtle_square'

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
    maintainer='Oskar Jablonowski',
    maintainer_email='jablonowskioskar8@gmail.com',
    description='Drives turtlesim turtle in a square using Twist messages',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'square_driver = turtle_square.square_driver:main'
        ],
    },
)
