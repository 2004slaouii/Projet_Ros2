from setuptools import setup

package_name = 'sensor_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Sensor node for detecting light position',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'sensor = sensor_node.sensor:main',
        ],
    },
)
